# chkbook.py
import os
import re
import shutil

# Here is where we make sure all necessary directories are present

def check_dirs():
    exercises_dir_present = False
    stdout_dir_present = False
    for p, dns, fns in os.walk('.'):
        for dn in dns:
            if dn == 'exercises':
                exercises_dir_present = True
            elif dn == 'stdout':
                stdout_dir_present = True
        break
    if exercises_dir_present and stdout_dir_present:
        return 'test passed (all directories are present) ...'

    s = 'You need '

    if not exercises_dir_present and not stdout_dir_present:
        s += 'exercises and stdout directories'
    elif not exercises_dir_present:
        s += 'exercises directory'
    elif not stdout_dir_present:
        s += 'stdout directory'

    return s

# Here is where we make sure all necessary files are present

def check():
    checking_directories = check_dirs()

    print(checking_directories)
    if 'test passed' not in checking_directories:
        print()
        print('would you like me to create the directories for you? (n to leave) ')
        choice = input()
        if choice != 'n':
            if 'exercises' in checking_directories:
                os.mkdir('exercises')
            if 'stdout' in checking_directories:
                os.mkdir('stdout')
        else:
            print('leaving, insufficient directories to use these notes in makebook')
            return

    if not os.path.isfile('chap.tex'):
        print('You need a chap.tex file !!!')
        print('leaving, insufficient file(s) to use these notes in makebook')
        return

    print('You have sufficient material to use the notes in makebook')
    print('All tests ... passed')
    return

if __name__ == '__main__':
    check()
