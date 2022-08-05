FROM node:14-alpine

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password

RUN mkdir -p /home/app

COPY ./app /home/node-app

WORKDIR /home/node-app

RUN npm install

CMD ["node", "server.js"]
