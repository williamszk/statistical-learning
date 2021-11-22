#!/usr/bin/sbcl --script

(+ 9 8)

(- 5 4)

(* 5 4)

(/ 5 4)

(/ 5 4.0)
; remainder and mod do the same thing
(rem 10 4)

(mod 5 4)

(defvar *var* (mod 5 4))
(format t "~d ~%" *var*)