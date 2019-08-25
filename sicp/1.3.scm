; A recap on syntax
; variable declaration:
;   (define variable_name expression)
; procedure declaration:
;   (define (procedure_name ...params) return_expression)
; conditional statements:
;   (cond (p1 e1) (p2 e2) ... (pn en) [(else e)])
; conditional expression
;   (if pred conseq alt)


(define (square x) (* x x))

(define (f x y z)
  (if (< x y)
      (if (< x z) (+ (square y) (square z))
                  (+ (square x) (square y))) ; z < x < y
      (if (< y z) (+ (square x) (square z))
                  (+ (square x) (square y))))) ; z < y < x

(f 2 3 1) ;13
(f 1 1 0) ;2
(f -10 2 -1) ;5
