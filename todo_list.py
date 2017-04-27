"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    new_item = raw_input("What do you want to add? ")
    my_list.append(new_item)
    #ask_for_input(my_list)


def view_list(my_list):
    """Print each item in the list."""
    for item in my_list:
        print item
    #ask_for_input(my_list)

def ask_for_input(my_list):
    """Displays main options, takes in user input, and calls view or add function."""


    user_options = """
    \nWould you like to:
    A. Add a new item
    B. View list
    C. Quit the program
    >>> """
    #print user_options

    
    while True:
        # Collect input and include your if/elif/else statements here.
        print user_options
        response = raw_input("Select A, B or C: ")
        if response == "A":
            add_to_list(my_list)
        elif response == "B":
            view_list(my_list)
        else:
            break

#-------------------------------------------------

my_list = []
ask_for_input(my_list)
