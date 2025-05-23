from makebook import *

#variables
found_notes = None
selected_notes = None
processed_notes = None
new_dir_name = None

def greeting():
    print("█▀▄▀█ █▀▀█ █─█ █▀▀ █▀▀▄ █▀▀█ █▀▀█ █─█ \n█─▀─█ █▄▄█ █▀▄ █▀▀ █▀▀▄ █──█ █──█ █▀▄ \n▀───▀ ▀──▀ ▀─▀ ▀▀▀ ▀▀▀─ ▀▀▀▀ ▀▀▀▀ ▀─▀")
    print("Makebook v1, 2025-??")
def goodbye():
    if processed_notes == None:
        print("Closing Makebook, goodbye...")
    else:
        print("Notes processed:\n", (print(i) for i in processed_notes), "Closing Makebook, goodbye...")
#display options menu
def menu():
    print('--------------------------------------')
    print("Select an option:")
    print("|1. Display detected notes directories\n|2. Select which note(s) to process\n|3. Make a new directory for notes\n|4. Process selected notes\n|5. Quit")
    print('--------------------------------------\n\n')
    return

#files is a list of potential directories of notes that the user can select from to process    
def show_notes(files):
    c = 0
    print("found potential notes to be processed:")
    for i in files:
        print('[%s]' % c, i, end ='   ')
        c += 1

#list all the potential notes directories found by the program
def find_notes():
    f = os.listdir()
    notes = {}
    c = 0
    for i in f:
        print(os.getcwd() + i, os.path.isdir(i) and os.path.isfile('chap.tex'))
        if os.path.isdir(i) and not os.path.isfile('chap.tex'):
            print("UNACCEPTABLE FILE STRUCTURE, NO 'chap.tex' FOR", i)
        elif os.path.isdir(i) and os.path.isfile('chap.tex'):
            print("ACCEPTABLE FILE STRUCTURE FOR", i)
            notes[c] = i
            c += 1
        else:
            continue
    found_notes = notes
    show_notes(found_notes)
    return

#select the notes to be processed from a list
def select_process():
    print("Enter your selection(s), or type 'a' for all")
    
    return

#make a new dir for new notes
def make_new_dir():
    #call mkbook or chkbook function to make a new dir
    return

#process selected notes
def process_notes(selected_notes=None):
    #wdir = os.getcwd()
    if selected_notes == None:
        print("no notes selected for processing, make your selections first")
    #os.chdir(wdir)
    else:
        print("Your selections are", selected_notes)
        for i in selected_notes:
            print("processing", i)
            #os.chdir(i)
            make_book(i)
    
#process user selections
def get_selection(selection):
    #TODO: IMPLEMENT PROCESSING
    match selection:
        case 1:
            print('1 -----------------------------------')
            find_notes()
        case 2:
            print('2 -----------------------------------')
            select_process()
        case 3:
            print('3 -----------------------------------')
            make_new_dir()
        case 4:
            print('4 -----------------------------------')
            process_notes()
        case 5:
            print('5 -----------------------------------')
            return
        case _:
            print("Invalid selection")
    return
        
#keep the user in the loop until quit has been selected        
def menu_loop():
    greeting()
    menu()
    selection = int(input())
    while 0 < selection < 5:
        get_selection(selection)
        menu()
        selection = int(input())
        
menu_loop()
