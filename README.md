# TP Docker

## Exercice : Manipulation de base des conteneurs

## Question 1

```bash
docker --version
```

```text
Docker version 29.9.2, build a82e528
```

---

## Question 2

```bash
docker images
```

```text
IMAGE                             ID             DISK USAGE   CONTENT SIZE   EXTRA
alpine:3.20                       d9e853e87e55       13.7MB         4.17MB        
curlimages/curl:latest            7c12af72ceb3       37.4MB         10.9MB        
gameboxd-backend:latest           6baf3d9a5143        598MB          136MB        
gameboxd-frontend:latest          69e73f9ba8a3        245MB         63.5MB        
gameboxd-test:latest              2a2907059b03        594MB          136MB        
party-games-server:latest         30f7abc8e323        330MB         75.3MB        
party-games-web:latest            1730df1538af        240MB         60.5MB        
postgres:16-alpine                cf78e76683b9        411MB          115MB        
postgres:17-alpine                18cfe3ef5e68        415MB          116MB    U   
postgres:18                       4ef4dbc939d6        672MB          167MB        
rayns-backend:architecture-test   7625dbe6696a        680MB          165MB        
rayns-bot:architecture-test       2858b41c3867        626MB          158MB        
rayns-canvas-dev:latest           c1f7d23e9361       1.74GB          421MB        
rayns-tcg-app:latest              d22cd1e073ea        2.6GB         1.21GB        
rayns-v3-api:latest               2ccc55067cd8        775MB          166MB    U   
rayns-v3-casino-loop:latest       c7fad6f1c0d4        775MB          166MB    U   
rayns-v4-api:latest               f84d0ea1d4bf        771MB          166MB    U   
rayns-web:architecture-test       8af1ac668f49        352MB         81.3MB        
redis:7-alpine                    ff02b58f971e       58.7MB         17.3MB        
redis:7.4-alpine                  6ba19c50b567       58.7MB         17.3MB    U   
tcg-app:latest                    b3cae30d2066        242MB         63.7MB
```

---

## Question 3

```bash
docker pull hello-world
```

```text
Using default tag: latest
latest: Pulling from library/hello-world
58dee6a49ef1: Pull complete 
c3bdf82c34d1: Download complete 
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

---

## Question 4

```bash
docker run hello-world
```

```text
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

---

## Question 5

```bash
docker ps
```

```text
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

---

## Question 6

```bash
docker ps -a
```

```text
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                     PORTS     NAMES
3109f1bf5c0b   hello-world            "/hello"                 8 minutes ago   Exited (0) 5 minutes ago             silly_bell
6492213834a2   rayns-v4-api           "sh -c 'python manag…"   6 days ago      Exited (137) 6 days ago              rayns-v4-api-1
48d23b035e5a   postgres:17-alpine     "docker-entrypoint.s…"   6 days ago      Exited (0) 6 days ago                rayns-v4-db-1
68195e55758e   redis:7.4-alpine       "docker-entrypoint.s…"   6 days ago      Exited (0) 6 days ago                rayns-v4-redis-1
841968f6f778   rayns-v3-casino-loop   "python manage.py ca…"   11 days ago     Exited (137) 8 days ago              rayns-v3-casino-loop-1
387bf6b84601   rayns-v3-api           "sh -c 'python manag…"   11 days ago     Exited (137) 8 days ago              rayns-v3-api-1
42d91ad166a8   postgres:17-alpine     "docker-entrypoint.s…"   11 days ago     Exited (0) 8 days ago                rayns-v3-db-1
58953cb7331f   redis:7.4-alpine       "docker-entrypoint.s…"   11 days ago     Exited (0) 8 days ago                rayns-v3-redis-1
3ebe61ff2e44   postgres:17-alpine     "docker-entrypoint.s…"   4 weeks ago     Exited (0) 4 weeks ago               rayns-tcg-db-1
```

---

## Question 7

```bash
docker rm 3109f1bf5c0b
```

```text
3109f1bf5c0b
```

---

## Question 8

```bash
docker rmi hello-world
```

```text
Untagged: hello-world:latest
Deleted: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
```

---

## Exercice : Création d'un serveur web avec Docker

## Question 1
```bash
docker pull nginx
```

```text
Using default tag: latest
latest: Pulling from library/nginx
1f7e08c0f6ab: Pull complete 
acd43e9bebc3: Pull complete 
34a564bc5d28: Pull complete 
3559a01b6a80: Pull complete 
c64233207369: Pull complete 
c19b54656735: Pull complete 
998fb033610b: Pull complete 
986a63116111: Download complete 
61b74d3d884f: Download complete 
Digest: sha256:165ddde8751e75a1c907d24ef10d9f6deb08b57e0fe56caf67512486aff76d82
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
```
---

## Question 2

```bash
docker run -d -p 8080:80 --name mon_nginx nginx
```

```text
f75cbdef37e34c16999f60646efb0c95805424260f75b3020e58caf3acb97a98
```

---

## Question 3

```bash
docker run -d -p 8080:80 --name mon_nginx nginx
```

```text
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     NAMES
f75cbdef37e3   nginx     "/docker-entrypoint.…"   43 seconds ago   Up 42 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
```

---

## Question 4

La page est accessible et affiche : "Welcome to nginx!".

---

## Question 5

```bash
docker stop mon_nginx
```

```text
mon_nginx
```

Il n'apparaît plus dans ```docker ps``` donc il a bien été arrêté.

---

## Question 6

```bash
docker rm mon_nginx
```

```text
mon_nginx
```

---

## Exercice : Déploiement d'une application Python Flask

### Build

```bash
docker build -t flask-hello .
```

```text
[+] Building 11.0s (10/10) FINISHED                                                                                                               docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                              0.0s
 => => transferring dockerfile: 199B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                                                               1.8s
 => [internal] load .dockerignore                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                         5.4s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                         0.0s
 => => extracting sha256:acd43e9bebc37bc4ba7a5f47bd7598913337803e53d468f37d940f11f5d5f1ef                                                                         0.6s
 => => sha256:70b4f81c82dc6ea2a5fc08c59c75940cc3f45dad8e2038b7773cd1b6ac24c7a0 249B / 249B                                                                        0.2s
 => => sha256:0ba3a3e89cd986f09d548ebfd13261fd4ad86bb310bb69923010538e0c5ce222 12.06MB / 12.06MB                                                                  5.2s
 => => sha256:0373269344dc260a94623aecbafee3cf336984ad3bbe8a49ac047d85aa69be9b 1.27MB / 1.27MB                                                                    0.9s
 => => extracting sha256:0373269344dc260a94623aecbafee3cf336984ad3bbe8a49ac047d85aa69be9b                                                                         0.0s
 => => extracting sha256:0ba3a3e89cd986f09d548ebfd13261fd4ad86bb310bb69923010538e0c5ce222                                                                         0.2s
 => => extracting sha256:70b4f81c82dc6ea2a5fc08c59c75940cc3f45dad8e2038b7773cd1b6ac24c7a0                                                                         0.0s
 => [internal] load build context                                                                                                                                 0.0s
 => => transferring context: 456B                                                                                                                                 0.0s
 => [2/5] WORKDIR /app                                                                                                                                            0.2s
 => [3/5] COPY requirements.txt .                                                                                                                                 0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                                      2.9s
 => [5/5] COPY . .                                                                                                                                                0.0s
 => exporting to image                                                                                                                                            0.7s
 => => exporting layers                                                                                                                                           0.3s
 => => exporting manifest sha256:6af0ffcbb87984bfbe9044ed24697725b1ceaefde9acdd7d58ee552960262c81                                                                 0.0s
 => => exporting config sha256:7c7b2c19c2210fc1022a708e0953d31a375d6dbd3391d592905cca1db0ca0c1c                                                                   0.0s
 => => exporting attestation manifest sha256:fa33b7799c26aa933b50f94cf48c68094085e5222f41b3634e36a5293da02297                                                     0.0s
 => => exporting manifest list sha256:bbb2483666aab2418102538305c3acf7022e939b0df0ae30c6f19ee2888257ec                                                            0.0s
 => => naming to docker.io/library/flask-hello:latest                                                                                                             0.0s
 => => unpacking to docker.io/library/flask-hello:latest   
