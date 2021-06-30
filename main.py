"""
Mastermind is a two player game typically played on a wooden board with colored pegs.
This is a version that can be played in the terminal, with the computer as codemaker and a player as codebreaker.
  One player is the codebreaker and one player is the codemaker.
  The codemaker will think of a code and the codebreaker will try to break it.
  The code will consist of four colors.
  The colors may be any combination of the following:
  red, orange, yellow, green, blue, purple.
  The codebreaker will get twelve chances to break the code.
  The codemaker will tell the codebreaker if any colors guessed are in the right spot of the code with the number of white.
  The codemaker will tell the codebreaker if any colors guessed are in the code, but in a different place with the number of black.
  Enter a guess like this:
  brown brown brown brown
"""
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def pick_color():
    # Will use random to choose one color from the constant COLORS and return it.
    color = random.choice(COLORS)
    return color

def computer_pattern():
    # Will use pick_color four times to generate a pattern and return it.
    pattern = []
    for i in range(4):
        pattern.append(pick_color())
    return pattern

def proper_form(guess):
    # checks that guess contains four colors, spelled correctly
    # takes in a list and returns True or False
    if len(guess) == 4:
        for i in range(len(guess)):
            if guess[i] not in COLORS:
                return False
    else:
        return False
    return True

def get_guess():
    # Gets a string guess from the player and converts it into a list, which it returns
    guess = input("Enter your guess: ").split()
    while not proper_form(guess):
        print("Your guess was entered incorrectly. Please try again.")
        guess = input("Enter your guess: ").split()
    return guess

def check_win(guess, pattern):
    if guess == pattern:
        return True

def right_spot(guess, pattern):
    # will count how many colors from guess match the pattern.
    # Any colors that match will be removed so that they are not counted multiple times.
    # will return the number of matching colors known as white.
    white = 0
    take_out = []
    for i in range(4):
        if guess[i] == pattern[i]:
            white += 1
            take_out.append(i)
    if take_out:
        for i in range(len(take_out)):
            guess.pop(take_out[i]- i)
            pattern.pop(take_out[i]- i)
    return white

def right_color(guess, pattern):
    # takes in the guess and pattern with any matching colors removed.
    # Will return a count of colors in guess that are also in pattern, but at a different index
    # Removes the color from pattern so it is not counted multiple times
    black = 0
    for i in range(len(guess)):
        if guess[i] in pattern:
            pattern.remove(guess[i])
            black += 1
    return black

def give_feedback(guess, pattern):
    # Will compare the two patterns.
    # Will print how many colors are in the correct spot and how many are in the wrong spot.
    copy = pattern.copy()
    white = right_spot(guess, copy)
    black = right_color(guess, copy)
    print(f"Colors in correct spot: {white}")
    print(f"Colors in incorrect spot: {black}")

def codebreaker(pattern):
    guess_count = 0
    game_over = False
    while guess_count < 12 and game_over == False:
        print("")
        if guess_count == 11:
            print("This is your last guess. Make it count!")
        guess = get_guess()
        guess_count += 1
        if check_win(guess, pattern) == True:
            game_over = True
        else:
            give_feedback(guess, pattern)
    if game_over:
        # if game_over is true, player guessed the code and won. Otherwise they ran out of moves and lost.
        return "Player"
    else:
        return "Computer"

def print_rules():
    print("I will think of a pattern of 4 colors. They can be all of the same color or any combination of colors.")
    print("I will choose from the following colors:")
    print("red, orange, yellow, green, blue, and purple")
    print("Your job is to try to guess the pattern.")
    print("Please make sure you spell the colors correctly and enter each guess like this:")
    print("color color color color")
    print("If you can guess my pattern in 12 or less turns, you win! Otherwise, I win!")
    print("Goodluck!")

def start_game():
    print("Let's play Mastermind!")
    choice = input("Would you like me to tell you the rules? y/n ")
    while choice != "y" and choice != "n":
        choice = input("Please enter y for yes or n for no: ")
    if choice == "y":
        print_rules()
    else:
        print("Color choices are: " + " ".join(COLORS))
    pattern = computer_pattern()
    winner = codebreaker(pattern)
    print("")
    if winner == "Player":
        print("You win!")
    else:
        print("You lose!")
        print("The pattern was: ")
        print(" ".join(pattern))

def main():
    start_game()
    print("")
    c = input("Would you like to play again? y/n ")
    print("")
    while c :
        while c != "y" and c != "n":
            c = input("Please enter y for yes or n for no: ")
        if c == "y":
            start_game()
    print("Thanks for playing!")

if __name__ == '__main__':
    main()
