print(r"""\begin{console}
%s
\end{console}""" % (ord('A') + ord('b') * 10 + ord('e') * 100))
\end{python}
Now what I'm going to do is to create an array of name-height values, say that
array has size 10.
The index values are of course from 0 to 9.
No problem: the above index value, I just do mod 10 and this will give me an integer
value from 0 to 9. Right?
This means that the name \verb!Abe! will be associated with index 
\begin{python}
v = ord('A') + ord('b') * 10 + ord('e') * 100
print(r"""\begin{console}
%s %% 10 = %s
\end{console}""" % (v, v % 10))
