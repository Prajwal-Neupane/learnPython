def printFn(s): 
    print(s)

    
# print("Hello World" + str(printFn("something")))


# Print patterns


n = int(input("Enter a number: "))

for i in range(n+1):
    for j in range(i):
        print("*", end="")
    print()
    
        