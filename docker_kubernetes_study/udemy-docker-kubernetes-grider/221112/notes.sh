
https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11437044#overview

# check if node is installed
node -v
# v16.17.0

npm init -y
npx create-react-app frontend

npm run start # development server
npm run test  # running tests
npm run build # for deployment

cd frontend
touch Dockerfile

docker build -t william/my-study-image -f Dockerfile.dev .

# without volumes
# docker run -d -p 3000:3000 --name my-docker-image william/my-study-image

# with volumes
docker run -d \
    -p 3000:3000 \
    -v $(pwd):/app \
    -v /app/node_modules \
    --name my-docker-image \
    william/my-study-image

# bookmarking volumes
# we write -v /app/node_modules because there is no 
# node_modules in the host machine, so we need to tell docker
# to not try to use a node_modules of the host machine and keep the
# one that is inside the container, for that we just don't write a :

docker stop my-docker-image
docker rm my-docker-image


touch docker-compose.yml
docker-compose up
docker-compose ls

# next video:
# https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/learn/lecture/11437078#overview
