import random
name = input("What is your name? ")


randomNumber = random.randint(1, 30)
counter = 1

while True:
    try:
        
        if counter == 6:
            print("Timeout! Number was : " , randomNumber)
            break
        
        
        
        number = input("Hey " + name + " take a guess from (1 to 30): ")
        if int(number) > randomNumber:
            print("You're too high!")
            counter+=1
        elif int(number) < randomNumber:
            print("Your too loww")
            counter+=1
        elif int(number) == randomNumber:
            print("Your guess is correct!")
            break
    except:
        print("Enter a valid number")



