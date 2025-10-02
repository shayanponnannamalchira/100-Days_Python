#conditional statements
#voting age
age=int(input("What us your age?"))
if age>=18:
    print("You are eligible to vote")
elif age<=17:
    print("You are not eligible to vote")
else:
    print("Invalid input")