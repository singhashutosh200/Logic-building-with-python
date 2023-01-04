# In this code, i am adding the sum of the digits provided for the given number.
# Number type is integer.

num = int(input("Enter the number"))  # User can provide the input in console
result = 0
while num != 0:
    digit = num % 10
    result = result + digit
    num = num // 10
print('Sum of the digits of the given number is ', result)
