import random
import sys
import turtle


def main():
    #Player number, word to be guesses, define previously guessed word and lives
    players = welcome()
    word = instructions(players).upper()
    lettersGuess = [" "]
    lives = 6
    pen, screen = turtle_setup()
    #Print hidden word
    print(fill_letter(word, lettersGuess))
    #Print/format previous guesses
    while True:
        if len(lettersGuess) > 1:
            print("\nLetters Guessed:", end="")
            for i in range(len(lettersGuess)):
                print(f"{lettersGuess[i]}", end='|')
        #Prompt letter guess, append to list
        letter = guess(lettersGuess)
        lettersGuess.append(letter)
        #Calculate if letter is correct, subtract life based on result
        lives, subtractLives = subtract_lives(letter, word, lives)
        #If life lost, draw hagman
        if subtractLives == True:
            drawing_body(pen, lives)
        #Reveal correct letters guesses and print lives/word
        result = (fill_letter(word, lettersGuess))
        print(f"Lives Remaining: {lives}")
        print(result)
        #End game if all letters revealed or lives = 0
        if "_" not in result:
            print("\nCongratulations! You win!")
            break
        elif lives == 0:
            print("\nSorry, You Lose!")
            break
    #screen.mainloop()
    sys.exit(0)
def welcome():
    #Prompts # of players
    print("Welcome to Hangman!")
    while True:
        try:
            player = input("How many players will there be? (Enter 1 or 2): ")
            if int(player) not in [1, 2]:
                raise ValueError
            return int(player)
        except ValueError:
            print("\nInvalid input!")

def instructions(x):
    #Explains instructions, if 1 player, use wordbank, if 2 prompts for word
    if x == 1:
        print("\nYou chose 1 player.\nYou have 6 lives to guess the word.\nThe word will randomly be selected from a word bank.")
        wordbank = ["Algorithm", "Quantum Computing", "Database", "Cybersecurity", "Machine Learning"]
        return random.choice(wordbank)
    elif x == 2:
        print("\nYou chose 2 players.\nPlayer 1 will enter a word or phrase for Player 2 to guess.\nPlayer 2 will have 6 lives to guess the word.")
        while True:
            try:
                word = input("Player 1 please enter a word or phrase. Only include English letters and spaces: ").upper()
                for char in word:
                    if not char.isalpha() and not char.isspace():
                       raise ValueError
                return word
            except ValueError:
                print("\nInvalid input!")

def guess(letterGuess):
    #Prompts for letter
    while True:
        try:
            letter = input("\nGuess a letter: ").upper()
            if not letter.isalpha() or len(letter) != 1:
                print("Invalid Input")
                raise ValueError
            elif letter in letterGuess:
                print("Letter Already Guessed")
                raise ValueError
            else:
                return letter
        except ValueError:
            pass

def subtract_lives(letter, word, lives):
    if letter not in word:
        print(f"\nSorry, {letter} is incorrect!")
        subtract = True
        return (lives-1), subtract
    else:
        print(f"\n{letter} is correct!")
        subtract = False
        return lives, subtract

def fill_letter(word, lettersGuess):
    #Loop through "word" and matched letters in "lettersGuess"
    blankWord = ""
    for char in word:
        if char in lettersGuess:
            blankWord += char
        else:
            blankWord += "_"
    return blankWord

def turtle_setup():
    #Define turtle and screen, screen topmost
    screen = turtle.Screen()
    screen.title("Hangman")
    pen = turtle.Turtle()
    pen.hideturtle()
    turtle_start(pen, screen)
    root = screen.getcanvas().winfo_toplevel()
    root.attributes("-topmost", True)
    return pen, screen


def drawing_body(pen, lives):
    if lives == 5:
        turtle_head(pen)
    if lives == 4:
        turtle_body(pen)
    if lives == 3:
        turtle_leftarm(pen)
    if lives == 2:
        turtle_rightarm(pen)
    if lives == 1:
        turtle_leftleg(pen)
    if lives == 0:
        turtle_rightleg(pen)

def turtle_start(pen, screen):
    # Move turtle to top and draw straight line down
    pen.speed(10)
    pen.up()
    pen.width(5)
    pen.setpos(0, 400)
    pen.right(90)
    pen.down()
    pen.forward(100)


def turtle_head(pen):
    pen.right(90)
    pen.circle(50)

def turtle_body(pen):
    pen.up()
    pen.left(90)
    pen.forward(100)
    pen.down()
    pen.forward(200)

def turtle_leftarm(pen):
    pen.up()
    pen.right(180)
    pen.forward(150)
    pen.left(135)
    pen.down()
    pen.forward(100)

def turtle_rightarm(pen):
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.right(90)
    pen.down()
    pen.forward(100)

def turtle_leftleg(pen):
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.left(135)
    pen.forward(150)
    pen.right(45)
    pen.down()
    pen.forward(100)

def turtle_rightleg(pen):
    pen.up()
    pen.right(180)
    pen.forward(100)
    pen.right(90)
    pen.down()
    pen.forward(100)



main()