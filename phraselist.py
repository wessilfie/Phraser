import random

phrases_list = []

def addList():
	#phrases_list = []
	again = 'y'

	while(again == 'y'):
		line = input("Please enter a phrase: ")
		phrases_list.append(line)
		again = input("Enter y to add another item or n to exit. ")
	
	end = input("Enter 1 to return to main screen or 2 to exit. ")
	
	if end == '1':
		main()
	if end == '2':
		print("Thanks for adding to the list of phrases. ")

	

def getPhrase():
	#phrases = phrases_list
	phrase_range = len(phrases_list)
	random_phrase = random.randrange(0, phrase_range)
	selected_phrase = print(phrases_list[random_phrase])

	return selected_phrase
	


def main():
	greeting = input("Please enter 1 to add to the phrases list or 2 to get a phrase: ")
	if greeting == '1':
		addList()
	else:
		getPhrase()

main()