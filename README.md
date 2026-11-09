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
