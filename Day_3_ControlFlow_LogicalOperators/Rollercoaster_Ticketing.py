print("Welcome to Roller Coaster.")
height = int(input("Please enter your height in Centimeters."))

bill = 0

if height >= 120:
    print("You are eligible to ride!!!")
    age = int(input("Please enter your age. -->"))
    if age < 12:
        bill = 5
        print("Ride for Children costs $5.")
    elif age <=19:
        bill = 7
        print("Ride for Teens costs $7.")
    else:
        bill = 12
        print("Ride for Adults costs $12.")

    photo = input("Do you want a photo on Roller Coaster? Enter Y or N -->")
    if photo == "Y":
        bill += 3
    print(f"Your total cost is ${bill}. Enjoy your ride!")
else:
    print("Sorry your are not eligible to ride :(")
