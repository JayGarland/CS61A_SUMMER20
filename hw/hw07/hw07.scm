(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond ((< num 0) -1) ((= num 0) 0) (else 1))
)


(define (square x) (* x x))

(define (pow x y)
  (if (= y 1) x
  (if (even? y)
   (square (pow x (/ y 2))) 
   (* x (square (pow x (/ (- y 1) 2))))))
)


(define (unique s)
  (if (null? s)
  nil
  (cons (car s) (unique(filter (lambda (x) (not (eq? x (car s)))) (cdr s)))
)))


(define (replicate x n)
  
  )


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
)


(define (accumulate-tail combiner start n term)
  'YOUR-CODE-HERE
)


(define-macro (list-of map-expr for var in lst if filter-expr)
  'YOUR-CODE-HERE
)

