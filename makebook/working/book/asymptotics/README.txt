https://math.stackexchange.com/questions/925053/using-limits-to-determine-big-o-big-omega-and-big-theta
https://www.cs.fsu.edu/~lacher/courses/notes/asymptotics.pdf
http://web.mit.edu/broder/Public/asymptotics-cheatsheet.pdf

standardize pseudo table:
                            time    number of times 
         i = 1              t1      1
         s = 0              t2      1
LOOP:    if i > n:          t3      n + 1
             goto ENDLOOP   t4      1
         term = i * i       t5      n
         s = s + term       t6      n
         i = i + 1          t7      n
         goto LOOP          t8      n
ENDLOOP:

pdflatex times: latest at bottom
3m10s
1m42.719s
2m19.962s

real	4m7.314s
user	2m0.162s
sys	0m1.314s

real	1m30.033s
user	0m44.440s
sys	0m0.514s

real	2m14.322s
user	0m54.990s
sys	0m0.491s
