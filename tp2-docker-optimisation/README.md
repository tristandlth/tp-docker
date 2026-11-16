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

### v1 : image légère et `.dockerignore`

- J'ai remplacé `node:latest` par `node:20-alpine`.
- J'ai supprimé `build-essential` et le `COPY node_modules`.
- J'ai ajouté un `.dockerignore` (`node_modules`, `.git`).
- Impact : **1.88 GB à 223 MB**.
