#First Game: Finding the absolute difference between two numbers

def difference_finder():
    print("\nThis game will find the absolute difference between two numbers.")

    while True:
        num1 = int(input("Please enter your first number here: "))
        num2 = int(input("Please enter your second number here: "))

        diff = abs(num1 - num2)

        print("The difference between {} and {} is {}.".format(num1, num2, diff))

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again == "no":
            print("Returning to menu...\n")
            break

#Game Two: Finding the remainder when the first number is divided by the second

def remainder_finder():
    print("\nThis game will help find the remainder of two numbers.")

    while True:
        num1= int(input("Please enter the first number here: "))
        num2 = int(input("Please enter the second number here: "))

        remainder = num1 % num2

        print("The remainder when {} is divided by {} is {}.".format(num1, num2, remainder))

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again == "no":
            print("Returning to menu...\n")
            break
    
#Game Three: Checking if a number is divisible by 3 and 5

def divisibility_checker():
    print("\nIn this game, you can check if a number is divisible by 3 and 5.")

    while True:
        number = int(input("Enter your number: "))

        if number % 3 == 0 and number % 5 == 0:
            print("This number is divisible by both 3 and 5.")

        else:
            print("This number is not divisible by 3 and 5.")

        play_again = input("Do you want to play again? (yes/no): ")

        if play_again == "no":
            print("Returning to menu...\n")
            break


while True:
    print("Welcome to the Math Game Menu! Make a choice between the options below to play a math game! ")
    print("1. Absolute Differences")
    print("2. Remainder Finder")
    print("3. Divisibility Checker")
    print("4. Exit")

    choice = input("Please pick between 1-4: ")

    if choice == "1":
        difference_finder()
    elif choice == "2":
        remainder_finder()
    elif choice == "3":
        divisibility_checker()
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
