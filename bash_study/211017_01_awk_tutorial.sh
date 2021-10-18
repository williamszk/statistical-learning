# https://www.youtube.com/watch?v=9YOZmI-zWok&t=6s&ab_channel=DistroTube

# text processing utility

ps

# print the first column
ps | awk '{print $1}'

# put a 0 to mean print everything
ps | awk '{print $0}'

# print the second column
ps | awk '{print $2}'

# spaces are columns in awk
# for bash there is only text

# print everything in /etc/passwd
awk '{print $0}' /etc/passwd

cat /etc/passwd

awk -F ":" '{print $1}' /etc/passwd
# -F means is used to change the separtor in awk
# the code above list all the users

# I want to print columsn 1, 6 and 7
awk -F ":" '{print $1 $6 $7}' /etc/passwd

# to separte the columns with a space we can write the following:
awk -F ":" '{print $1" "$6" "$7}' /etc/passwd

# better than space is a tab
awk -F ":" '{print $1"\t\t"$6"\t\t"$7}' /etc/passwd

# treat field separtors are ":"
# but in the output, the field separtor is "-"
awk 'BEGIN{FS=":"; OFS="-"} {print $1,$6,$7}' /etc/passwd

awk 'BEGIN{FS=":"; OFS="\t\t\t\t\t"} {print $1,$6,$7}' /etc/passwd

# list all the shells in the system
cat /etc/shells

awk -F "/" '{print $0}' /etc/shells
awk -F "/" '{print $3}' /etc/shells
awk -F "/" '{print $4}' /etc/shells

awk 'BEGIN{FS="/"; OFS="\t"} {print $0}' /etc/shells

awk -F "/" '/^\// {print $NF}' /etc/shells
# NF means the last field, that is the last column of each line
# the notation for /^\// means /  / are separtors 
# ^\/ = ^ means in the beginning of the line
# \/ means the value /, where \ is the escape character

awk -F "/" '{print $NF}' /etc/shells

# some of the output is duplicate
# so we can pipe the output to the command uniq
awk -F "/" '{print $NF}' /etc/shells | uniq

# use sort to make the alphabetical order
awk -F "/" '{print $NF}' /etc/shells | uniq | sort

# show cisk usage or disk free
df | awk '/\/dev/ {print $0}' 
# /  / start the search

df | awk 'BEGIN{FS="\t"; OFS="-"} /\/dev/ {print $1,$NF}'

df | awk '/\/dev/ {print $1"\t"$2"\t"$3}'
df -h
df -h | awk '/\/dev/ {print $1"\t"$2"\t"$3"\t"$4}'
df -h | awk '/\/dev/ {print $1"\t"$3 + $4}'
df -h | awk '/^\/dev/ {print $1"\t"$3 + $4}'


# find lines that have more than 7 characters
awk 'length($0) > 7' /etc/shells
awk 'length($0) > 12' /etc/shells
awk 'length($0) < 10' /etc/shells

# list all process that are running in the machine
ps -ef

# how to filter process using awk
ps -ef | awk '{ if($NF == "/bin/bash") print $0}'
ps -ef | awk '{ if($NF == "/usr/bin/bash") print $0}'

ps -ef | grep "/usr/bin/bash"

# we can make calculations with awk, and write some programming
awk 'BEGIN { for(i=1; i<=10; i++) print "The square rooot of", i, "is", i*i; }'

# search characters inside a file
awk '$1 ~ /^[b,c]/ {print $0}' ~/.bashrc
# search inside  ~/.bashrc if the first column
# starts with characters b or c and print the whole line




