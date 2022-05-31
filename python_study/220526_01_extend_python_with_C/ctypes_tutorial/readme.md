

https://www.youtube.com/watch?v=p_LUzwylf-Y&ab_channel=C%2FC%2B%2BDublinUserGroup


fPIC: Position Independent Code
```
gcc -c -fPIC basic.c -o basic.o
gcc basic.o -shared -o libbasic.so
```

To do in one step:
```
gcc -shared -o libbasic.so -fPIC basic.c
```