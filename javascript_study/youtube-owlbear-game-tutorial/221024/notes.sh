# https://www.youtube.com/watch?v=eYTnoJluds0&ab_channel=Frankslaboratory

apt install npm
npm i n -g

npm init -y

npm i typescript --save-dev

# start typescript project
npx tsc --init
# Created a new tsconfig.json with:                                                                                       
#                                                                                                                      TS 
#   target: es2016
#   module: commonjs
#   strict: true
#   esModuleInterop: true
#   skipLibCheck: true
#   forceConsistentCasingInFileNames: true

touch script.ts

tsc

touch style.css
