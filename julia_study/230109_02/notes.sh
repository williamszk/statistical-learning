curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.4-linux-x86_64.tar.gz

tar -xvf julia-1.8.4-linux-x86_64.tar.gz

mv julia-1.8.4/ /opt/
rm julia-1.8.4-linux-x86_64.tar.gz

ln -s /opt/julia-1.8.4/bin/julia /usr/local/bin/julia

# inside julia
julia
using Pkg
Pkg.add("IJulia")

using IJulia
installkernel("Julia")



curl -L -O -v https://www.kaggle.com/datasets/ninzaami/loan-predication/download?datasetVersionNumber=1
curl -LO https://www.kaggle.com/datasets/ninzaami/loan-predication/download

https://www.kaggle.com/datasets/ninzaami/loan-predication/download?datasetVersionNumber=1

unzip archive.zip


# =============================================================================== 
# I need to install matplotlib in the base environment because julia will 
# use pyplot
apt update
apt upgrade
apt install python3-pip
pip3 install matplotlib


