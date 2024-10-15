import random

print("BINE AI VENIT")
print("-------------------------------------------")
print("Reguli: Poti gresi de 6 ori, Foloseste doar litere mari!")

wordDictionary = ["ICONOGRAFĂ", "FAGOCITUL", "APICOLILOR", "HIPOPLAZII", "PROHODI", "CIOPLEA", "COVÂRȘITELOR",
                  "PÂRGUIRILE", "BURGHIERILE"]

randomWord = random.choice(wordDictionary)

for x in randomWord:
    print("_", end=" ")


def print_hangman(wrong):
    if (wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 1):
        print("\n+---+", "   5 incercari ramase")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif (wrong == 2):
        print("\n+---+", "   4 incercari ramase")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif (wrong == 3):
        print("\n+---+", "   3 incercari ramase")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif (wrong == 4):
        print("\n+---+", "   2 incercari ramase")
        print(" O  |")
        print("/|/ |")
        print("    |")
        print("   ===")
    elif (wrong == 5):
        print("\n+---+", "   Ultima incercare!")
        print(" O  |")
        print("/|/ |")
        print("/   |")
        print("   ===")
    elif (wrong == 6):
        print("\n+---+", )
        print(" O   |")
        print("/|/  |")
        print("/ /  |")
        print("    ===")


def printWord(guessedLetters):
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if (char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters


def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while (amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLitere incercate pana acum: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    ### Prompt user for input
    letterGuessed = input("\nGhiceste litera: ")
    ### User is right
    if letterGuessed in randomWord:
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_guess_index += 1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()

    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letterGuessed)
        ### Update la pictura
        print_hangman(amount_of_times_wrong)
        ### Print cuvant
        current_letters_right = printWord(current_letters_guessed)
        printLines()

print("    Game Over! ")