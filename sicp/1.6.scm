(define (new-if test conseq alt) (cond (test conseq) (else alt)))

(define (sq x) (* x x))

(define (sqrt-iter n guess)
  ; this line can be switched between if and new-if
  (if (good-enough n guess sq)
      guess
      (sqrt-iter n (improve n guess))))

(define (good-enough n guess fn)
  (< (abs (- (fn guess) n)) 0.00001))

(define (improve n guess)
  (average guess (/ n guess)))

(define (average a b) (/ (+ a b) 2))

(define (my-sqrt n) (sqrt-iter n (/ n 2)))

(define ans (my-sqrt 0.01))
(sq ans)


; through experimentation, we realize that with cond, 
; maximum recursion depth is reached.

; note: I looked at the answer online, and understood
; new-if is a function, and scheme evaluates ALL its arguments
;   when a function is called. Therefore recursion occurs.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;; IMPROVEMENT using block structure ;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0)
)
