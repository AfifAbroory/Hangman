from random import choice
from time import sleep
from os import system, name

def RandomWord():
	ListWords = [
	'Shark', 'Sloth', 'Hamster', 'Bee', 'Monkey', 'Wolf', 'Crab', 'Lion', 'Ant', 'Camel', 'Chicken', 
	'Cheetah', 'Cow', 'Deer', 'Dog', 'Dolphin', 'Duck', 'Goat', 'Eagle', 'Seal', 'Bear', 'Spider', 
	'Hornet', 'Jaguar', 'Jellyfish', 'Parrot', 'Llama', 'Giraffe', 'Mice', 'Puma', 'Zebra', 'Rabbit', 
	'Snake', 'Fish', 'Bird', 'Tapir', 'Turtle', 'Bat', 'Wolves'
	]

	Word = choice(ListWords).upper()

	return Word

def HideWord(RandomWords):
	HideWords = '_' * len(RandomWords)
	HideWords = ' '.join(HideWords)

	return HideWords

def ASCII(Indx = 6):
	Hangman = ['''
               +---+ Chance = 6 left
               |   |
                   |
                   |
                   |
                   |
            ========''','''
               +---+ Chance = 5 left
               |   |
               o   |
                   |
                   |
                   |
            ========''','''
               +---+ Chance = 4 left
               |   |
               o   |
               |   |
                   |
                   |
            ========''','''
               +---+ Chance = 3 left
               |   |
               o   |
              /|   |
                   |
                   |
            ========''','''
               +---+ Chance 2 left
               |   |
               o   |
              /|\  |
                   |
                   |
            ========''','''
               +---+ Chance = 1 left
               |   |
               o   |
              /|\  |
              /    |
                   |
            ========''','''
              HANGED!

               +---+
               |   |
               o   |
              /|\  |
              / \  |
                   |
            ========''']

	return print(Hangman[Indx])

# Wins and Lose Change only support ASCII
def Result(UsedLatter, RandWord, HiddenWord, Chance = 1):
	Win = '''
 __   _____  _   _  __      _____ _  _ _ 
 \ \ / / _ \| | | | \ \    / /_ _| \| | |
  \ V / (_) | |_| |  \ \/\/ / | || .` |_|
   |_| \___/ \___/    \_/\_/ |___|_|\_(_)
                                         
	'''
	Lose = '''
 __   _____  _   _   _    ___  ___ ___ _ 
 \ \ / / _ \| | | | | |  / _ \/ __| __| |
  \ V / (_) | |_| | | |_| (_) \__ \ _||_|
   |_| \___/ \___/  |____\___/|___/___(_)
                                         
	'''
	if HiddenWord == RandWord:
		HiddenWord = HiddenWord.replace(' ','')

		print('\n You Guess:', HiddenWord, '\n',Win)

	elif Chance == 1:
		RandWord = RandWord.replace(' ','')

		UsedLatter = [', '.join(UsedLatter)]

		for UsedLatter in UsedLatter:
			UsedLatter = UsedLatter

		print('\n',Lose,'\n')
		print('Your Guess is: {}'.format(UsedLatter))
		print('Correct Answear is: {}'.format(RandWord))


def AddLatter(UsedLatter, UserInput):
	UsedLatter = UsedLatter.append(UserInput)

	return UsedLatter

def AddGuess(RandWord, UserGuess, HiddenWords):
	for Indx, Latter in enumerate(RandWord):
		if Latter == UserGuess:
			HiddenWords = HiddenWords[:Indx] + Latter + HiddenWords[Indx+1:]
	
	return HiddenWords

def IsValid(UserInput, Bol = True):
	if len(UserInput) == 1 and UserInput.isalpha() and Bol:
		return True

	elif UserInput == '1' and Bol:
		pass

	elif UserInput == '0' and Bol:
		pass

	elif len(UserInput) >= 1 and Bol:
		pass

	elif UserInput == '' and Bol:
		pass

	else:
		UserInput = ' Oops! Your Input "{}" Is Wrong! '.format(UserInput)
		Border = '=' * len(UserInput)

		print('\n',Border,'\n',UserInput,'\n',Border)

		sleep(1)

def ExitProgram(Playing, Title, Lose, Win):
    if Playing == 0:
        ClearScreen()
        print(Title)

        print('\n Okay, Maybe Next Time!\n\n Bye!')
        sleep(2.5)
        exit()

    elif Playing >= 1:
        ClearScreen()

        print(Title)
        # User Score
        print('''
 Thanks For Playing!

 +==========INFO===========+
 | Playing Time  :{:>8} |
 | Total Lose    :{:>8} |
 | Total Win     :{:>8} |
 +=========================+
 
 Bye!'''.format(
            Playing, Lose, Win))

        sleep(2.5)
        exit()

def UserGuide():
	ClearScreen()

	print('''
    =====User Guide=====================================================
     Rules:
         - User Only Have Chance Guessing Word 6 Times.
           If Chance is 0, User Lose.
 
         - If User Succes Guess a Hidden Word.
           User Win The Game!
 
     User Input Guide:
         - For Input Guessing Word, Input Only Accept One Latter 
           (e.g., "a", "B", "z", etc) and Alphabet Only, Except "1"
           and "0"
           for Showing User Guide and Exit Program. 
           Input is not Sensitive Case, So Upper Case or Lower Case.
           Is Same Meaning In This Program.
 
         - For Input Asking for Play, Input Only 
           Accept One Latter "Y" (YES) or "N" (NO), 
           Except "1" for Showing User Guide.
 
         - For Exit Program While in Game Type "0"
 
         - ">>" Mean Input.        
    ===================================================================''')

	sleep(2)

def ClearScreen():
    if name == 'nt':
        system('cls')

    else:
        system('clear')

def AskToPlay(Playing):
    if Playing == 0:
        UserInput = input('\n(Type [1] for User Guide)\n >> Are You Ready To Play? [Y/N]: ')

    else:

        UserInput = input('\n(Type [1] for User Guide)\n >> Play Again? [Y/N]: ')

    return str(UserInput.upper())