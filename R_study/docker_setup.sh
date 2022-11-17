

apt update
apt install git build-essential python3 python3-pip -y

pip3 install jupyter

# enable jupyter extension in container
# https://www.youtube.com/watch?v=_10avr-dOSE&t=280s&ab_channel=1littlecoder
# take a look at the video above to setup the R with jupyter

# inside R shell we need to install
install.packages("IRkernel")
# then we need to call the package
IRkernel::installspec()

# for the step above we need to have jupyter installed...
# for that we need python
# and then
pip3 install jupyter
# and for vscode connected to the container
# we need to have the jupyter extension activated


