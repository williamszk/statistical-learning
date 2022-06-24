
# notes based on:
# https://valgrind.org/docs/manual/ms-manual.html


gcc -g prog.c -o prog.out

# valgrind --tool=massif prog

# bash: valgrind: command not found
apt update
apt install valgrind -y

# ======================================== #

gcc -g prog.c -o prog.out

valgrind --tool=massif ./prog.out --log-file="valgrind_output.out"
# valgrind --leak-check=yes myprog arg1 arg2
valgrind  --leak-check=yes ./prog.out 

ms_print massif.out.782525

ms_print massif.out.782525 --time-unit=B



gcc -g prog2.c -o prog2.out
valgrind  --leak-check=yes ./prog2.out 