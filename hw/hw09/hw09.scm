(define (reverse lst)
    (if (null? lst) nil
    (append (reverse (cdr lst)) (list (car lst))))
)
;ban be revealed to quasitation 
