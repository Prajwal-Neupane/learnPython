array = [-5, -4, -2, 0, 1, 3, 4, 5, 7, 8, 9]

# target = 3

# import sys




# left = 0
# right = len(array) - 1

# while left <= right:
#     mid = (left+right) // 2
    
    
#     if array[mid] == target:
#         print("Found the number: " , target)
#         # sys.exit()
#         break
#     elif array[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
        
# print("Not found")


#Traditional Approach
def binary_search(array, target):
    left = 0
    right = len(array) - 1
    
    while left<=right:
        mid = (left+right) // 2  #This is traditional approach
        mid = left + (right - left) // 2  #This is to overcome the integer overflow problem
        
        if array[mid] == target:
            return ("Found the number", target)
        
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"



#Condition-based Approach


def binary_search_condition(array, target):
    N = len(array)
    L = 0
    R = N - 1
    
    while L < R:
        M = (L+R) // 2
        
        if array[M] < target:
            L = M+1
        else:
            R = M
    return L
    

    
# print(binary_search([-5, -4, -2, 0, 1, 3, 4, 5, 7, 8, 9], 1))

idx = binary_search_condition(array, 5)
# print(received)

if (idx < len(array) and array[idx] == 5):
    print("Found at index: ", idx)
    
else:
    print("Not found")