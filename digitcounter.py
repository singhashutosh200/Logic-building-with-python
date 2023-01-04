# In this code, i am counting the digits of the given  number.

# Easy Approach
print("Number of Digits is", len(input("Enter the number")))

# Hard Approach
num = int(input('Enter the number'))  # User can provide the input in console
count = 0
while num != 0:
    count = count + 1
    num = num // 10
print("Number of Digits is", count)