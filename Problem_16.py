"""Basic Conditions:

Write a program to check if someone is eligible for a bus pass. 
If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. 
Otherwise, they pay the full price."""

age=int(input("Enter your age: "))
if age <5:
    print("Bus pass is free")
elif age >=60:
    print("Get a senior citizen discount")
else:
    print("You pay full price")


