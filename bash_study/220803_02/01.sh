#!/bin/bash

# https://www.youtube.com/watch?v=7qd5sqazD7k&ab_channel=NetworkChuck

# variable
name="Random User"

# read will get some use input
echo "What is your name?"
read name

# $1 is an alias for the first argument
name=$1

echo "Good morning $name"
sleep 1
echo "You are looking good $name"
sleep 1
echo "You have the best beer $name"
sleep 1
echo "Finish"
sleep 0.5
# include information of 
# whoami
# pwd
# date

echo "I am the $(whoami)"
sleep 1
echo "We are running inside $(pwd)"
sleep 1
echo "Now is: $(date)"


# chmod +x 01.sh
