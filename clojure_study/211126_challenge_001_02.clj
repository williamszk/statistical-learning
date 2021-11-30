;; This is a cleaning from the script challenge_001.clj
;; here we organize and keep only the parts that are important to
;; solve the challenge

;; Chosen programming language:  Clojure
;; Chosen challenge platform:  reddit_dailyprogrammer
;; Chosen challenge id:  31


;; The easy one:
;; Write a function that takes two base-26 numbers in which digits are represented by 
;; letters with A=0, B=1, … Z=25 and returns their product using the same notation. As an example, CSGHJ × CBA = FNEUZJA.
;; Your task is to write the base-26 multiplication function.
;; Try to be very efficient in your code!


;; CSGHJ * CBA = FNEUZJA

;; how to open Clojure REPL in terminal
;; To start the Clojure REPL use the command below in the terminal:
;; $ /usr/local/bin/clj


;; VScode
;; to include the shortcut to send code to the terminal
;; Run Selected Text in Active Terminal


;; /usr/local/bin/clj


;; the hash-map to be used to convert chars to numbers
(def map-translator-str
  {"A" 0
   "B" 1
   "C" 2
   "D" 3
   "E" 4
   "F" 5
   "G" 6
   "H" 7
   "I" 8
   "J" 9
   "K" 10
   "L" 11
   "M" 12
   "N" 13
   "O" 14
   "P" 15
   "Q" 16
   "R" 17
   "S" 18
   "T" 19
   "U" 20
   "V" 21
   "W" 22
   "X" 23
   "Y" 24
   "Z" 25})

;; convert a letter for example "AB" to a list: ("A" "B")
(defn convert-twentysix-to-listchar [string-twentysix]
  (map str (seq string-twentysix)))

;; (def my-char-number "AB")
;; (convert-twentysix-to-listchar my-char-number)

;; a function to just get the value when you supply the key
(defn get-number-map [key]
  (get map-translator-str key))

;; (get-number-map "B")
;; (get-number-map "H")
;; (get-number-map "A")
;; (map get-number-map ["C" "B"])

;; define a general exponetiation function
(defn exp [x n]
  (if (zero? n) 1
      (* x (exp x (dec n)))))

;; set a more specific use for exponentiation
;; where the base is always 26
(defn exp26 [n]
  (exp 26 n))

;; (exp26 1)
;; (exp26 0)
;; (exp26 2)
;; (* 26 26)
;; (map exp26 [2 1 0])
;; (reduce + [676 26 1])
;; (reduce + (map exp26 [2 1 0]))
;; (reduce + 
;;   (map * 
;;     (map get-number-map ["C" "B"])
;;     (map exp26 [1 0])))

