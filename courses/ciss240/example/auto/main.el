(TeX-add-style-hook "main"
 (lambda ()
    (TeX-add-symbols
     '("DrawBoxAndArrow" ["argument"] 3)
     '("tikzmark" 1)
     '("EMPHASIZE" 1))
    (TeX-run-style-hooks
     "listings"
     "mybookpreamble"
     "yliow")))

