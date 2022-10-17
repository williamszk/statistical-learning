

# https://www.kaggle.com/datasets/yasserh/walmart-dataset


mkdir original-data
touch .gitignore
touch original-data/.gitkeep

python3 -m venv .venv

pip3 install jupyter pandas

# for convinience let's set 1 week equivalent to 1 minute
# so every minute the client will send the data of the week

mkdir client
# the client will be a typescript code base
cd client
npm init -y

# why shouldn't we use java? or any other language actually
# how to build a client using typescript?

# how to open csv using typescript?
# https://blog.tericcabrel.com/read-csv-node-typescript/
mkdir client/src
touch client/main.ts

# how to setup a typescript project?
# https://www.digitalocean.com/community/tutorials/typescript-new-project

npm i typescript --save-dev

# to initialize a typescript project
npx tsc --init

npx tsc

# set typescript compiler in watch mode
npx tsc -w

npm i csv-parse
npm i @types/node

# not sure if I need this one here
# npm i @types/csv-parse

# we could take a look at the package documentation
# https://www.npmjs.com/package/csv-parse

# I wanted to read just a few lines of the csv file
# But for now the way that this is working will suffice 
# then I need to take each line of the csv and send the object through an
# http request
# Search for how to make requests with typescript