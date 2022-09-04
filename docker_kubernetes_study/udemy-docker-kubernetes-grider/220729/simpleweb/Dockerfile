# Specify a base image
FROM node:14-alpine

WORKDIR /usr/app

# to avoid making the npm install every time we make a change
# to the source code
COPY ./package.json ./

# Install dependencies
RUN npm install

COPY ./ ./

# Default command
CMD ["npm", "start"]