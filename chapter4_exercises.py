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
    
# Question 3
# Add for loop with a range. Use range number 101 equlivant to 0, 101
# Each loop, print the calculation of the range value times 10 
# Format with , separated instead of new line (default format)
for number in range(101):
    print(number * 10, end = ",")


# Programming Exercises
# Question 1 - Bug Collector
# Loop five times (1, 6) and store the number of bugs collected
# Use the augmented assignment operator to calculate the running total of bugs collected
# After the loop, print the total bugs collected
total_bugs_collected = 0
bugs_collected = 0
for day in range(1, 6):
    bugs_collected = int(input("Enter number of bugs collected: "))
    total_bugs_collected += bugs_collected
print(f'You collected a total of {total_bugs_collected} bugs.')