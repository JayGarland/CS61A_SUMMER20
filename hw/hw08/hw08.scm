(define (rle s)
(define (next s n)
(if
(null? s)
nil
(if (= n (car s)) (next (cdr-stream s) n) s)))

(define (helper lst num n)
(if (and (not (null? lst)) (= (car lst) n))
(helper (cdr-stream lst) (+ num 1) n) (list n num)
)
)

(if (null? s) nil
(cons-stream (helper s 0 (car s)) (rle (next s (car s))))
)
)
;for the "next" function it defines the afterward list and refers the next one car s, in every next, helper func there's cdr-stream behind of the tail, the next is used to compare the car s with the next one, for the helper, first to see if the lst is null or the next car s is equal to the previous, if so then add the number of times the same car s showed up and do recursion or either way just list it, and for the last return, to check if it's null and cons-stream the helper parameter and also recursion of itself rle of the next function


(define (group-by-nondecreasing s)
    (define (next lst curr)
    (if (null? lst)
    nil
    (if (>= (car lst) curr) (next (cdr-stream lst) (car lst)) lst)
    )
    )
    (define (helper curr lst res)
    (if (null? lst) res
    (if (>= (car lst) curr)
    (helper (car lst) (cdr-stream lst) (append res (list (car lst))))
    res
    
    )
    )
    )
    
    (if (null? s)
    nil
    (cons-stream (helper (car s) (cdr-stream s) (list (car s))) (group-by-nondecreasing (next s (car s)))) ;in this cons-stream of recursion exe the s in the next func is always the same s that nothing changed but just in case of the car lst is greater than the curr the lst would be pushed forward then the curr change and transfer it to helper, otherwise the lst keep the same that its first element does not append into the current cons lst and just list itself
    )
    )


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

