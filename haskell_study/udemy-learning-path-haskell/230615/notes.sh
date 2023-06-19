# https://www.udemy.com/course/learning-path-haskell-functional-programming-and-haskell/learn/lecture/6898588#overview

# https://docs.haskellstack.org/en/stable/#how-to-install-stack
curl -sSL https://get.haskellstack.org/ | sh
# source ~/.bashrc

which stack

stack --version

mkdir 01_install
cd 01_install

stack new hello-world simple --resolver=lts-7.8

cd hello-world

stack setup 

stack build

stack exec hello-world

# compile just one file
stack ghc -- -o main src/Main.hs
./main

stack runghc src/Main.hs

# ------------------------------------------------------------
mkdir 03
cd 03



















