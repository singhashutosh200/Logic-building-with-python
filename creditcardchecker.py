# preconditions are as
# if credit score falls in between 400 to 599 user can apply for Silver Credit card
# if credit score falls in between 600 to 799 user can apply for Gold Credit card
# if credit score falls in between 800 to 850 user can apply for Platinum Credit card

credit_score = int (input("Enter the Credit score"))
if credit_score < 400 or credit_score > 850:
    print("Invalid Credit Score")
else:
    if credit_score >= 400 and credit_score <= 599:
        print("User is eligible for Silver Credit card")
    elif credit_score >= 600 and credit_score < 799:
        print("User is eligible for Gold Credit card ")
    else:
         print(' User is eligible for Platinum Credit card')