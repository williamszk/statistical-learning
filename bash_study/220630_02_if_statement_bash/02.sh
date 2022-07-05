#! /bin/bash

if [ "$EDITOR" = "" ]; then
    echo "No default editor is set"
    EDITOR=vim
fi

# how to set to nothing the EDITOR variable
unset EDITOR


# using -z will do the same thing
if [ -z "$EDITOR" ]; then
    echo "No default editor is set"
    EDITOR=vim
fi

unset EDITOR

# ============================ 
# using just one line to do the same if statement
[ -z "$EDITOR" ] && EDITOR=vim

unset EDITOR

