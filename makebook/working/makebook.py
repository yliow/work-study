import os
import re
import shutil

old_dir = os.getcwd() + '/'    
new_dir = os.getcwd() + '/book/'

# variables
found_notes = []
selected_notes = []
processed_notes = []
# new_dir_name = None

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
    print("█▀▄▀█ █▀▀█ █ █ █▀▀ █▀▀▄ █▀▀█ █▀▀█ █ █ \n█ ▀ █ █▄▄█ █▀▄ █▀▀ █▀▀▄ █  █ █  █ █▀▄ \n▀   ▀ ▀  ▀ ▀ ▀ ▀▀▀ ▀▀▀  ▀▀▀▀ ▀▀▀▀ ▀ ▀")
    #update this as necessary
    print("Makebook v0.1, 2025")
    
def goodbye():
    if processed_notes == None or len(processed_notes) <= 0:
        print("Closing Makebook, goodbye...")
    else:
        print("Notes processed:\n", (print(i) for i in processed_notes), "Closing Makebook, goodbye...")
        
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

#process selected notes
def process_notes():
    global selected_notes
    wdir = os.getcwd()
    if not selected_notes:
        print("no notes selected for processing, make your selections first")
    else:
        for i in selected_notes:
            print(f'processing {i} ...')
            make_book(i)
    
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
    os.system('cp %s %s' % (old_dir + f, new_dir + f))
    
def make_book(dir_):
    print(f'making {dir_} ...')
    # make_new_book_dir()

menu_loop()
goodbye()
