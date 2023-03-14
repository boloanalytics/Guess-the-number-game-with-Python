print("Number guessing game by Bolo")
print('\n')
from random import randint
guess = 0
secret_number = randint(1, 100)
estimation = 0
name = input("Tell me your name: ")
print(f"Okay {name}, I have though of a number between 1 and 100\n"
      f"You have 8 guesses to guess.")

while guess < 8:
    estimation = int(input("What is the number? "))
    guess +=1

    if estimation < secret_number:
        print("My number is higher, please try again!")
    elif estimation > secret_number:
        print("My number is lesser, please try again!")
    else:
        print(f"Congratulations {name}, you have guessed in {guess} attempts")
if estimation != secret_number:
    print(f"Sorry, we have run out of attempts, the secret number was {secret_number}")






