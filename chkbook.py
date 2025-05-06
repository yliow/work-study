# chkbook.py
import os


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

def check():
    checking_directories = check_dirs()

    print(checking_directories)
    if 'test passed' in checking_directories:
        print('continue doing checks')
    else:
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
                print('would you like me to fill the chapters directory with everything in your chap.tex? (n to leave) ')
                choice = input()
                if choice != 'n':
                    print('working ...')
                else:
                    print('leaving ...')
        else:
            print('leaving')

if __name__ == '__main__':
    check()
