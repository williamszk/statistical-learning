for module_name in "$@"
do
    cython --embed -o "$module_name".c "$module_name".py
    # gcc -c -fPIC "$module_name".c -o "$module_name".o -I/usr/include/python3.9/ \
    #     -L/usr/lib/x86_64-linux-gnu/ -lpython3.9.so
done
# /usr/include/python3.9/Python.h


for module_name in "$@"
do
    module_with_c="$module_name".c
    c_files=$c_files" $module_with_c"
done
echo ">>>>>>>>>> $c_files"

gcc -fPIC  $c_files -I/usr/include/python3.9/ -L/usr/lib/x86_64-linux-gnu/ -lpython3.9 -o main


# ./usr/lib/x86_64-linux-gnu/libpython3.9.so