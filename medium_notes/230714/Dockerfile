# src/Dockerfile
from python:3.11.4-bullseye
RUN apt-get update && apt-get install vim -y

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .

CMD python3 app.py

# -----------------------------------------------------------------------------

# src/Dockerfile
FROM node:16-alpine AS builder

USER node
RUN mkdir /home/node/app
WORKDIR /home/node/app

COPY --chown=node:node ./package.json ./
RUN npm install

COPY --chown=node:node ./ ./

RUN npm run build
# /home/node/app/build <-- all the stuff we care about

FROM nginx
COPY --from=builder /home/node/app/build /usr/share/nginx/html

# -----------------------------------------------------------------------------
# src/Dockerfile.base
FROM ubuntu
RUN apt-get update && \
    apt-get install -y && \
    upgrade && \
    python3 && \
    python3-pip && \
    libcurl4-openssl-dev && \
    libssl-dev && \
    build-essential && \
    libzip-dev && \
    libzip4 && \
    sqlite3

COPY requirements.txt .
RUN pip install -r requirements.txt 

# -----------------------------------------------------------------------------
# src/Dockerfile
FROM base-python-image

COPY . .
CMD python3 app.py

# -----------------------------------------------------------------------------
# Original Dockerfile
# src/Dockerfile
FROM ubuntu
RUN apt-get update && \
    apt-get install -y && \
    python3 && \
    python3-pip && \
    libcurl4-openssl-dev && \
    libssl-dev && \
    build-essential && \
    libzip-dev && \
    libzip4 && \
    sqlite3

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .

CMD python3 app.py

# -----------------------------------------------------------------------------



