import os
import glob
import re
import shutil
import subprocess
from pathlib import Path

old_dir = os.getcwd() + '/'    
new_dir = os.getcwd() + '/book/'

# variables
found_notes = []
selected_notes = []
processed_notes = []
# new_dir_name = None

#process selected notes
def process_notes():
    global selected_notes
    wdir = os.getcwd()
    if not selected_notes:
        print("no notes selected for processing, make your selections first")
    else:
        makemakefile()
        shutil.copy(old_dir + selected_notes[0] + '/thismacros.tex', new_dir)
        shutil.copy(old_dir + selected_notes[0] + '/thispackages.tex', new_dir)
        shutil.copy(old_dir + selected_notes[0] + '/thispreamble.tex', new_dir)
        shutil.copy(old_dir + selected_notes[0] + '/thispostamble.tex', new_dir)
        shutil.copy(old_dir + selected_notes[0] + '/thistitle.tex', new_dir)
        print("Copied prerequisite files to book directory ...\n")
        for i in selected_notes:
            print(f'processing {i} ...')
            moveother(i)
            makefiles(i)
            update_input_in_dir(i)
            blot_out_makefile_command(i)
            subprocess.run(["rm", "-f", new_dir + i + '/main.tex'], check=True)
        for path in Path(new_dir).rglob('*.cpp'):
            shutil.copy(path, new_dir)
        for path in Path(new_dir).rglob('*.py'):
            shutil.copy(path, new_dir)
        print('Copied all cpp and py files to book directory')
        finishupfiles()

def blot_out_makefile_command(i):
    with open(new_dir + i + '/makefile', 'r') as f:
        lines = f.readlines()

    new_lines = [line for line in lines if "$(PDF)" not in line]

    with open(new_dir + i + '/makefile', 'w') as f:
        f.writelines(new_lines)


def update_input_in_dir(i):
    os.chdir(new_dir + i)
    tex_files = glob.glob('**/*.tex', recursive=True)

    for filepath in tex_files:
        with open(filepath, 'r') as f:
            content = f.read()
        new_content = content.replace(r"\input{", fr"\input{{{i}/")

        with open(filepath, 'w') as f:
            f.write(new_content)

def finishupfiles():
    with open(new_dir + 'makefile', 'a') as f:
        f.write('''\t$(PDF)
c:
	$(LATEXRM)
v:
	$(OPEN) main.pdf''')
    with open(new_dir + 'chap.tex', 'a') as f:
        f.write(r'''\begin{python0}
from solutions import *
prepare_solutions()
\end{python0}
\input{solutions.tex}
\begin{python0}
from solutions import *
clear()
\end{python0}''')
    with open(new_dir + 'main.tex', 'w') as f:
        f.write('''%-*-latex-*-
\input{thispreamble}
\clearsolutions
\input{chap.tex}
\input{thispostamble}''')

def makemakefile():
    with open(new_dir + 'makefile', 'w') as f:
        f.write(r'''OPEN = xdg-open
PDF = rm -rf solutions.tex; touch solutions.tex; \
	pdflatex --shell-escape -halt-on-error -interaction=nonstopmode -file-line-error $@.tex && \
	pythontex main.tex && \
        makeindex $@.idx && \
        pdflatex --shell-escape $@.tex && \
        $(OPEN) $@.pdf;
LATEXRM = rm -f \
        main.aux main.ilg main.log main.idx main.ind main.out \
        main.py.err main.py.out \
        comment.cut comment.err comment.out \
        latex.py
main:''')
        f.write('\n')

def makefiles(dr):
    with open(old_dir + dr + "/chap.tex", 'r') as f:
        lines = f.readlines()

    moved_lines = []

    pattern = re.compile(r"^[^%]*\\newpage\\input\{.*\}\s*$")

    for line in lines:
        if pattern.match(line):
            moved_lines.append(line[:15] + dr + '/' + line[15:])

    with open(new_dir + 'chap.tex', 'a') as f:
        f.write(f'% notes for {dr}\n')
        f.writelines(moved_lines)
        f.write('\n\n')

    with open(new_dir + 'makefile', 'a') as f:
        f.write(f'\tcd {dr} ; make ; cd .. ; \n')

# Here is where we make sure all necessary directories are present
def check_dirs(dir_):
    exercises_dir_present = False
    stdout_dir_present = False
    for p, dns, fns in os.walk(dir_):
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

def check(dir_):
    checking_directories = check_dirs(dir_)

    print(checking_directories)
    if 'test passed' not in checking_directories:
        print()
        print('would you like me to create the directories for you? (n to leave) ')
        choice = input()
        os.chdir(dir_)
        if choice != 'n':
            if 'exercises' in checking_directories:
                os.mkdir('exercises')
            if 'stdout' in checking_directories:
                os.mkdir('stdout')
        else:
            print('leaving, insufficient directories to use these notes in makebook')
            return

    os.chdir(new_dir)

    if not os.path.isfile(f'{dir_}/chap.tex'):
        print('You need a chap.tex file !!!')
        print('leaving, insufficient file(s) to use these notes in makebook')
        return

    print(f'You have sufficient material to use {dir_} in makebook\n')
    return

