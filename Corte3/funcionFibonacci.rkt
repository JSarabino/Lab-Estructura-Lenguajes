#lang racket
(define (fibonacci n)
  (cond ((= n 0) 0);casos base y valores de retorno
        ((= n 1) 1)
        (else
         (+ (fibonacci (- n 1)) (fibonacci (- n 2)))
        )
  )
)