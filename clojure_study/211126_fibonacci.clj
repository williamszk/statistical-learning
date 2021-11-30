;; Build a function that calculates the Fibonacci sequence
;; give n to the function than it returns that Fibonacci number

;; /usr/local/bin/clj

(defn fibonacci [n]
  (if (= n 1) 1
    (if (= n 2) 1
      (+ (fibonacci (- n 2)) (fibonacci (- n 1))))))

;; n = 4, the fibonacci is 3
;; n = 7, the fibonacci is 13

(fibonacci 4)
(fibonacci 7)
(fibonacci 8)
