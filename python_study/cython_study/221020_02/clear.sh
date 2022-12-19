for module_name in "$@"
do
    echo "$module_name"
    rm python_modules/"$module_name".c
    rm python_modules/"$module_name".cpython-39-x86_64-linux-gnu.so
    rm "$module_name".cpython-39-x86_64-linux-gnu.so
    rm -rf python_modules/build
done