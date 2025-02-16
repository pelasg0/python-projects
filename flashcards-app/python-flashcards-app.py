import json
import sys

json_file_const = 'flashcards.json'
short_answer_type_const = 'short-answer'
multiple_choice_type_const = 'multiple-choice'
note_type_const = 'note'
question_type_const = 'question-type'
correct_answer_const = 'correct-answer'

def manage_points(answer):
    points = 0
    if answer == True:
        points += 1 
        return points
    else:
        points -= 1
        return points
    if points < 0:
        print('Game Over')
        return points


def get_flashcard_types():

    flashcard_types = {
        multiple_choice_type_const: get_multiple_choice_input,
        short_answer_type_const: get_short_answer_input,
        note_type_const: get_note_input
    }

    return flashcard_types
       
def save_content(content):
    with open(json_file_const, "w") as file:
        json.dump(content, file, indent=4)

while True: 
    start_menu()
       
def exit(): 
    sys.exit()
    
def post_topics(): 
    with open(json_file_const, "r") as file:
        content = json.load(file)
        json.dumps(content, indent=4)
        for topic in content:
            print(topic)
    return content
       
def post_all_flashcards():
    content = post_topics()
    input_topic = input('Type the name of the topic: ').strip().lower()
    if input_topic not in content:
        print('Topic doesnt exist')
 
    with open(json_file_const, "r") as file:
        content = json.load(file)
        json.dumps(content, indent=4)
        for flashcard in content[input_topic]:
            print(f"Flashcard: {flashcard['flashcard']} \n ")
                
    return content, input_topic
    
def add_flashcard(): 

    content, input_topic = post_all_flashcards()
    flashcard_type = input('What flashlight do you want to add? multiple-choice / short-answer / note: ').strip().lower() 

    flashcard_types = get_flashcard_types() 
    
    if flashcard_type in flashcard_types: 
        content[input_topic].append(flashcard_types[flashcard_type]())
        save_content(content)
        print('Flashcard added successfully!')
        return start_menu()
    else: 
        print('Flashcard type doesnt exist')

    if input_option in input_options: 
        input_options[input_option]()
    else: 
        print('Invalid Option :/')

 
def get_multiple_choice_output(flashcard): 
    for key, value in flashcard["option"].items():
        print(f"{key}: {value}")
#Test
def determine_output_type(flashcard): 
    if flashcard["flashcard_type"] == multiple_choise: 
        get_multiple_choise_output(flashcard)
 
def start_quiz(): 
    content, input_topic = post_all_flashcards()
    flashcard_types = get_flashcard_types() 

    for flashcard in content[input_topic]:
        print("\nQuestion:", flashcard["flashcard"])
        #print("Type:", flashcard["flashcard-type"])
        if flashcard["flashcard_type"] in flashcard_types: 
            determine_output_type(flashcard)        
               
def get_multiple_choice_input():
    options = {}
    for input_option in ["A", "B", "C"]:
        options[input_option] = input(f'Enter the option for {input_option} here: ')
    return {"flashcard": input('Enter your flashcard here: '), "option": options, "correct-answer": input('Enter the correct answer here: '), "flashcard-type": "multiple-choice"}
    
def get_short_answer_input():
    return {"flashcard": input('Enter your flashcard here: '), "correct-answer": input('Enter the correct answer here: '), "flashcard-type": "short-answer"}

def get_note_input():
    note_input = input('Enter note')
    notes = []
    while note_input:
        notes.append(note_input)
        note_input = input('Enter yes/y if you want to add another note: ')
        if note_input == 'yes' or note_input == 'y': 
            note_input = True
        else: 
            note_input = False
    return {"flashcard": input('Enter your flashcard here: '), "notes": notes, "flashcard-type": "note"}

def add_topic():
    content = post_topics()
    topic_input = input('Enter a topic: ')
    if topic_input in content: 
        print('Topic already exists')
    else:
        content[topic_input] = []
        save_content(content)
        print('Topic added successfully')
           
def start_menu():
    print("----------------------------------------------------------------------------------------------------")
    input_option = input("Do you want to: 🐝\n"+ 
        "1. Show all topics\n"+
        "2. Add another flashcard \n"+
        "3. Start quiz \n"+
        "4. Add another topic \n"+
        "5. Show all flashcards \n"+
        "6. Quit \n"+
        " ---------------------------------------------------------------------------------------------------- \n"+
        "")
    input_options = {
        '1': post_topics,
        '2': add_flashcard,
        '3': start_quiz,
        '4': add_topic,
        '5': post_all_flashcards,
        '6': exit
    }
    



