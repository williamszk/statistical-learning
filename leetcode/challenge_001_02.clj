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
  {
    "A" 0,
    "B" 1,
    "C" 2,
    "D" 3,
    "E" 4,
    "F" 5,
    "G" 6,
    "H" 7,
    "I" 8,
    "J" 9,
    "K" 10,
    "L" 11,
    "M" 12,
    "N" 13,
    "O" 14,
    "P" 15,
    "Q" 16,
    "R" 17,
    "S" 18,
    "T" 19,
    "U" 20,
    "V" 21,
    "W" 22,
    "X" 23,
    "Y" 24,
    "Z" 25,
  })

(defn convert-twentysix-to-listchar [string-twentysix]
  (map str (seq string-twentysix)))

(convert-twentysix-to-listchar my-char-number)

(defn get-number-map [key] 
  (get map-translator-str key))

;; (get-number-map "B")
;; (get-number-map "H")
;; (get-number-map "A")
;; (map get-number-map ["C" "B"])

;; define an exponetiation function
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
(defn reverve-list [my-list]
  (reduce conj '() my-list))

;; a function to make a reversed list
;; of a range
(defn reverse-range [n]
  (reverve-list (range n)))
;; (reverse-range 5)

;; get the length of a list
;; (def my-number-char ["C" "B"])
;; (count my-number-char)

;; (reduce + 
;;   (map * 
;;     (map get-number-map my-number-char)
;;     (map exp26 (reverse-range (count my-number-char)))))

;; function to convert a list of chars into
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

;; we still need to create the function that can conver the decimal
;; number into a 26-based number
;; after doing this we can solve the problem

;; CSGHJ * CBA = FNEUZJA
;; (convert-26based-to-10based-number "CSGHJ")
;; (convert-26based-to-10based-number "CBA")






