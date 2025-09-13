# def divideNumber(number):
    
#     try:
#         return 50 / number
#     except:
#         print("Error occured")
        


# print(divideNumber(4))
# print(divideNumber(0))
# print(divideNumber(1))

while True: 
    print("How many cats do you have?")
    cats = input();
    try:

        if int(cats) >= 4:
            print("Thats a lot of cat")
            break
        elif int(cats) < 0:
            print("Nah dude! That's negative")
        else:
            print("That's not much cats")
            break
    except:
        print("Enter a valid number")


