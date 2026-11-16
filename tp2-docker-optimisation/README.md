# Rapport TP Optimisation Docker

**Auteur :** DELTHIL Tristan

## 1. Point de départ

L'application est un serveur Node.js (`express`) avec deux routes : `/` et `/big`.
J'ai mesuré la taille avec la commande ci-dessous :

```bash
docker images tp-node:v0
```

```text
IMAGE        ID             DISK USAGE   CONTENT SIZE
tp-node:v0   56e9c40210a4       1.88GB          464MB
```

L'image de départ fait **1.88 GB**.

### Mauvaises pratiques repérées

- `node:latest` : image Debian complète et lourde.
- `apt-get install build-essential` : outils de compilation qui n'est pas forcément utile dans notre cas.
- `COPY node_modules` puis `npm install` : doublon, et pas de `.dockerignore`.
- `COPY . /app` avant `npm install` : le cache est perdu à chaque modification du code.
- `NODE_ENV=development` et `USER root`.
- `EXPOSE 3000 4000 5000` alors que le serveur n'écoute que sur le port 3000.
- `mongodb` et `nodemon` installés mais jamais utilisés en production.
- Un seul stage : tout reste dans l'image finale.

## 2. Itérations

J'ai fait une étape à la fois, avec un commit par étape et une mesure de la taille à chaque fois.

| Version | Changement | Taille |
|---|---|---|
| v0 | Dockerfile de départ | 1.88 GB |
| v1 | Image `alpine` et `.dockerignore` | 223 MB |
| v2 | Ordre des instructions (cache) | 223 MB |
| v3 | Multi-stage et `npm ci --omit=dev` | 218 MB |
| v4 | Sans `mongodb`, `NODE_ENV=production`, utilisateur `node` | 199 MB |

### v1 : image légère et `.dockerignore`

- J'ai remplacé `node:latest` par `node:20-alpine`.
- J'ai supprimé `build-essential` et le `COPY node_modules`.
- J'ai ajouté un `.dockerignore` (`node_modules`, `.git`).
- Impact : **1.88 GB à 223 MB**.

### v2 : cache des layers

- `package*.json` est copié avant le code, puis `npm ci`, puis `COPY . .`.
- Impact : la taille ne change pas, mais après une modification de `server.js` le rebuild passe de 3 secondes à moins d'1 seconde car les dépendances restent en cache.

### v3 : multi-stage

- L'étape `build` installe tout et l'image finale ne reçoit que `server.js`.
- Impact : **223 MB à 218 MB**. Le gain est faible car l'application est minuscule.

### v4 : dépendances et sécurité

- J'ai retiré `mongodb`, qui n'est jamais utilisé dans `server.js`.
- `NODE_ENV=production` et `USER node` à la place de root.
- `EXPOSE 3000` uniquement.
- Impact : **218 MB à 199 MB** et le conteneur ne tourne plus en root.

## 3. Dockerfile final

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --from=build --chown=node:node /app/server.js ./
EXPOSE 3000
USER node
CMD ["node", "server.js"]
```

## 4. Résultat

- La taille passe de **1.88 GB à 199 MB**.
- Les rebuilds sont plus rapides grâce au cache.
- Le conteneur ne tourne plus en root.

Pour lancer l'image :

```bash
cd tpdockeroptimisation
docker build -t tp-node:final .
docker run -p 3000:3000 tp-node:final
```