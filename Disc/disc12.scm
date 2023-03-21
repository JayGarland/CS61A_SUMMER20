(define (map-stream f s) (if (null? s) nil
 (cons-stream (f (car s)) (map-stream f (cdr-stream s)))
 ))


(define (slice s start end) 
(cond ((or (null? s) (= end 0) nil))
((> start 0) (slice (cdr-stream s)  ))
(else (cons (car s) (slice (cdr-stream s) (- start 1) (- end 1))))
)
)

(define factorials (cons-stream 1 (combine-with * (naturals 1) (factorials))))

(define fibs (cons-stream 0 (cons-stream 1 (combine-with + fibs (cdr-stream fibs)))))




(define (sieve s) (cons-stream (car s) (sieve (sift (car s) (cdr-stream s)))))

(define (sift prime s) (filter-stream (lambda (x) (not (= 0 (modulo x prime))) s)))

