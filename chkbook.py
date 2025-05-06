# chkbook.py
import os

def check():
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

if __name__ == '__main__':
    checking_directories = check()

    print(checking_directories)
    if 'test passed' in checking_directories:
        print('continue doing checks')
    else:
        print()
        print('would you like me to create ')
        if 'exercises' in checking_directories:
            print('an exercises directory? ')
            choice = input()
            if choice != 'n':
                print('creating exercises directory for you ...')
                os.mkdir('exercises')
            else:
                print('leaving ...')
        print()
        if 'stdout' in checking_directories:
            print('an stdout directory? ')
            choice = input()
            if choice != 'n':
                print('creating stdout directory for you ...')
                os.mkdir('stdout')
            else:
                print('leaving ...')
        print()
        if 'chapters' in checking_directories:
            print('an chapters directory? ')
            choice = input()
            if choice != 'n':
                print('creating chapters directory for you ...')
                os.mkdir('chapters')
            else:
                print('leaving ...')
