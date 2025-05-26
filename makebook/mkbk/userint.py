'''
=================================================================
STUFF THAT NEEDS TO BE DONE
=================================================================
fix exiting loop by inputting incorrect choices (NaN, too high of a num, etc)
discard potential duplicates entered under select_notes() func
add option 3
'''

from makebook import *

#variables
found_notes = []
selected_notes = []
processed_notes = []
new_dir_name = None

def greeting():
    print("█▀▄▀█ █▀▀█ █─█ █▀▀ █▀▀▄ █▀▀█ █▀▀█ █─█ \n█─▀─█ █▄▄█ █▀▄ █▀▀ █▀▀▄ █──█ █──█ █▀▄ \n▀───▀ ▀──▀ ▀─▀ ▀▀▀ ▀▀▀─ ▀▀▀▀ ▀▀▀▀ ▀─▀")
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
def select_process(found_notes):
    if found_notes == None or len(found_notes) <= 0:
        dbg_txt("No notes found for selection")
        print(found_notes)
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
        print("choice = ", choice)
        for i in choice:
            i = int(i)
        for i in choice:
            print(i)
            if i.isnumeric() and 0 <= int(i) < len(found_notes) and int(i) not in selected_notes:
                selected_notes.append(found_notes[int(i)])
    print("Your selections are:", selected_notes)
    return

#make a new dir for new notes
def make_new_dir():
    make_new_book_dir()
    return

#process selected notes
def process_notes(selected_notes):
    wdir = os.getcwd()
    if selected_notes == None or len(selected_notes) <= 0:
        print("no notes selected for processing, make your selections first")
    else:
        print("Your selections are", selected_notes)
        for i in selected_notes:
            print("processing", i)
            os.chdir("%s/%s/" % (wdir, i))
            make_book(i)
    
#process user selections
def get_selection(selection):
    #TODO: IMPLEMENT PROCESSING
    match selection:
        case 1:
            find_notes()
        case 2:
            select_process(found_notes)
        case 3:
            make_new_dir()
        case 4:
            process_notes(selected_notes)
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
            selection = 1
        get_selection(selection)

menu_loop()
goodbye()
