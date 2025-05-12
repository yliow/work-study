# chkbook.py
import os
import re
import shutil

# Since chapters directory is a new development, here we will check if the chapters dir is empty, if so, we fill it ...

def chapters_empty():
    chap_empty = True
    for p, dns, fns in os.walk('chapters'):
        if (fns):
            chap_empty = False
    return chap_empty

# Here is where we fill the chapters dir

def fill_chap_dir():
    try:
        with open('chap.tex', 'r') as f:
            input_files = re.findall(r'\\input\{([^}]+)\}', f.read())
        for i in input_files:
            if i != 'solutions.tex':
                shutil.move(i, 'chapters')
    except FileNotFoundError:
        raise FileNotFoundError(f'You are missing a necessary latex file ...')

# Here is where we make sure all necessary directories are present

def check_dirs():
    exercises_dir_present = False
    stdout_dir_present = False
    chapters_dir_present = False
    for p, dns, fns in os.walk('.'):
        for dn in dns:
            if dn == 'exercises':
                exercises_dir_present = True
            elif dn == 'stdout':
                stdout_dir_present = True
            elif dn == 'chapters':
                chapters_dir_present = True
        break
    if exercises_dir_present and stdout_dir_present and chapters_dir_present:
        return 'test passed (all directories are present) ...'

    s = 'You need '

    if not exercises_dir_present:
        s += 'exercises '
    if not stdout_dir_present:
        s += 'stdout '
    if not chapters_dir_present:
        s += 'chapters '

    return s + 'directories'

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
            if 'chapters' in checking_directories:
                os.mkdir('chapters')
        else:
            print('leaving, insufficient directories to use these notes in makebook')
            return

    if not os.path.isfile('chap.tex'):
        print('You need a chap.tex file !!!')
        print('leaving, insufficient file(s) to use these notes in makebook')
        return
    elif chapters_empty():
        print('would you like me to fill the chapters directory with everything in your chap.tex? (n to leave) ')
        choice = input()
        if choice != 'n':
            fill_chap_dir()
        else:
            print('leaving, insufficient chapters directory to use these notes in makebook')
    print('You have sufficient material to use the notes in makebook')
    print('All tests ... passed')
    return

if __name__ == '__main__':
    check()
