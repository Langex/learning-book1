import random		
HANGMAN_PICS = ['''		
	  +---+		
	      |		
	      |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	      |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	  |   |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|   |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	      |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	 /    |		
	     ===''', '''		
	  +---+		
	  O   |		
	 /|\  |		
	 / \  |		
	     ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олен орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()


def getRandomWorld(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
	print(HANGMAN_PICS[len(missedLetters)])
	print()

	print('Ошибочные буквы:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()

	blanks = '_' * len (secretWord)

	for i in range(len(secretWord)):
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

	for letter in blanks:
		print(letter, end=' ')
	print()

def getGuess(alreadyGuessed):

	while True:
		print('Введите букву.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Пожалуйста, введите одну букву.')
		elif guess in alreadyGuessed:
			print('Вы уже назвали эту букву. Назовите другую.')
		elif guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
			print('Пожалуйста, введите БУКВУ.')
		else:
			return guess

def playAgain():

	print('Хотите сыграть еще? (да или нет)')
	return input().lower().startswith('д')


print('В И С Е Л И Ц А')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
	displayBoard(missedLetters, correctLetters, secretWord)


	guess = getGuess(missedLetters + correctLetters)

	if guess in secretWord:
		correctLetters = correctLetters + guess


		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break