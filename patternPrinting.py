def halfPyramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()


def square(n):
    for i in range(n+1):
        for j in range(n+1):
            print("*", end="")
        print() 


def reverse_half_pyramid(n):
    for i in range(n):
        for j in range(i, n):
            print("*", end="")
        print()

number = int(input("Enter a number: "))
# halfPyramid(number)
# square(number)

reverse_half_pyramid(number)