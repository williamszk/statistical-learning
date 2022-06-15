
# notes based on:
# https://valgrind.org/docs/manual/ms-manual.html


gcc -g prog.c -o prog.out

valgrind --tool=massif prog

# bash: valgrind: command not found
apt update
apt install valgrind -y


valgrind --tool=massif ./prog.out

ms_print massif.out.782525

ms_print massif.out.782525 --time-unit=B


