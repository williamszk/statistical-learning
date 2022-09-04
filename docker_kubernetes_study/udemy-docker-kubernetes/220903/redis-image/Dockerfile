# Use an existing docker image
FROM alpine



# download and install a dependency
RUN apk add --update redis



# thell the image what to do when it starts
CMD ["redis-server"]
# those commands are called Dockerfile instructions
# FROM, RUN, CMD
# for each instruction we provide the argument for the instruction
# in FROM alpine
# the instruction FROM needs a base image to pull from, which
# in our case the argument is "alpine"







