(define (split-at lst n)
  (define (helper head tail n)
  (if (null? tail)
  (cons head nil)
  (if (= n 0)
  (cons head tail)
  (helper (append head (list (car tail))) (cdr tail) (- n 1))
  )
  )
  )
  (helper nil lst n)
)
;use method of binary separately with head and tail, the initial head is nil, and tail is list, the first of first base case is when tail null then construct head, otherwise, when the first n is 0, cons all, in other case, recursively call helper, and use append to add previous head to the list of car tail, so tail would be the cdr tail, for case of this, tail move forward following n subtracted by one, everytime
;call helper with initial value


(define-macro (switch expr cases)
	(cons `cond
		(map (lambda (case) (cons (list `eq? expr (car case)) (cdr case)))
    			cases))
)
;format like list `eq, list `begin .etc are the macro procedure that is called on the operand expressions without evaluate them first, and then evaluate the expression returned from the macro procedure

