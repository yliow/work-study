import os
import shutil
import config as con

def file_struct():
    if os.path.exists(con.assignment):
        shutil.rmtree(con.assignment)
    for i in range(1, con.num + 1):
        s = r'''%(a)s/%(a)sq%(i)s/doc/''' %{'a': con.assignment, 'i': i}
        os.makedirs(s + 'src')
        os.makedirs(s + 'skel')
