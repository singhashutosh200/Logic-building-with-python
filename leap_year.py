#  In this code, I am checking the year is leap or not.

year = int (input("Enter the year"))   # User can provide the input in console
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is Leap Year")
else:
    print(year, "is not a Leap Year")