(define (over-or-under num1 num2)
  'YOUR-CODE-HERE
  (if (> num1 num2) 1 (if (= num1 num2) 0 -1))
  

)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0


(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (if (null? lst)
    nil
    (if (fn (car lst))
      (cons (car lst) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))
      )
    )
  )

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (make-adder num)
  'YOUR-CODE-HERE
  (lambda (inc) (+ inc num))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13


(define lst
  '((1) 2 (3 4) 5)
)


(define (composed f g)
  'the-program-exe-from-inside-to-outside
  (lambda (x) (f(g x)))
)


(define (remove item lst)
  (if (null? lst)
  nil
  (if (= item (car lst))
  (remove item (cdr lst))
  (cons(car lst) (remove item (cdr lst)))
  )
  )
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)


(define (no-repeats s)
  (if (null? s)
  nil
  (cons (car s) (no-repeats (remove (car s) (cdr s)))
  
  )
))


(define (substitute s old new)
  (if (null? s)
  nil
  (if (pair? (car s))
    
      (cons (substitute (car s) old new) (substitute (cdr s) old new))
    (if (eq? (car s) old)
    (cons new (substitute (cdr s) old new))
    (cons (car s) (substitute (cdr s) old new))
    )
    
  )
  )
)


(define (sub-all s olds news)
  (if (null? s)
  nil
  (if (null? olds) s
  (sub-all (substitute s (car olds) (car news)) (cdr olds) (cdr news))
  )
  )
)

(define (factorial x)
(if (= x 1) 1 (* x (factorial (- x 1))))
)

(define (fib n)
(if (= n 1) 1 (if (= n 0) 0 (+ (fib (- n 2)) (fib (- n 1)))))
)

(define (my-append a b)
(if (null? a) b (cons (car a) (my-append (cdr a) b)))
)

(define (insert element lst index)

)