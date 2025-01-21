import config as con

f = open('makefile', 'r')

s = f.read()

s = r'''tarzip tz:
	tar -cvf %(dest)s.tar %(dest)s
	gzip %(dest)s.tar;
''' % {'dest':con.destination, 'base':con.basepath}

f.write(s)
 
#a06, a07
