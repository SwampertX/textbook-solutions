(define (average a b) (/ (+ a b) 2))

(define (sqrt x)
  (define (good-enough? guess pguess)
    (and (not (= pguess -1))
        (< (/ (abs (- guess pguess)) pguess) 0.001)))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess pguess)
    (if (good-enough? guess pguess)
        guess
        (sqrt-iter (improve guess) guess)))
  (sqrt-iter (/ x 2) -1)
)

(define ans (sqrt 0.01))
(* ans ans)
