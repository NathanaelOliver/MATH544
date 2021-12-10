
from matrix import Matrix
from vector import Vector


# OUTPUT

def print_ans():
    # Prints the value currently stored in ans
    global ans
    print(ans)


# MENUS

def initialize_menus():
    # Initializes global variables and menus
    # MENUS
    global main_menu
    global settings_menu
    global curr_menu
    main_menu = {"1) Input Matrix": input_matrix,
                 "2) Print Matrix": print_ans,
                 "3) Reduced Row Echelon Form": rref,
                 "4) Gaussian Elimination": gaussian_elimination,
                 "5) Edit Settings": edit_settings,
                 "6) Exit": quit}
    settings_menu = {"1) Back": set_main_menu,
                     "2) Show Steps": flip_show_steps}
    curr_menu = main_menu
    # LINEAR ALGEBRA
    global ans
    ans = ""
    # SETTINGS
    global show_steps
    show_steps = True


def set_main_menu():
    # Sets the current menu to the main menu
    global curr_menu
    global main_menu
    curr_menu = main_menu


def edit_settings():
    # Sets the current menu to the settings menu
    global curr_menu
    global settings_menu
    curr_menu = settings_menu

# LINEAR ALGEBRA


def input_matrix():
    # Get a matrix from user input
    global ans
    line = input(
        "Please input a Matrix delimited by spaces or pipes and new lines\n")
    ans = Matrix()
    while(line != ""):
        arr = []
        if "|" in line:
            [ans.add_partition(i+11) for i, val in enumerate("".join(
                filter(lambda x: x in set(" |"), line))) if val == "|"]
        arr = [int(e) for e in line.replace("|", " ").split(" ")]
        ans.add_row(Vector(arr))
        line = input()


def rref():
    # Puts the matrix stored in ans into reduced row echelon form
    global ans
    ans = ans.rref(ans.row_length, show_steps)


def gaussian_elimination():
    # Performs Gaussian Elimination on the stored matrix
    global ans
    ans.add_partition(ans.row_length - 1)
    ans = ans.ref(ans.row_length - 1, show_steps)

# SETTINGS


def flip_show_steps():
    # Changes the settings for show steps
    global show_steps
    show_steps = not show_steps

# Main Control Loop


def main():
    initialize_menus()
    global curr_menu
    input_matrix()
    while True:
        print("Please select option")
        [print("  " + key) for key in curr_menu]
        curr_menu.get(list(curr_menu)[int(input())-1])()


if __name__ == "__main__":
    main()
