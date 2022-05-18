# https://www.youtube.com/watch?v=WeTesTCzep0&ab_channel=dotNetVi%E1%BB%87tNamOfficial


# how to install c# .net core into the container


# I don't have wget
apt update
apt install wget -y 

cd
# https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu#2004
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb

apt-get update;
apt-get install -y apt-transport-https
apt-get update
apt-get install -y dotnet-sdk-6.0

apt-get update
apt-get install -y apt-transport-https
apt-get update
apt-get install -y aspnetcore-runtime-6.0

# finish installation I think
# https://docs.microsoft.com/en-us/dotnet/core/install/linux-ubuntu#2004

# now dotnet should be installed

#
dotnet --version
# 6.0.300

dotnet new
# Common templates are:
# Template Name         Short Name    Language    Tags               
# --------------------  ------------  ----------  -------------------
# ASP.NET Core Web App  webapp,razor  [C#]        Web/MVC/Razor Pages
# Blazor Server App     blazorserver  [C#]        Web/Blazor         
# Class Library         classlib      [C#],F#,VB  Common/Library     
# Console App           console       [C#],F#,VB  Common/Console     

# let's create a class library
# dotnet new classlib

# actually let's install a console app
dotnet new console

# this resolve some dependencies
dotnet restore 

# to run the program
dotnet run
# Hello, World!


