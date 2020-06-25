from Hangman import *

# Chance TITLE!!!
Title = '''

    ======================================================
      _  _     _     _  _    ___   __  __     _     _  _ 
     | || |   /_\   | \| |  / __| |  \/  |   /_\   | \| |
     | __ |  / _ \  | .` | | (_ | | |\/| |  / _ \  | .` |
     |_||_| /_/ \_\ |_|\_|  \___| |_|  |_| /_/ \_\ |_|\_|
                                                     
    ======================================================
    By: AfifAbroory
    Webiste: AfifAbroory.github.io
'''

Playing = 0
Win = 0
Lose = 0

print(Title)

while True:
    RandWord = RandomWord()
    HiddenWord = HideWord(RandWord)
    RandWord = ' '.join(RandWord)
    UsedLatter = []
    Indx = 0
    Chance = 7

    UserInput = AskToPlay(Playing)

    if UserInput == 'Y':
        ClearScreen()
        sleep(1)
        print('\n Let\'s Go!')
        while True:
            ASCII(Indx)

            print(' ', HiddenWord)

            UserGuess = str(input('\n(Type [1] for UserGuide), (Type [0] for Exit Program)\n >> Guess Animal Word: ')).upper()

            if IsValid(UserGuess):
                if UserGuess in UsedLatter:
                    ClearScreen()
                    print('\n Latter "{}" Already Used!'.format(UserGuess))

                elif UserGuess in RandWord:
                    ClearScreen()

                    HiddenWord = AddGuess(RandWord, UserGuess, HiddenWord)
                    AddLatter(UsedLatter, UserGuess)

                    if HiddenWord == RandWord:
                            Win += 1
                            Playing += 1

                            Result(UsedLatter, RandWord, HiddenWord, Chance = True)

                            break
                else:
                    ClearScreen()

                    Chance -= 1
                    Indx += 1

                    print('\n Latter "{}" Not In Secret!'.format(UserGuess))

                    AddLatter(UsedLatter, UserGuess)

                    if Chance == 1:
                        Playing += 1
                        Lose += 1

                        Result(UsedLatter, RandWord, HiddenWord, Chance)
                        ASCII()

                        break


            elif UserGuess == '1':
                UserGuide()

            elif UserGuess == '0':
                ExitProgram(Playing, Title, Lose, Win)

            else:
                IsValid(UserGuess, Bol = False)


    elif UserInput == 'N':
        ExitProgram(Playing, Title, Lose, Win)

    elif UserInput == '1':
        UserGuide()

    else:
        IsValid(UserInput, Bol = False)
