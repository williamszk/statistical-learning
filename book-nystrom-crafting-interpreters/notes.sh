

mkdir 230711
cd 230711

# how to install java
# curl -LO https://corretto.aws/downloads/latest/amazon-corretto-17-x64-linux-jdk.tar.gz
# sudo tar -C $HOME -xzf amazon-corretto-17-x64-linux-jdk.tar.gz
# echo "export JAVA_HOME=$HOME/amazon-corretto-17.0.5.8.1-linux-x64" >> ~/.bashrc
# source .bashrc 
# echo "export PATH=$PATH:$JAVA_HOME/bin" >> ~/.bashrc
# source .bashrc
# java --version

# remove all .class files
find . -type f -name "*.class" -delete

cd 230711/src
javac com/proj/Main.java
java com.proj.Main







