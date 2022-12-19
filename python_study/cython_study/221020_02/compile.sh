
cd python_modules
python setup.py build_ext --inplace
cd ..

# How many arguments were passed to the bash script
# echo $#

for module_name in "$@"
do
    echo "$module_name"
    cp python_modules/"$module_name".cpython-39-x86_64-linux-gnu.so ./"$module_name".cpython-39-x86_64-linux-gnu.so
done

# i=1
# echo $($i)
# while [ -z $(( $i ))  ]
# do
#     echo $(( $i ))

#     i=$(( $i + 1 ))
# done

# echo $1
# echo $2

# cp python_modules/integrate1.cpython-39-x86_64-linux-gnu.so ./integrate1.cpython-39-x86_64-linux-gnu.so