;; function to reverse a list: my-list
(defn reverse-list [my-list]
  (reduce conj '() my-list))
;; I don't know how this functions works...
;; But it works for reversing PersistentVector and PersistentList
;; Example:
;; (def my-list [1 2 3])
;; (reverse-list my-list)
;; how to verify types in clojure?
;; (type my-list)
;; clojure.lang.PersistentVector
;; What is difference between PersistentVector and lists in clojure?
;;
;; how to create a list in clojure
;; (list 1 2 3)
;; (type (list 1 2 3))
;; clojure.lang.PersistentList
;; What is the difference between PersistentVector and PersistentList in Clojure?
;; I think that a vector needs to have the same types of data inside it
;; but a list doesn't necessarily.
;;
;; 
(def my-list (list 1 2 3))
(type my-list)
(reverse-list my-list)

;; a function to make a reversed list
;; of a range
(defn reverse-range [n]
  (reverse-list (range n)))
;; (reverse-range 5)

;; How to get the length of a list in Clojure?
;; (def my-number-char ["C" "B"])
;; (count my-number-char)

;; (reduce + 
;;   (map * 
;;     (map get-number-map my-number-char)
;;     (map exp26 (reverse-range (count my-number-char)))))

;; function to convert a list of chars into a list of numbers
;; and make the sum to find the decimal number that is equivalent
(defn convert-charlist-decnumber [my-number-char]
  (reduce +
          (map *
               (map get-number-map my-number-char)
               (map exp26 (reverse-range (count my-number-char))))))

;; (def my-number-char ["C" "B"])
;; (convert-charlist-decnumber my-number-char)

;; (def my-number-char ["C" "B" "B"])
;; (convert-charlist-decnumber my-number-char)

;; (def my-number-char ["U"])
;; (convert-charlist-decnumber my-number-char)

;; (def my-number-char ["W" "H"])
;; (convert-charlist-decnumber my-number-char)

;; function that receives an string of as 26-based number
;; and finds the equivalent of this number in 10-based number
(defn convert-26based-to-10based-number [the-26based-number]
  (convert-charlist-decnumber
   (convert-twentysix-to-listchar the-26based-number)))
;; Examples 1
;; (def my-char-number "BA")
;; this should be 26
;; (convert-26based-to-10based-number my-char-number)
;; Examples 2
;; (def my-char-number "AA")
;; this should be 0
;; (convert-26based-to-10based-number my-char-number)
;; Examples 2
;; (def my-char-number "BAA")
;; this should be 676
;; (convert-26based-to-10based-number my-char-number)

;; we still need to create the function that can converts the decimal
;; number into a 26-based number
;; after doing this we can solve the problem

;; CSGHJ * CBA = FNEUZJA
;; (convert-26based-to-10based-number "CSGHJ")
;; (convert-26based-to-10based-number "CBA")

;; Function that converts a 1-based number into the 26-based number
(def my-10-based-number 676)
;; this needs to be "BAA"

;; maybe I dont need this...
;; create a list with the powers of 26
(map exp26 (reverse-range 3))
;; this list is used to verify in which category the 10-based number falls
;; if it is less than 26^2? or 26^3?
;; 

;; how to take the mathematical log in clojure?
(Math/log 10)
(Math/log 2.71828189)
;; this is log of base e, where e is the mathematical constant
;; we can change the base of the log, we can look at google to find out

;; build a function that finds the log of a number in base 26
(defn get-log-base26 [number]
  (/ (Math/log number) (Math/log 26)))
;; Example 1
;; this should give 2
;; (get-log-base26 676)
;; Example 2
;; (def number 676)
;; this should give 5
;; (get-log-base26 11881376)
;; Just a test
;; (get-log-base26 456)

;; The function above will be important to find the number of 26-base number 
;; slots the number will occupy

;; return the integer value of the log_26 from a number to know in which case the number is
(defn get-int-log-base26 [number]
  (int (get-log-base26 number)))
;; (get-log-base26 879)
;; gives: 2.0805966976662007
;; (get-int-log-base26 879)
;; gives: 2

;; clojure have double and float
;; float = single precision 32 bits
;; double = double precision 64 bits

;; how to revert a hash-map in clojure?
(ns user
  (:require [clojure.set]))

;; define the inverted dictionary that is used to hash-map 
;; letters to numbers
(def map-translator-int
  (clojure.set/map-invert map-translator-str))


(def number 987)

(map-translator-int
 (int
  (/ number
     (exp26
      (get-int-log-base26 number)))))


;; clojure how to take modulus?
;; (mod number 26)

(reverse-range (+ 1 (get-int-log-base26 number)))

(map exp26
     (reverse-range
      (+ 1 (get-int-log-base26 number))))



(defn divide-by-number [x]
  (/ number x))



(map int
   (map divide-by-number
        (map exp26
             (reverse-range
              (+ 1
                 (get-int-log-base26
                  number))))))

(map exp26 
  (range
  (+ 1
  (get-int-log-base26
    number))))

;; (type 
;;  (map exp26
;;       (range
;;        (+ 1
;;           (get-int-log-base26
;;            number)))))
;; clojure.lang.LazySeq


(def int-division-from-input-number
  (map int
       (map divide-by-number
            (map exp26
                 (reverse-range
                  (+ 1
                     (get-int-log-base26
                      number)))))))

(def auxiliar-exponential-26
  (map exp26
       (range
        (+ 1
           (get-int-log-base26
            number)))))

(map int
     (map /
          int-division-from-input-number
          auxiliar-exponential-26))


(def number-holder-0 987)
;; (def number-holder-0 15000)
(def power-holder-0 
  (get-int-log-base26 number-holder-0))
(def check-0
  (exp26 power-holder-0))

(def number-holder-1
  (mod number-holder-0 check-0))
(def power-holder-1
  (get-int-log-base26 number-holder-1))
(def check-1
  (exp26 power-holder-1))

(def number-holder-2
  (mod number-holder-1 check-1))
(def power-holder-2
  (get-int-log-base26 number-holder-2))
(def check-2
  (exp26 power-holder-2))

(def number 128)
(defn my-recursion-func [number]
  (if (< number 26) ;; the last step, no need to take the rest
    number
    ((def power-holder (get-int-log-base26 number))
     (def check (exp26 power-holder))
     (def rest (mod number check))
     (my-recursion-func rest) 
     )))



(def number 128)

(defn my-recursion-func [number]
  (if (< number 26) ;; the last step, no need to take the rest
    number
    (my-recursion-func (
      (mod number 
      (exp26 
      (get-int-log-base26 (mod number 26))))))))

    
(my-recursion-func 128)

