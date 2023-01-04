# In this code, i am printing the reverse of the number that is given as input in console

num = int(input("Enter the number"))  # User can provide the input in console
while num != 0:
    digit = num % 10
    print(digit, end="")
    num = num // 10
