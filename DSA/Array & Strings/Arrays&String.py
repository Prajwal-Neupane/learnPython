A = [1, 2, 3, 4, 5]
print(A)

# Append the element to the last  O(1)
A.append(6)
print(A)

# Popping the element or deleting from the end 0(1)

A.pop()
print(A)

# Insert but not to the end of the array 0(n)
A.insert(1, 10)
print(A)

# Modify an element O(1)
A[3] = 8
print(A)

# Accessing element at an index i O(1)
print(A[2])

# Checking if element is present in the array or not O(n) as we have to search through the array

if 5 in A:
    print(True)