import random


class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


with open("words.txt", "r", encoding="utf-8") as f:
    file_contents = f.read()
    words = file_contents.split("\n")

correct_word = random.choice(words)
# print(colour.GREEN + correct_word + colour.END)

num_guesses = 0

win = False

total_guesses = 7
total_letters = 5


def laziness(g, letter, position):
    for pos, l in enumerate(g):

        if l == correct_word[pos] == letter:
            return False

        if pos >= position + 1:
            if l == letter:
                return False
    return True


while num_guesses < total_guesses:
    if num_guesses == 1:
        guess = input(f"Enter a {total_letters} letter word ({total_guesses - num_guesses} guess left): ")
    else:
        guess = input(f"Enter a {total_letters} letter word ({total_guesses - num_guesses} guesses left): ")
    guess = guess[:total_letters]
    guess = guess.lower()
    if guess in words:
        num_guesses += 1
        if guess == correct_word:
            win = True
            break
        else:
            for position, letter in enumerate(guess):
                if letter in correct_word:
                    if correct_word[position] == letter:
                        print(colour.GREEN + letter + colour.END, end="")
                    elif guess.count(letter) > correct_word.count(letter):
                        if not laziness(guess, letter, position):
                            print(letter, end="")
                        else:
                            print(colour.YELLOW + letter + colour.END, end="")
                    else:
                        print(colour.YELLOW + letter + colour.END, end="")

                else:
                    print(letter, end="")
            print()
    else:
        print(guess, "is not a word!")

if win:
    if num_guesses == 1:
        print(
            colour.GREEN + colour.BOLD + f"Congratulations, you won the game!\nIt took you {num_guesses} try." + colour.END)
    else:
        print(
            colour.GREEN + colour.BOLD + f"Congratulations, you won the game!\nIt took you {num_guesses} tries." + colour.END)
else:
    print(colour.RED + colour.BOLD + f"You lost! Better luck next time.\nThe word was {correct_word}." + colour.END)