#basic block text greeting
def greeting():
    print('''
█▀▄▀█ █▀▀█ █ █ █▀▀ █▀▀▄ █▀▀█ █▀▀█ █ █ 
█ ▀ █ █▄▄█ █▀▄ █▀▀ █▀▀▄ █  █ █  █ █▀▄ 
▀   ▀ ▀  ▀ ▀ ▀ ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▀▀▀ ▀ ▀
          ''')
    #update this as necessary
    print("Makebook v0.1, 2025")
    
def goodbye():
    if processed_notes == None or len(processed_notes) <= 0:
        print("Closing Makebook, goodbye...")
    else:
        print("Notes processed:\n", (print(i) for i in processed_notes), "book made.\nClosing Makebook, goodbye...")
        
#display options menu
def menu():
    print('--------------------------------------')
    print("Select an option:")
    print("|1. Find valid notes directories\n|2. Select which notes to process\n|3. Make a new directory for notes\n|4. Process selected notes\n|5. Quit")
    print('--------------------------------------\n')
    return

#f is a list of potential directories of notes that the user can select from to process    
def show_notes(f):
    c = 0
    print("found potential notes to be processed:")
    for i in f:
        print('[%s]' % c, i)
        c += 1

#list all the potential notes directories found by the program
def find_notes():
    f = os.listdir()
    c = 0
    for i in f:
        if i in found_notes:
            continue
        elif os.path.isdir(i) and not os.path.isfile('%s/chap.tex' % i):
            print("UNACCEPTABLE FILE STRUCTURE, NO 'chap.tex' FOR", i)
        elif os.path.isdir(i) and os.path.isfile('%s/chap.tex' % i):
            print("ACCEPTABLE FILE STRUCTURE FOR", i)
            found_notes.append(i)
            c += 1
        else:
            continue
    print()
    show_notes(found_notes)
    print()
    return

#select the notes to be processed from a list
def select_process():
    global found_notes
    global selected_notes
    if found_notes == None or len(found_notes) <= 0:
        dbg_txt("No notes found for selection")
        return
    print("Enter your selection(s) as a comma separated list, or type 'a' for all\nTo return to the menu, enter 'q'")
    show_notes(found_notes)
    choice = input()
    if choice == 'q':
        return
    elif choice == 'a':
        for i in found_notes:
            selected_notes.append(i)
    else:
        choice = choice.replace(' ', '')
        choice = choice.split(',')
        for i in choice:
            if i.isnumeric():
                i = int(i)
            else:
                i = -1
        used = []
        for i in choice:
            if i.isnumeric() and 0 <= int(i) < len(found_notes) and not (int(i) in used):
                used.append(int(i))
                selected_notes.append(found_notes[int(i)])
    print("Your selections are:", selected_notes, end = '\n\n')
    return

#make a new dir for new notes
def make_new_dir():
    make_new_book_dir()
    return

    
#process user selections
def get_selection(selection):
    match selection:
        case 1:
            find_notes()
        case 2:
            select_process()
        case 3:
            make_new_dir()
        case 4:
            process_notes()
        case 5:
            return
        case _:
            print("Invalid selection")
            selection = 0
    return

#keep the user in the loop until quit has been selected        
def menu_loop():
    greeting()
    selection = 0
    while 0 <= selection < 5:
        menu()
        #print("found [%s], selected [%s], process [%s]" % (found_notes, selected_notes, processed_notes))
        try:
            selection = int(input())
        except:
            print("Invalid selection")
            selection = 0
        get_selection(selection)

#for important messages during compilation
def dbg_txt(msg):
    for i in range(len(msg) + 2):
        print('*', end='')
    print()
    print("# %s #" % msg)
    for i in range(len(msg) + 2):
        print('*', end='')
    print()
    

#make a new directory
def make_new_book_dir():
    global selected_notes
    if not os.path.isdir('book'):
        os.system('mkdir book')
        print("created new directory for compiled book at", new_dir)
    for dn in selected_notes:
        print(f'{old_dir}/{dn}')
        check(old_dir + dn)
    return

#looks at all the .tex files within the directory and moves the files not explicity in the blacklist into the chapters folder
def movechaps(f):
    blacklist = ['thispreamble', 'thispostamble', 'thismacros', 'main']
    for i in blacklist:
        if f.find(i) >= 0:
            print('%s, not copying' % f)
            return
        else:
            os.system('cp %s %s' % (old_dir + f, new_dir + 'chapters/' + f))
            return

#moves all the stdout into the correct stdout folder
def movestd(f):
    os.system('cp %s %s' % (old_dir + f, new_dir + 'stdout/' + f))
    return

#moves files that are to be in the same level dir as makebook and the chaps
def moveother(f):
    print(f'copying over {f} to book/ ...')
    os.system('cp -r %s %s' % (old_dir + f, new_dir + f))


menu_loop()
goodbye()