```

### Lancement du conteneur

```bash
docker run -d -p 5001:5000 flask-hello
```

```text
5e934ce7348cce4f4988a5e5d80f4a9825a936c28e4d4084892420452f041e78
```

### Test de l'application depuis le navigateur

L'application est bien lancé sur le port 5001 et affiche "Hello, World!".
J'ai utilisé le port 5001 car je suis sur Mac et le port 5000 par défaut pour Flask est déjà utilisé par Airplay.

---

## Exercice : Utilisation de docker compose

### Lancement du docker compose

```bash
docker compose up -d --build
```

```text
[+] Building 0.8s (12/12) FINISHED                                                                                                                                     
 => [internal] load local bake definitions                                                                                                                        0.0s
 => => reading from stdin 596B                                                                                                                                    0.0s
 => [internal] load build definition from Dockerfile                                                                                                              0.0s
 => => transferring dockerfile: 199B                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12-slim                                                                                               0.6s
 => [internal] load .dockerignore                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                   0.0s
 => [1/5] FROM docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                         0.0s
 => => resolve docker.io/library/python:3.12-slim@sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b                                         0.0s
 => [internal] load build context                                                                                                                                 0.0s
 => => transferring context: 389B                                                                                                                                 0.0s
 => CACHED [2/5] WORKDIR /app                                                                                                                                     0.0s
 => CACHED [3/5] COPY requirements.txt .                                                                                                                          0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                                                                               0.0s
 => [5/5] COPY . .                                                                                                                                                0.0s
 => exporting to image                                                                                                                                            0.0s
 => => exporting layers                                                                                                                                           0.0s
 => => exporting manifest sha256:9a6c972ce528621f2fbce8673e32fc74e28994ca3fbb0a924e6d8184e0f7a4b5                                                                 0.0s
 => => exporting config sha256:18a0876e92f9067f8f0dcf1be16f6fc7b59b4a35ba76ba6f1749f3b8730916d1                                                                   0.0s
 => => exporting attestation manifest sha256:059319206a7614ef4a069c5f2631a51c4b43796e2e5bca8166a2fefecd52a759                                                     0.0s
 => => exporting manifest list sha256:188266407094fc582a90218ccfc72f8b27e4c2dad74f031ce1d1afa6c6bfeccc                                                            0.0s
 => => naming to docker.io/library/flask-docker-web:latest                                                                                                        0.0s
 => => unpacking to docker.io/library/flask-docker-web:latest                                                                                                     0.0s
 => resolving provenance for metadata file                                                                                                                        0.0s
[+] up 4/4
 ✔ Image flask-docker-web         Built                                                                                                                            0.9s
 ✔ Volume flask-docker_mongo-data Created                                                                                                                          0.0s
 ✔ Container flask-docker-mongo-1 Started                                                                                                                          3.3s
 ✔ Container flask-docker-web-1   Started
```

### Vérification de la connexion à la base de données

J'ai ajouté une route /db sur l'application Flask qui doit renvoyer ```Connexion MongoDB OK``` dans le cas où la connexion fonctionne.
Lorsque je me rends sur localhost:5001/db, la connexion fonctionne.