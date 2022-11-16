
# notes based on:
# https://asecuritysite.com/hash/goshake

go mod init example.com/main
touch .gitignore
echo "main" >> .gitignore
touch main.go

go get "golang.org/x/crypto/sha3"
