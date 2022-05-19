# Some study notes about `ar` in Linux

Study notes based on:

https://www.howtogeek.com/427086/how-to-use-linuxs-ar-command-to-create-static-libraries/

archive files

`tar` is used instead of `ar`

`ar` is used to create static libraries

how to create static libraries

"Files which contain programming instructions are called **source code files**."

`libcipher.a`  will contain all files of `library` directory

`libcipher.a` will contain the compiled versions of these two **source code files**.

We’ll also create a short text file called `libcipher.h`.

`libcipher.h` is a header file containing the definitions of the two functions in our new library.

Anyone with the library and the header file will be able to use the two functions in their own programs. 

They do not need to re-invent the wheel and re-write the functions; they simply make use of the copies in our library.


We need to compile 

- `cipher_encode.c`
- `cipher_decode.c`

But we'll use the `-c` flag from `gcc`. This will compile the code but not make an executable.

We just want the binaries.

`cd library`

`gcc -c cipher_encode.c`

`gcc -c cipher_decode.c`

This command will just create the respective:

- `cipher_encode.o`
- `cipher_decode.o`

The object files.

We can create the **library file**, which is **archive file** with extension `.a`.

We use the `ar` command.

- `-c` : create the library file.
- `-r` : add with replace to files to **library file**
- `-s` : index, create an index of the files inside the library file

The name of the libfile is going to be `libcipher.a`

`ar -crs libcipher.a cipher_encode.o cipher_decode.o`

- `-t` will show a table inside the libfile

`ar -t libcipher.a`

The above sniped will show all object `.o` files inside the libfile

To be able to use the `libcipher.a` we also need a header file that will indicate the functions defined in the libfile. We will calll it `libcipher.h`.

We need to test the libfile. 

Copy all files related to the libcipher to the `test` directory

`cp libcipher.* ./test`

`cd test`

We need to compile `test.c` linking the libfile `.a`

`gcc test.c libcipher.a -o test.out`

`./test`

cd ..

gcc -c cipher_version.c

Run ar

-v verbose

The previous command:
`ar -crs libcipher.a cipher_encode.o cipher_decode.o`


The command that we want to run:
`ar -rsv libcipher.a cipher_version.o`

There is no -c flag, it means that we are not creating a new file.
And we only include the new cipher_version.o file.

ar -t libcipher.a

rm ./test/libcipher.*

cp libcipher.* ./test

cd test

gcc test.c libcipher.a -o test.out

./test.out

cd ..

gcc -c cipher_version.c

 This will just replace the with `cipher_version.o`

ar -rsv libcipher.a cipher_version.o

cp libcipher.* ./test

cd test

gcc test.c libcipher.a -o test.out

./test.out

We don't want the cipher_version.o anymore in the libfile

From the ar command:

-d : delete
-v : verbose
-s : update index

ar -dsv libcipher.a cipher_version.o

ar -t libcipher.a

We need to delete the definitions of the functions in the header file.



https://stackoverflow.com/a/9810368/15875971

`.a` are also called archive libraries, archive files or lib files.

`.so` is the shared object

They are linked during run time. .so files don't need to be compiled together with the 
other files.








# Next Steps:

After this tutorial maybe we can understand some of the code inside of:

https://opensource.com/article/20/6/linux-libraries


http://www.yolinux.com/TUTORIALS/LibraryArchives-StaticAndDynamic.html