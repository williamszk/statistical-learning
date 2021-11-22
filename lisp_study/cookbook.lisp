;;;; 

;;; hello this is a comment


;;;(print "Hello World!")

(print "Hello World!")

; (format t "Hello world ~%")

(format t "What is your name ~%")

; lisp is not case sensitive

(defvar *name* (read))

(defun hello-you (name)
    (format t "Hello ~a! ~%" name)
)

; to capitalize jus the first letter of the input
; the default is to capitalize everything
(setq *print-case* :capitalize)

(hello-you *name*)

; ------------------------------------------------

(+ 5 4)

(+ 5 (- 4 - 2))

; ------------------------------------------------

(format t "Hi, what is your name? ~%")

(defvar name (read))

(defun greeting-name (name)
    (format t "Hello, ~a. Welcome back!~%" name)
)

; ------------------------------------------------
; concells
; consecutive cells

; ------------------------------------------------
(defvar *number* 6)

(format t "*number* = ~a ~%" *number*)

(setf *number* 0)

; (print *number*)
(format t "*number* = ~a ~%" *number*)
; ------------------------------------------------
(format t "Number with commas ~:d ~%" 10000000)

(format t "PI to 5 characters ~5f ~%" 3.141593)

(format t "PI to 4 decimals ~,4f ~%" 3.141593)

(format t "10 Percent ~,,2f % ~%" .10)

(format t "10 Dollars ~$ ~%" 10)
; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

; ------------------------------------------------

