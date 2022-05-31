# how to import protofile?

# protoc, protobuf compiler

# we need to download the protoc for the specific operating system
# https://github.com/protocolbuffers/protobuf/releases

# protoc-21.1-linux-x86_64.zip
# for now I downloaded this
# given that I am in a container I should use the terminal to download
# https://github.com/protocolbuffers/protobuf/releases/download/v21.1/protoc-21.1-linux-x86_64.zip

# we download the protoc into the directory's project
# but we need to set the gitignore to not commit the protoc 
# protoc-21.1-linux-x86_64.zip
# I need to unzip the zip file

# tar 
# apt install unzip -y
# unzip 
# unzip "protoc-21.1-linux-x86_64.zip"
# the unziping is not working...

# let's try using tar
tar -xvf protoc-21.1-linux-x86_64.zip

# let's try to download the file again
curl -O -L "https://github.com/protocolbuffers/protobuf/releases/download/v21.1/protoc-21.1-linux-x86_64.zip"
# I needed to include the -L flag
# Follow a 301-redirected file while downloading file with curl, run
# It seems that this is a redirected file... I'm not pretty sure what that is.

# Now I think I can use unzip
unzip "protoc-21.1-linux-x86_64.zip" -d ./protoc-21.1-linux-x86_64

# we can access the compiler, protoc
./protoc-21.1-linux-x86_64/bin/protoc

# to run the protoc in our proto file for javascript
./protoc-21.1-linux-x86_64/bin/protoc --js_out=import_style=commonjs,binary:. employees.proto
# I had problem using the command above


npm install google-protobuf
# this didn't work

./protoc-21.1-linux-x86_64/bin/protoc

protobuf-all-21.1.tar.gz

curl -O -L https://github.com/protocolbuffers/protobuf/releases/download/v21.1/protobuf-all-21.1.tar.gz
# unzip "protobuf-all-21.1.tar.gz" -d ./protobuf-all-21.1 # this does not work
tar -xvf protobuf-all-21.1.tar.gz

protobuf-3.21.1/bin/protoc



# try this link instead to see if js is inside of it...
curl -O -L https://github.com/protocolbuffers/protobuf/releases/download/v3.19.4/protoc-3.19.4-linux-x86_64.zip
unzip "protoc-3.19.4-linux-x86_64.zip" -d ./protoc-3.19.4-linux-x86_64 

protoc-3.19.4-linux-x86_64/bin/protoc

# ============================================================== #

./protoc-3.19.4-linux-x86_64/bin/protoc --js_out=import_style=commonjs,binary:. employees.proto
# this works


# this is used by node to use protobuf
npm install google-protobuf


