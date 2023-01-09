;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname lectures) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;Simple Expressions
(+ 3 4)
(+ 3 (* 2 3))
(/ 12 (* 2 3))

(sqr 3)
(sqrt 16)

(/ (+ 4 6.2 -12) 3)

;Evaluation
(+ 2 (* 3 4) (- (+ 1 2) 3))
(+ 2 12      (- (+ 1 2) 3))
(+ 2 12      (- 3       3))
(+ 2 12      0)
14

;Strings
"apple"
(string-length "apple")
(string-append "Ada" " " "Lovelace")
(substring "Caribou" 2 4)

;Images
(require 2htdp/image)

(circle 10 "solid" "red")
(rectangle 30 60 "outline" "blue")

(text "hello" 24 "orange")

(above (circle 10 "solid" "red")
       (circle 20 "solid" "yellow")
       (circle 30 "solid" "green"))

(beside (circle 10 "solid" "red")
        (circle 20 "solid" "yellow")
        (circle 30 "solid" "green"))

(overlay (circle 10 "solid" "red")
        (circle 20 "solid" "yellow")
        (circle 30 "solid" "green"))

;Constant definitions
(define WIDTH 400)
(define HEIGHT 600)