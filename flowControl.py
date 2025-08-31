import random

# number = int(input("Enter a number: "))

randomNumber = random.randint(1, 100)

while True:
    guess = int(input("Enter a number: "))
    if guess < randomNumber:
        print("Little Low")
    elif guess > randomNumber:
        print("Too High")
    elif guess == randomNumber:
        print("You guess correct!!")
        break