from random import choice
from time import sleep, strftime
from os import getlogin


# Hangman ASCII
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

Title = '''

    ===================================================== 

        ╦ ╦    ╔═╗    ╔╗╔    ╔═╗    ╔╦╗    ╔═╗    ╔╗╔
        ╠═╣    ╠═╣    ║║║    ║ ╦    ║║║    ╠═╣    ║║║
        ╩ ╩    ╩ ╩    ╝╚╝    ╚═╝    ╩ ╩    ╩ ╩    ╝╚╝

    =====================================================
    By: AfifAbroory
    Webiste: AfifAbroory.github.io
'''

Wins = '''
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 █ ███ ██ ▄▄▄ ██ ██ ████ ███ █▄ ▄██ ▀██ █ ██
 █▄▀▀▀▄██ ███ ██ ██ ████ █ █ ██ ███ █ █ █▄██
 ███ ████ ▀▀▀ ██▄▀▀▄████▄▀▄▀▄█▀ ▀██ ██▄ █▀██
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''

Loses = '''
 ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 █ ███ ██ ▄▄▄ ██ ██ ████ █████ ▄▄▄ ██ ▄▄▄ ██ ▄▄▄█ █
 █▄▀▀▀▄██ ███ ██ ██ ████ █████ ███ ██▄▄▄▀▀██ ▄▄▄█ █
 ███ ████ ▀▀▀ ██▄▀▀▄████ ▀▀ ██ ▀▀▀ ██ ▀▀▀ ██ ▀▀▀█▀█
 ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
'''

UserGuide = '''
   ===================================================================
    Rules:
        ■ User Only Have Cahnce Guessing Word 6 Times.
          If Chance is 0, User Lose.

        ■ If User Succes Guess a Hidden Word.
          User Win The Game!

    User Input Guide:
        ■ For Input Guessing Word, Input Only Accept One Latter 
          (e.g., "a", "B", "z", etc) and Alphabet Only, Except "1"
          and "0"
          for Showing User Guide and Exit Program. 
          Input is not Sensitive Case, So You Can Input 
          Upper Case or Lower Case.

        ■ For Input Asking for Play or Wrong Input, Input Only 
          Accept One Latter "Y" (YES) or "N" (NO) and Alphabet Only, 
          Except "1" and "0" for Showing User Guide and Exit Program.

        ■ For Exit Program While in Game Type "0"

    Program Info:
        ■ ">>" Mean Input.
        ■ Latest Win Score, Lose Score, and Time, Day, Date Playing
          Saved in Log.txt.
   ===================================================================
