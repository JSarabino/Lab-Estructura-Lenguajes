#lang racket
;1. Defina una función que permita convertir de grados centígrados a Fahrenheit.
(define (conversion c)
  (+ (/ (* c 9) 5) 32)
)

;2. Defina una función que permita determinar el menor entre dos números.
(define (menor a b)
  (cond ((< a b) a)
  (else (menor b a))
  )
)

;3. Defina una función recursiva que permita sumar los n primeros números.
(define (sumarN n)
  (cond ((= n 0) 0)
    (else
     (+ (sumarN (- n 1)) n)
    )
  )
)

;Sumatoria con for
(define (sumatoria n)
  (define sum 0)
  (for ([i (in-range 1 (+ n 1))])
    (set! sum (+ sum i))
    (writeln i)
  )
  sum
)

;Sumatoria con if y recursivo
(define (sumatoriaR n)
  (if (= n 0) 0
      (+ n (sumatoriaR (- n 1)))
  )
)

;4. Defina una función que permita encontrar el factorial de un número de forma iterativa y recursiva.
(define (factorial n)
  (cond ((= n 0) 1)
        ((= n 1) 1)
    (else
     (* (factorial (- n 1)) n)
    )
  )
)

;5. Defina una función que permita encontrar la potencia de un número de forma iterativa y recursiva.
(define (potencia n p)
  (cond ((= p 0) 1)
        ((= p 1) n)
    (else
     (* (potencia n (- p 1)) n)
    )
  )
)
