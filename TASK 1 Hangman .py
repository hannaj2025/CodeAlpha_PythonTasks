import random

words = ["python", "program", "hangman", "developer", "project"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("🎮 Welcome to Hangman!")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", ", ".join(used_letters))

    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

    if "_" not in guessed:
        print("\n🎉 You won! The word was:", word)
        break

if "_" in guessed:
    print("\n❌ You lost! The word was:", word)
