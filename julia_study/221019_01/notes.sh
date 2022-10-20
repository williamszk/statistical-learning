# setting up julia again in an ubuntu
# https://medium.com/coffee-in-a-klein-bottle/install-julia-1-5-on-ubuntu-bb8be4b2571d

apt install julia

# https://julialang.org/downloads/


curl -LO https://julialang-s3.julialang.org/bin/linux/x64/1.8/julia-1.8.2-linux-x86_64.tar.gz

# inside the 221019_01 directory
touch .gitignore

tar -xvzf julia-1.8.2-linux-x86_64.tar.gz

# You now have a folder with all the Julia files. 
# No installation is required. Now, we move this folder 
# to “/opt” (this is not strictly necessary, you can use 
# any other location in your machine).
mv julia-1.8.2/ /opt/

# Finally, create a symbolic link to the Julia binary file. 
# This will allow you to run the command “julia” in your terminal 
# and start the Julia REPL.
ln -s /opt/julia-1.8.2/bin/julia /usr/local/bin/julia


# 3. Adding Julia kernel to Jupyter
# in terminal
julia

using Pkg
Pkg.add("IJulia")

using IJulia
installkernel("Julia")

