;; Chosen programming language:  Clojure
;; Chosen challenge platform:  reddit_dailyprogrammer
;; Chosen challenge id:  31

;; I've found three alternatives for challenge 31:
;; https://www.reddit.com/r/dailyprogrammer/comments/rg1vv/3272012_challenge_31_easy/
;; https://www.reddit.com/r/dailyprogrammer/comments/rg25w/3272012_challenge_31_intermediate/
;; https://www.reddit.com/r/dailyprogrammer/comments/rg2dj/3272012_challenge_31_difficult/


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


;; How to create a map in Clojure?
(hash-map)

{}

(hash-map :key1 11, :key2 22)
(hash-map :key1 1, :key1 2)

{:key1 1, :key2 2}


{"A" 1, "B" 2}

{:key1 1, :key1 1}
;; Syntax error reading source at (REPL:7:19).
;; Duplicate key: :key1

(def )


;; What are clojure's syntax convetions?
;; https://github.com/bbatsov/clojure-style-guide

;; https://github.com/bbatsov/clojure-style-guide#functions-and-variables
;; use lisp-case for variables and functions
(def some-var 2)

(def map-translator 
  {
    :A 0,
    :B 1,
    :C 2,
    :D 3,
    :E 4,
    :F 5,
    :G 6,
    :H 7,
    :I 8,
    :J 9,
    :K 10,
    :L 11,
    :M 12,
    :N 13,
    :O 14,
    :P 15,
    :Q 16,
    :R 17,
    :S 18,
    :T 19,
    :U 20,
    :V 21,
    :W 22,
    :X 23,
    :Y 24,
    :Z 25,
  })



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


(get map-translator-str "T")

;; how to access elements of a map?
(get map-translator :Z)


(def my-number "BA")

;; how to create lists in Clojure?
;; https://stackoverflow.com/a/5083774/15875971


(list "Berlin" "Brussels" "Helsinki" "Madrid")

;; a shorter way to create the same list
'("Berlin" "Brussels" "Helsinki" "Madrid")


(def my-list-number-letters 
  '("B" "A"))


;; How to convert a string into a list where each letter is an
;; element of the list?


;; How to access elements of a list in Clojure?
(nth my-list-number-letters 0)
;; we need to use the nth function

(nth my-list-number-letters 0)

(get map-translator 
  :B)

;; (get map-translator 
;;   :(nth my-list-number-letters 0))


my-list-number-letters

;; There is a difference between map and hash-map
;; a map is like an apply a for loop, 
;; but the hash-map is like a dictionary

;; an example of map with the function inc
(map inc [1 2 3 4 5 ])

(inc 1)

(map + [1 2 3] [4 5 6])

;; what happens when one of the lists is lengthier than the other?
(map + [1 2 3] [4 5 6 7])
;; the map stops at the shortest one

(defn get-number-map [key] (get map-translator-str key))

(get-number-map "B")
(get-number-map "H")
(get-number-map "A")

(map get-number-map my-list-number-letters)

(map get-number-map ["C" "B"])


(defn exp [x n]
  (if (zero? n) 1
    (* x (exp x (dec n)))))

(defn exp26 [n]
  (exp 26 n))

(exp26 1)
(exp26 0)
(exp26 2)
(* 26 26)

(map exp26 [2 1 0])

(reduce + [676 26 1])

(reduce + (map exp26 [2 1 0]))

(reduce + 
  (map * 
    (map get-number-map ["C" "B"])
    (map exp26 [1 0])))


(defn reverve-list [my-list]
  (reduce conj '() my-list))

;; a function to make a reversed list
(defn reverse-range [n]
  (reverve-list (range n)))

(reverse-range 5)


(def my-number-char ["C" "B"])
my-number-char

my-number-char

;; get the length of a list
(count my-number-char)


(def my-number-char ["C" "B" "B"])
(def my-number-char ["C" "B"])

(reduce + 
  (map * 
    (map get-number-map my-number-char)
    (map exp26 (reverse-range (count my-number-char)))))

(* 676 2)

(reduce + [1352 26 1])


(defn convert-charlist-decnumber [list-char]
  (reduce + 
    (map * 
      (map get-number-map my-number-char)
      (map exp26 (reverse-range (count my-number-char))))))


(def my-number-char ["C" "B"])
(convert-charlist-decnumber my-number-char)

(def my-number-char ["C" "B" "B"])
(convert-charlist-decnumber my-number-char)

(def my-number-char ["U"])
(convert-charlist-decnumber my-number-char)


(def my-number-char ["W" "H"])
(convert-charlist-decnumber my-number-char)



(* 22 26)



