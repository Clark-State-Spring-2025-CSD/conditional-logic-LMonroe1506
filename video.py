#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

print("Welcome to the Menu Ordering System")

CustomerAge = int(input("Please enter your age: "))

price = 0

if CustomerAge <= 10:
    price = 8
elif CustomerAge >= 62:
    price = 9 
#else:
#    price = 12

print(f"The cost of your ticket is: ${price}")

drinkYesNo = input("Add a dringk? (Y/N): ")

if drinkYesNo == "Y":
    smallLarge == "S":
    if smallLarge == "S":
        price += 1
    else:
        price += 2

print(f"Total is: ${price}")