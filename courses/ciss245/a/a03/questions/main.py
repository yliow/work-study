import glob, os.path
fs = glob.glob('../*/question/main.tex')
for i, f in enumerate(fs):
    q = i + 1
    base, filename = os.path.split(f)
    print r'''

\newpage{\bf Q%s. }this is a test \subimport*{%s/}{%s}

''' % (q, base, filename)

    print

