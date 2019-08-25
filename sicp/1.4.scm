(define (a-plus-abs-b a b)
  ((if (> b 0) + -) a b))

; if b is greater than zero, return (+ a b)
; and (- a b) otherwise, following the substitution model
