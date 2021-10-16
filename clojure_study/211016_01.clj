;; To start the Clojure REPL use the command below in the terminal:
;; clj

(ns clojure_study
  (:require [clojure.string :as str]))

;; https://www.youtube.com/watch?v=ciGyHkDuPAE&ab_channel=DerekBanas
(defn -main
    "I dont't do a whole lot yet"
    [& args]

    (println "Hello, World!")
    
    ;; how to run the main function
    
    ;; values are imutable in clojure
    (def randVar 10)

    (def aDouble 1.2333)

    (def myBool true)

    (type myBool)
    (type aDouble)

    (def aLong 15)

    (nil? aLong)

    ;; check if a value is positive
    (pos? 15)

    ;; check if a value is negative
    (neg? 15)

    (even? 15)
    (odd? 15)

    (number? 15)

    (integer? 15)

    (float? 15)

    (def aString "Hello there!")

    (format "This is a string %s" aString)

    (def aLong 15)

    (format "5 spaces and %5d" aLong)

    (format "Leading zeros %04d" aLong)
    (format "Leading zeros %010d" aLong)

    (format "%-4d left justified" aLong)

    (def aDouble 1.23456789)
    (format "3 decimals %.3f" aDouble)


    ;; about strings
    (def str1 "This is my 2nd string")
    (str/blank? str1) ;; No such namespace: str

    (def str2 "")
    (str/blank? str2) ;; Boolean

    (type (str/blank? str2)) 


    (str/includes? str1 "my")

    (str/index-of str1 "my")

    ;; Clojure have the concept of vectors

    ;; how to split a string into a vector
    (str/split str1 #" ")

    ;; split based on the location of a number
    (str/split str1 #"\d")

    ;; This is a collection in Clojure
    ;; ["The" "Big" "Clojure" "Brother"]
    (str/join " " ["The" "Big" "Clojure" "Brother"])

    ;; how to replace in a string
    (str/replace "I am 42" #"42" "90")

    (str/trim-newline "  hello  \n")
    (str/trim "  hello  ")
    (str/triml "  hello  ")
    (str/trimr "  hello  ")

    (str/upper-case "  hellow ")
    (str/lower-case "  HELLOW ")

    ;; Lists, they are collections



)


;; just use (-main)