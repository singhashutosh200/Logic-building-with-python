# In this code, i am printing the Even or Odd number as per the given number

num = int (input ("Enter the number"))  # User can provide the input in console
if num <= 0:
    print(num, "is Invalid")
else:
    if num % 2 ==0:
        print( num, " is Even Number")
    else:
        print(num, " is Odd Number")
