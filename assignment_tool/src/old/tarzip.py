import config as con

f = open('makefile', 'a')

s = r'''tarzip tz:
	tar -cvf %(dest)s.tar %(dest)s
	gzip %(dest)s.tar;
''' % {'dest':con.destination, 'base':con.basepath}

f.write(s)
