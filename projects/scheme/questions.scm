(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement. (cond ((null? rests) nil)
;(else (map (lambda first (list first (car rests))) rests)


(define (cons-all first rests)
  'replace-this-line
  ;(cond ((null? rests) nil)((eq? rests nil) nil)
;(else (map (lambda (first) (cons first (car rests))) (cons-all first (cdr rests)))
   (cond
  ((null? rests) nil)
    (else (cons (append (list first) (car rests)) (cons-all first (cdr rests)))
  )))

(define (zip pairs)
  'replace-this-line
  (list (map car pairs) (map cadr pairs))  ;containing a list within an existed list which used double map to continue the rest of pairs in the same order
  )



;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  'replace-this-line
  (define (enumeratehelper s n)
  (if (null? s)
    nil 
    (if (eq? s nil)
      nil
      (cons (list n (car s)) (enumeratehelper (cdr s) (+ n 1)))
      )
  ))
  (enumeratehelper s 0)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS


(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  'replace-this-line
  (cond ((= total 0) '(nil))
  ((< total 0) nil)
  ((null? denoms) nil)
  (else 
  (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) (list-change total (cdr denoms))))
  ))
  
  ; END PROBLEM 17

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (append (cons (cons 'lambda (cons (car (zip values)) (map let-to-lambda body))) nil) (map let-to-lambda (cadr (zip values))))
           
           ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18

          (cons (car expr) (map let-to-lambda (cdr expr)))  ;To get the value will be calculated      
         ; END PROBLEM 18
         )))