show_menu = True

def start_menu(): 
    print("=====")
    input_option = input("Which operation do you want to practice? \n"+
                         "1. Addition \n") 
    input_options = {
            '1': get_addition_task,
            'e': quit_program
    }
    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print("Invalid option. Please choose a valid number.")

def get_addition_task(): 
    return True

def quit_program(): 
    global show_menu
    show_menu = False
    return show_menu

while show_menu: 
    start_menu()


    
