
from matrix import Matrix
from vector import Vector


# Main Control Loop
def main():
    clear()
    initialize_menus()
    global curr_menu
    input_matrix()
    while True:
        print("Please select option")
        [print("  " + key) for key in curr_menu]
        curr_menu.get(list(curr_menu)[int(input())-1])()
if __name__ == "__main__":
    main()
# OUTPUT
# Prints the value currently stored in ans
def print_ans():
    global ans
    print(ans)
# MENUS
# Initializes global variables and menus
def initialize_menus():
    # MENUS
    global main_menu
    global settings_menu
    global curr_menu
    main_menu = {"1) Input Matrix": input_matrix,
    "2) Print Matrix": print_ans,
    "3) Reduced Row Echelon Form": rref,
    "4) Edit Settings": edit_settings,
    "5) Exit":quit}
    settings_menu = {"1) Back": set_main_menu,
    "2) Show Steps": flip_show_steps}
    curr_menu = main_menu
    # LINEAR ALGEBRA
    global ans
    ans = ""
    # SETTINGS 
    global show_steps
    show_steps = True
# Sets the current menu to main menu
def set_main_menu():
    global curr_menu
    global main_menu
    curr_menu = main_menu
# Sets the current menu to the settings menu
def edit_settings():
    global curr_menu
    global settings_menu
    curr_menu = settings_menu
# LINEAR ALGEBRA
# Get a matrix from user input
def input_matrix():
    global ans
    line = input("Please input a Matrix delimited by spaces and new lines\n")
    ans = Matrix()
    while(line != ""):
        ans.add_row(Vector([int(e) for e in line.split(" ")]))
        line = input()
def rref():
    global ans
    ans = ans.rref(show_steps)
# SETTINGS
def flip_show_steps():
    global show_steps
    show_steps = not show_steps
