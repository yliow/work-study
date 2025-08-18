import os
import glob
wdir = os.getcwd()
os.chdir('%s/n' % wdir)
f = os.listdir()
#make a string for the file to be substituted in the cmd
for i in f:
    if os.path.isdir(i):
        #print("trve", i)
        x = os.listdir('%s/n/%s' % (wdir, i))
        for a in x:
            #print(a)
            #print(glob.glob('*%s/%s/*.odt' % (wdir, a)))
            if a.find('.odt') >= 0:
                print("running on", a)
                # print('\n\npandoc -s %s/n/%s/%s --pdf-engine=pdflatex -o main.tex\n\n' % (wdir, i, a))
                
                os.system('pandoc -s %s/n/%s/%s --pdf-engine=pdflatex -o %s/n/%s/main.tex' % (wdir, i, a, wdir, i))
                # os.system('')
                # os.chdir()
                # os.chdir()
            else:
                continue
                #print("PASSED %s" % a)
                
