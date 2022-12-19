for module_name in "$@"
do
    rm "$module_name".c
    rm "$module_name".o
    rm main
done