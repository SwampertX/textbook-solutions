; note the subtlety in brackets
; the first (p) signifies we are defining a proc
; the second (p) signifies we are doing an application
;   of p on no arguments, which recurses infinitely

(define (p) (p))

(define (test x y)
  (if (= x 0) 0 y))

(test 0 (p)) 

; normal order: fully expand then reduce
; (test 0 (p))
; (if (= 0 0) 0 (p))
; 0

; applicative order: 
; (test 0 (p))
; since the arguments are first evaluated, we are stuck

