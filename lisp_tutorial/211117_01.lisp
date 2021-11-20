; https://www.youtube.com/watch?v=3GEAINRCbJ4&ab_channel=NeilMunro  
; just a simple tutorial and hello world using common lisp
; to use common lisp we use the command in the terminal: 
; sbcl
; which stands for stell bank common lisp compiler    
(print "Hello World, also!")


(format t "Hello World!~%")
; ~% => I think it is a line drop
; we do not use \n for new line, this notation came later

; ~A is the interpolation character 

(format t "Hello, ~A!~%" "Neil")

(format t "Hello, ~A ~A ~A!~%" "Neil" ""Tyson")