'''


# Global Variable
Playing = 0
Win = 0
Lose = 0
GetPcName = getlogin()
GetTime = strftime("%c")


# Random Choice Words
ListWords = ['Shark', 'Sloth', 'Hamster', 'Bee', 'Monkey', 'Wolf', 'Crab', 'Lion', 'Ant', 'Camel', 'Chicken', 'Cheetah', 'Cow', 'Deer', 'Dog', 'Dolphin', 'Duck', 'Goat', 'Eagle', 'Seal', 'Bear', 'Spider', 'Hornet', 'Jaguar', 'Jellyfish', 'Parrot', 'Llama', 'Giraffe', 'Mice', 'Puma', 'Zebra', 'Rabbit', 'Snake', 'Fish', 'Bird', 'Tapir', 'Turtle', 'Bat', 'Wolves']


print(Title)

while True:
    if Playing >= 1:
        UserInput = str(input('\n(Type [1] for User Guide)\n >> Play Again? [Y/N]: ')).upper()
    else:
        UserInput = str(input('\n(Type [1] for User Guide)\n >> Are You Ready To Play? [Y/N]: ')).upper()

    # Play The Games
    if UserInput == 'Y' and UserInput.isalpha():
        Index = 0
        Chance = 7

        print('\n Let\'s Go!\n')

        # Random Words
        RandomWords = choice(ListWords).upper()

        # Hiding Words
        HideWords = '_' * len(RandomWords)
        HideWords =  ' '.join(HideWords)

        RandomWords = ' '.join(RandomWords)

        UsedLatter = []

        while True:
            # Print Blank Words and Hangman
            print(' ', Hangman[Index])
            print('\n', HideWords)

            # Get User Input Latter Guess
            UserGuess = str(input('\n(Type [1] for User Guide), (Type [0] for Exit Program)\n >> Guess Animal Word: ').upper())

            # If UserGuess Is One Latter and Alphabet
            if len(UserGuess) == 1 and UserGuess.isalpha():
                # Message If UserGuess Latter Already Use
                if UserGuess in UsedLatter:
                    print('\n Latter "{}" Already Used!'.format(UserGuess))
                
                # If UserGuess in Random Words 
                elif UserGuess in RandomWords:
                    Indx = 0

                    # For Looping Checking Latter in RandomWords
                    for Latter in RandomWords:
                        # If Latter from RandomWords In UserGuess, Add Latter in HideWords
                        if Latter == UserGuess:
                            HideWords = HideWords[:Indx] + Latter + HideWords[Indx+1:]
                        Indx += 1
                    # Adding UserGuess UsedLatter
                    UsedLatter.append(UserGuess)

                    # Show Message and Break While Loop If All HideWords Already Used
                    if HideWords == RandomWords:
                        HideWords = HideWords.replace(' ','')
                        print('\n You Guessed: ',HideWords)
                        print('\n', Wins)
                        Win += 1
                        Playing += 1
                        break

                # Show Message Latter Not In Secret Word and Adding UserGuess latter in UsedLatter if UserGuess not in RandomWords, and Incerment Index for ASCII Art (Hangman) also Decerment Chance User.
                else:
                    UsedLatter.append(UserGuess)
                    print('\n Latter "{}" Not In Secret Word!'.format(UserGuess))
                    Chance -= 1
                    Index += 1

                    # If Chance Is Equal 1 Show Message Lose and break While Loop
                    if Chance == 1:
                        print(' ', Hangman[6])
                        print('\n',Loses,'\n')

                        UsedLatter = [', '.join(UsedLatter)]

                        # Convert List to String
                        for UsedLatter in UsedLatter:
                            UsedLatter = UsedLatter

                        # Remove Space
                        RandomWords = RandomWords.replace(' ','')

                        print('Your Guess is: {}'.format(UsedLatter))
                        print('Correct Answear is: {}'.format(RandomWords))
                        Lose += 1
                        Playing += 1
                        break

            # Message if User Input not Alphabet and UserGuess len > 1
            else:
                if UserGuess == '1':
                    print(UserGuide)

                # Exit Program While In Game
                elif UserGuess == '0':
                    print('\n Thanks For Playing!')

                    # User Score
                    ScoreInfo = '''
    +==========INFO===========+
    | Playing Time  :{:>8} |
    | Total Lose    :{:>8} |
    | Total Win     :{:>8} |
    +=========================+'''.format(Playing, Lose, Win)

                    with open('Log.txt', 'w') as f:
                        print(ScoreInfo, file=f)
                        print('\nPC-NAME: {} - {}'.format(GetPcName, GetTime), file=f)
                    print(ScoreInfo)

                    sleep(2.5)

                    exit()

                else:
                    UserGuess = ' Oops! Your Input "{}" Is Wrong! '.format(UserGuess)
                    Border = "=" * len(UserGuess)
                    print('\n',Border,'\n',UserGuess,'\n',Border)

    # Exit Prorgam
    elif UserInput == 'N' and UserInput.isalpha():
        # Message If User Not Playing Before
        if Playing == 0:
            print('\n Okay, Maybe Next Time!')
            sleep(1.5)

            break

        # Message If User Already Playing Games
        else:
            print('\n Thanks For Playing!')

            # User Score
            ScoreInfo = '''
    +==========INFO===========+
    | Playing Time  :{:>8} |
    | Total Lose    :{:>8} |
    | Total Win     :{:>8} |
    +=========================+'''.format(Playing, Lose, Win)
            with open('Log.txt', 'w') as f:
                print(ScoreInfo, file=f)
                print('\nPC-NAME: {} - {}'.format(GetPcName, GetTime), file=f)
            print(ScoreInfo)

            sleep(2.5)

            break

    # Message If UserInput Not 'Y', 'N', or Not Alphabet
    else:
        # Show User Guide
        if UserInput == '1':
            print(UserGuide)

        else: 
            UserInput = ' Oops! Your Input "{}" Is Wrong! '.format(UserInput)
            Border = '=' * len(UserInput)
            print('\n',Border,'\n',UserInput,'\n',Border)