
create-react-app frontend


npm run start
npm run test 
npm run build 

docker build .
docker build -f Dockerfile.dev .

# without deleting the node_modules
    # Sending build context to Docker daemon  304.5MB
    # Step 1/6 : FROM node:16-alpine
    # 16-alpine: Pulling from library/node
    # 213ec9aee27d: Pull complete 
    # 864b973d1bf1: Pull complete 
    # 80fe61ad56f5: Pull complete 
    # e3887ab559e6: Pull complete 
    # Digest: sha256:2c405ed42fc0fd6aacbe5730042640450e5ec030bada7617beac88f742b6997b
    # Status: Downloaded newer image for node:16-alpine
    #  ---> 5dcd1f6157bd
    # Step 2/6 : WORKDIR '/app'
    #  ---> Running in 251191e5836b
    # Removing intermediate container 251191e5836b
    #  ---> 0f3e8977ff13
    # Step 3/6 : COPY package.json .
    #  ---> f479b171e952
    # Step 4/6 : RUN npm install
    #  ---> Running in abd9afca2da3
    # npm WARN deprecated stable@0.1.8: Modern JS already guarantees Array#sort() is a stable sort, so this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
    # npm WARN deprecated svgo@1.3.2: This SVGO version is no longer supported. Upgrade to v2.x.x.

    # added 1373 packages, and audited 1374 packages in 2m

    # 207 packages are looking for funding
    #   run `npm fund` for details

    # 6 high severity vulnerabilities

    # To address all issues (including breaking changes), run:
    #   npm audit fix --force

    # Run `npm audit` for details.
    # npm notice 
    # npm notice New minor version of npm available! 8.15.0 -> 8.18.0
    # npm notice Changelog: <https://github.com/npm/cli/releases/tag/v8.18.0>
    # npm notice Run `npm install -g npm@8.18.0` to update!
    # npm notice 
    # Removing intermediate container abd9afca2da3
    #  ---> dcf8fab30d56
    # Step 5/6 : COPY . .
    #  ---> 33c49a9c1178
    # Step 6/6 : CMD ["npm", "run", "start"]
    #  ---> Running in 16d0686e1092
    # Removing intermediate container 16d0686e1092
    #  ---> 38db21dc2e0b
    # Successfully built 38db21dc2e0b


# When deleting the node_modules
    # Sending build context to Docker daemon  2.227MB
    # Step 1/6 : FROM node:16-alpine
    #  ---> 5dcd1f6157bd
    # Step 2/6 : WORKDIR '/app'
    #  ---> Using cache
    #  ---> 0f3e8977ff13
    # Step 3/6 : COPY package.json .
    #  ---> Using cache
    #  ---> f479b171e952
    # Step 4/6 : RUN npm install
    #  ---> Using cache
    #  ---> dcf8fab30d56
    # Step 5/6 : COPY . .
    #  ---> 57bae0e485db
    # Step 6/6 : CMD ["npm", "run", "start"]
    #  ---> Running in 8690faf030a3
    # Removing intermediate container 8690faf030a3
    #  ---> 8dd1c8abff90
    # Successfully built 8dd1c8abff90

# william@william-300E5M-300E5L:~/Documents/220820_01/frontend$ docker build -f Dockerfile.dev .
# Sending build context to Docker daemon  2.227MB
# Step 1/6 : FROM node:16-alpine
#  ---> 5dcd1f6157bd
# Step 2/6 : WORKDIR '/app'
#  ---> Running in 66dab4b132ad
# Removing intermediate container 66dab4b132ad
#  ---> 4a1330d9056d
# Step 3/6 : COPY package.json .
#  ---> f48a597f7874
# Step 4/6 : RUN npm install
#  ---> Running in 127972cbe9b9
# npm WARN deprecated stable@0.1.8: Modern JS already guarantees Array#sort() is a stable sort, so this library is deprecated. See the compatibility table on MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#browser_compatibility
# npm WARN deprecated svgo@1.3.2: This SVGO version is no longer supported. Upgrade to v2.x.x.

# added 1373 packages, and audited 1374 packages in 2m

# 207 packages are looking for funding
#   run `npm fund` for details

# 6 high severity vulnerabilities

# To address all issues (including breaking changes), run:
#   npm audit fix --force

# Run `npm audit` for details.
# npm notice 
# npm notice New minor version of npm available! 8.15.0 -> 8.18.0
# npm notice Changelog: <https://github.com/npm/cli/releases/tag/v8.18.0>
# npm notice Run `npm install -g npm@8.18.0` to update!
# npm notice 
# Removing intermediate container 127972cbe9b9
#  ---> fd4c1a2d75ea
# Step 5/6 : COPY . .
#  ---> 4477324ccff6
# Step 6/6 : CMD ["npm", "run", "start"]
#  ---> Running in 18f96cc47332
# Removing intermediate container 18f96cc47332
#  ---> 5df29da78516
# Successfully built 5df29da78516


docker build -t my-react-image -f Dockerfile.dev .

# docker run my-react-image
# docker run -p 3000:3000 my-react-image
docker run -d --name my-react-container  -p 3000:3000 my-react-image 

docker logs my-react-container
docker stop my-react-container
docker rm my-react-container

# ===========================================================

docker run -d \
    --name my-react-container \
    -p 3000:3000 \
    -v /app/node_modules \
    -v $(pwd):/app \
    my-react-image 

# we need to include -v /app/node_modules 
# because we don't want the next command -v $(pwd):/app
# to overwrite the node_modules inside the container
# with a blank directory

docker logs my-react-container
docker stop my-react-container
docker rm my-react-container

# Create a docker-compose file to encode the command for creating
# the my-react-container

touch docker-compose.yaml

docker-compose up -d --build
docker-compose up -d

docker-compose stop
docker-compose start

















