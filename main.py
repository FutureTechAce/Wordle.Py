import random
def print_menu():
    print("Welcome to Wordle!")
    print("Try to guess the 5-letter word in 6 attempts.")
def random_word():
    with open("words.txt") as w:
        words = w.read().splitlines()
        return random.choice(words).lower()
def print_colored_letter(letter, correct_position=False, correct_letter=False):
    if correct_position:
        print(f"\033[92m{letter}\033[0m", end="")  # Green color
    elif correct_letter:
        print(f"\033[93m{letter}\033[0m", end="")  # Yellow color
    else:
        print(letter, end="")  # Default color (grey) for incorrect letter
def give_feedback(guess, word):
    for i in range(len(guess)):
        if guess[i] == word[i]:
            print_colored_letter(guess[i], correct_position=True)
        elif guess[i] in word:
            print_colored_letter(guess[i], correct_letter=True)
        else:
            print_colored_letter(guess[i])
    print()
def play_game():
    print_menu()
    word = random_word()
    attempts_left = 6
    while attempts_left > 0:
        guess = input(f"Attempt {7 - attempts_left}: ").strip().lower()
        if len(guess) != 5 or not guess.isalpha(): #isalpha checks to see if the guess contains only letters
            print("Please enter a valid 5-letter word.")
            continue
        if guess == word:
            print("\033[92mCongratulations! You guessed the word.\033[0m")  # green color
            break
        print(end="")
        give_feedback(guess, word)
        attempts_left -= 1
    if attempts_left == 0:
        print("Sorry, you didn't guess the word. It was:", word)
if __name__ == "__main__":
    play_game()
