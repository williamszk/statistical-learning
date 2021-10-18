# https://www.cyberciti.biz/faq/bash-for-loop/

for i in 1 2 3 4 5
do
    echo "Welcome $i times"
done

# we can include range {1..5}
for i in {1..5}
do 
    echo "Welcome $i times"
done

# you can set steps in range too
echo "Bash version ${BASH_VERSION}"
for i in {0..10..2}
do
    echo "Welcome $i times"
done

# C-like for loop syntax
# three-expression for loop
for (( c=1; c<=5; c++))
do
    echo "Welcome $c times"
done

# infinite loops in bash
for (( ; ; ))
do
    echo "infinite loops [ hit CTRL+C to stop]"
done

# break out the for loop
# ls /etc/*
for file in /etc/*
do
    if [ "${file}" == "/etc/resolv.conf" ]
    then
        countNamesservers=$(grep -c nameserver /etc/resolv.conf)
        echo "Total ${countNamesservers} nameservers defined in ${file}"
        break
    fi
done

# continue statement for for-loops
FILES="$@"
for f in $FILES
do
    echo "Skipping $f"
done

FILES="$@"
echo "$FILES"
FILES="a.out"
for f in $FILES
do
    if [ -f ${f}.bak ]
    then 
        echo "Skiping $f file..."
    fi

    /bin/cp $f $f.bak
done

# for loop with array elements
DB_AWS_ZONE=("us-east-2a" "us-west-1a" "eu-central-1a")
# above is an example of array
echo "${DB_AWS_ZONE[@]}"
for zone in "${DB_AWS_ZONE[@]}"
do
    echo "Creating RDS (DB) server in $zone, please wait ..."
    # I will not run the code below because it will create databases
    # that I don't need
    :'
    aws rds create-db-instance \
    --availability-zone "$zone" \
    --allocate-storage 20 --db-instance-class db.m1.small \
    --db-instance-identifier test-instance \
    --engine mariadb \
    --master-username $my_username \
    --master-user-password $my_password_here \
    '
done

# Loop witha a shell variable
_admin_ip="202.54.1.33|MUM_VPN_GATEWAY 23.1.2.3|DEL_VPN_GATEWAY 13.1.2.3|SG_VPN_GATEWAY"
echo $_admin_ip





