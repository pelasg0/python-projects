import json
import sys

# json constants 
json_file_const = 'flashcards.json'
short_answer_type_const = 'short-answer'
multiple_choise_type_const = 'multiple-choise'
question_type_const = 'question-type'
correct_answer_const = 'correct-answer'


'''
--------- START MENU FUNCTIONS --------- 
'''

'''
Saves a flashcard

:param content:array content of the flashcard
:return: returns nothing
'''
def save_flashcard(content):
	with open(json_file_const, "w") as file:
		json.dump(content, file, indent=4)

'''
Counts and manages points

:param answer:bool answer of the question
:return: returns nothing
'''
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

		
'''
Adds a question

:return: returns nothing
'''
def add_question(): 
	content = post_topics()
	input_topic = input('Type the name of the topic: ')
	if input_topic in content:
		post_all_questions(input_topic)
		question_type = input('What question do you want to add? multiple-choise / short-answer') 
		if question_type == multiple_choise_type_const: 
			input_question = input('Enter your question here: ')
			input_first_answer = input('Enter your first answer here: ')
			input_second_answer = input('Enter your second answer here: ')
			input_third_answer = input('Enter your third answer here: ')
	
			new_entry = {"question": input_question, "option": {"A":input_first_answer, "B":input_second_answer, "C":input_third_answer}}
			content[input_topic].append(new_entry)
			save_flashcard(content)
		elif question_type == short_answer_type_const: 
			input_question = input('Enter your question here: ')
			input_answer = input('Enter your first answer here: ')

			new_entry = {"question": input_question, "answer": input_answer}
			content[input_topic].append(new_entry)
			save_flashcard(content)
	else: 
		print('Topic doesnt exist')
		start_menu()

'''
Adds a topic

:return: returns nothing
'''
def add_topic():
	content = post_topics()
	input_topic = input('Type the name of the topic you want to add: ')

'''
Function that shows the start menu

:return: returns nothing
'''
def start_menu():
	print("----------------------------------------------------------------------------------------------------")
	input_option = input("Do you want to: 🐝\n"+ 
		"1. Show all topics\n"+
		"2. Add another question \n"+
		"3. Start quiz \n"+
		"4. Quit \n"+
		" ---------------------------------------------------------------------------------------------------- \n"+
		"")
	if input_option == '1':
		post_topics()
	if input_option == '2':
		add_question()
	if input_option == '3':
		start_quiz()
	if input_option == '4':
		exit()

'''
Post topics

:return: returns content:array
'''
def post_topics(): 
	with open(json_file_const, "r") as file:
		content = json.load(file)
		json.dumps(content, indent=4)
		for i in content:
			print(i)
	return content

'''
Saves a flashcard

:param content: The name of foo
:return: returns nothing
'''
def post_all_questions(input_topic):
	with open(json_file_const, "r") as file:
		content = json.load(file)
		json.dumps(content, indent=4)
		for i in content[input_topic]:
			print(i)
	return content

'''
Starts the quiz
 
:return: returns nothing
'''
def start_quiz(): 
	content = post_topics()
	input_topic = input('Type the name of the topic: ')
	if input_topic in content:
		i = 0
		while i < len(content[input_topic]):
			if content[input_topic][i][question_type_const] == multiple_choise_type_const:
				print(content[input_topic][i]['question']) 
				print(content[input_topic][i][question_type_const])
				print(content[input_topic][i]['option'])
				input_answer = input('Answer: ')
				if input_answer == content[input_topic][i][correct_answer_const]: 
					points = manage_points(input_answer == content[input_topic][i][correct_answer_const])
					i += 1
					print(points)
				else:
					print('Wrong Answer')
			elif content[input_topic][i][question_type_const] == short_answer_type_const:
				print(content[input_topic][i]['question'])
				print(content[input_topic][i][question_type_const])
				input_answer = input('Answer: ')
				if input_answer == content[input_topic][i][correct_answer_const]: 
					points = manage_points(input_answer == content[input_topic][i][correct_answer_const])
					i += 1
					print(points)
				else:
					print('Wrong Answer')
	else: 
		print('Topic doesnt exist')
		start_menu()

'''
Stops the application

:return: returns nothing
'''
def exit(): 
	sys.exit()



'''
--------- "main method" --------- 
'''
while True: 
	start_menu()




