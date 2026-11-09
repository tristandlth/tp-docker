# TP Docker

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
