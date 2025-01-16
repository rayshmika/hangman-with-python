import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Your guess '{guess}' is incorrect! You lose a life!")
        if lives == 0:
            game_over = True
            print(f"***************The correct word is {chosen_word}. YOU LOSE**************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    stages = hangman_art.stages
    if not game_over:
        print(stages[lives])
