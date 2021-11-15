
from matrix import Matrix
from matrix import Vector

def initialize_menus():
    global main_menu
    global settings_menu
    global curr_menu
    main_menu = {"1) Input Matrix": input_matrix,"2) Edit Settings": edit_settings,"3) Exit":quit}
    settings_menu = {"1) Back": set_main_menu}
    curr_menu = main_menu

def set_main_menu():
    global curr_menu
    curr_menu = main_menu

def input_matrix():
    line = input("Please input a Matrix delimited by spaces and new lines\n")
    mat = Matrix()
    while(line != ""):
        mat.add_row(Vector([int(e) for e in line.split(" ")]))
        line = input()
    return mat

def edit_settings():
    global curr_menu
    curr_menu = settings_menu

def main():
    curr_menu = main_menu
    while True:
        print("Please select option")
        [print("  " + key) for key in curr_menu]
        curr_menu.get(input())()

    


if __name__ == "__main__":
    main()