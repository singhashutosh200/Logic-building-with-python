# In this code, i am creating the sum of multiple of 3.
# Number type is integer.

num = int(input("Enter the number"))  # User can provide the input in console
result = 0
while num != 0:
    digit = num % 10
    if digit in [3, 6, 9]:
         result = result + digit
    num = num // 10
print("Sum of multiple of 3 as digits of the given number is ", result)
