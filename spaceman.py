import random

#Opens word file and returns a file object in this case "r"
def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close() #Closes file

##creates a secrete word object from the wordslist
   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

#first line of code I inserted V
print(load_word()) #Test the load_word function by printing it

'''secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise'''


def is_word_guessed(secret_word, letters_guessed):
    for l in secret_word:
        if l not in letters_guessed:  #Cannot use not (!=) Because it is searching for each letter in the word
            return True
        return False

print(is_word_guessed) #some sort of test. Remove in final products

'''
secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
lettersGuessed: list of letters that have been guessed so far.
returns: string, of letters and underscores.  For letters in the word that the user has
guessed correctly, the string should contain the letter at the correct position.  For letters
in the word that the user has not yet guessed, shown an _ (underscore) instead.
'''
def get_guessed_word(secret_word, letters_guessed):
    word = ""  #Declare a variable with an empty string
    for letter in secret_word:  #Starts a for loop for letters get_guessed_word
        if letter in letters_guessed:
            word += letter + ""  # Could I rewrite this with .append?
    else:
        word += "_"
    return word

print(get_guessed_word)##some sort of test? Remove for final product

'''
lettersGuessed: list of letters that have been guessed so far
returns: string, comprised of letters that represents what letters have not
  yet been guessed.
'''
def get_available_letters(letters_guessed):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    for letter in letters_guessed: #starts a for loop
        alpha.remove(letter) #removes chosen letter from alpha list
    return alpha

print(get_available_letters)##some sort of test? Remove for final product


'''secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.'''

## User PRompt imput function
def user_input (prompt):
    user_input = input(prompt)
    return user_input

#Life Couter Function


def life(count):
    count = 0  # does this need to be changed for final product?
    if count == 7:
        print("V")
        print("O")
    if count == 6:
        print("V")
        print("O")
        print("|")
    if count == 5:
        print(" V")
        print(" O")
        print(" |")
        print("/")
    if count == 4:
        print(" V")
        print(" O")
        print(" |")
        print("/ \ ")
    if count == 3:
        print(" V")
        print(" O")
        print("-|")
        print("/ \ ")
    if count == 2:
        print("|  V  |")
        print("|  O  |")
        print("| -|- |")
        print("| / \ |")
    if count == 1:
        print("  ___   ")
        print(" /   \ ")
        print("|  V  |")
        print("|  O  |")
        print("| -|- |")
        print("| / \ |")
        print(" \___/")
    if count == 0:
        print("Ahhhhh NOoooooOoooOOo!!!!")
        print("***___***   ")
        print("**/   \**")
        print("*|  V  |*")
        print("*|  O  |*")
        print("*| -|- |*")
        print("*| / \ |*")
        print("**\___/**")
        print("*******")
        print("AIRLOCK ACTIVATED! YOU LOSE")


def spaceman(secret_word):
    secret_word_ln = len(secret_word)  #saves lenght of string to objects
    letters_guessed = []
    count = 8

#Opening Text:
    print("Welcome to the Spaceman's Airlock")
    print("I come in peace, GET ME OUT OF THIS AIRLOCK!")
    print("Please Help me hack the passcode, by guessing the letters: ")
    print("The passcode has %s charictors " % secret_word_ln)
    print("You have 7 guesses before the airlock automatically opens.")

    while is_word_guessed(secret_word, letters_guessed) == false and count > 0:
        guessed_letter = input("Guess a Letter HotShot ")
        if guessed_letter not in letters_guessed:
            letters_guessed.append(guessed_letter)
            print("So far, you have guessed:{}".format(get_available_letters(letters_guessed))) #shows word with underscores for tcorrect letters in order
            print("You are missing: {}".format(get_guessed_word(secret_word, letters_guessed)))
            #Create if statement to determine if letters are correctly

            if is_given_guess_correct(guessed_letter, secret_word):
                print("Correct!")
                life(count)
                print(count)
            else:
                print("incorrect")
                count -=1
                life(count)
                print(count)

        else:
            if count == 0:
                print("AIRLOCK ACTIVATED. NooooOOoOooOo00oooo!!! The passcode was {}".format(secret_word))
            else:
                print("Im in!! Thank you human! Take me to your leader!")


secret_word = load_word()
spaceman(load_word())
