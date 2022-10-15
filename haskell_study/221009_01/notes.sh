# https://www.udemy.com/course/learning-path-haskell-functional-programming-and-haskell/learn/lecture/6898588#overview

# https://docs.haskellstack.org/en/stable/#how-to-install-stack
# 
curl -sSL https://get.haskellstack.org/ | sh

which stack
# /usr/local/bin/stack

stack --version
# Version 2.9.1, Git revision 409d56031b4240221d656db09b2ba476fe6bb5b1 x86_64 hpack-0.35.0

stack new hello-world simple --resolver=lts-7.8
# Downloading template "simple" to create project "hello-world" in hello-world/ ...
                                                                
# The following parameters were needed by the template but not provided: author-email, author-name, category, copyright, github-username
# You can provide them in /root/.stack/config.yaml, like this:
# templates:
#   params:
#     author-email: value
#     author-name: value
#     category: value
#     copyright: value
#     github-username: value
# Or you can pass each one as parameters like this:
# stack new hello-world simple -p "author-email:value" -p "author-name:value" -p "category:value" -p "copyright:value" -p "github-username:value"

# Looking for .cabal or package.yaml files to use to init the project.
# Using cabal packages:                                           
# - hello-world/                                                  

# Selected resolver: lts-7.8                                      
# Initialising configuration using resolver: lts-7.8              
# Total number of user packages considered: 1                     
# Writing configuration to file: hello-world/stack.yaml           
# All done.                                                       
# /root/.stack/templates/simple.hsfiles:    5.75 KiB downloaded...

cd hello-world

stack setup 

stack build

stack exec hello-world

