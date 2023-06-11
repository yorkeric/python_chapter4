# Algorithm Workbench
# Question 2
# Set iterator with inital value of y and loop until user sets value to n
# Prompt user for two values and print the sum
# Prompt user to try again. y will loop again and n will stop loop
keep_going = 'y'
while keep_going == 'y':
    firstNumber = int(input("Enter a number: "))
    secondNumber = int(input("Enter a number: "))
    print("The sum of the two numbers is", (firstNumber + secondNumber))
    keep_going = input("Do you want to try again? y or n: ")
