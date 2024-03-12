v = ord('A') + ord('b') * 10 + ord('e') * 100
print(r"""\begin{console}
%s %% 10 = %s
\end{console}""" % (v, v % 10))
