(define (cbrt x)
  (define (good-enough guess guess-before) (little-changed guess guess-before))

  (define (little-changed guess guess-before)
    ; (define delta (/ (- guess guess-before) guess-before))
    (define delta (- x (* guess (* guess guess))) )
    (< (abs delta) 0.0001))

  (define (improve y) (/ (+ (/ x (* y y)) (* 2 y)) 3))

  (define (cbrt-iter guess guess-before)
    (if (good-enough guess guess-before)
        guess
        (cbrt-iter (improve guess) guess)))

  (cbrt-iter 1 1)
)

(define x (cbrt 27))
(* x (* x x))
