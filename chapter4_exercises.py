# Algorithm Workbench

# Question 2
# Set iterator with inital value of y and loop until user sets value to n
# Prompt user for two values and print the sum
# Prompt user to try again. y will loop again and n will stop loop
keep_going = 'y'
while keep_going == 'y':
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a number: "))
    print("The sum of the two numbers is", (first_number + second_number))
    keep_going = input("Do you want to try again? y or n: ")

# Question 3
# Add for loop with a range. Use range number 101 equlivant to 0, 101
# Each loop, print the calculation of the range value times 10
# Format with , separated instead of new line (default format)
for number in range(101):
    print(number * 10, end=",")


# Programming Exercises
# Question 1 - Bug Collector
# Loop five times (1, 6) and store the number of bugs collected
# Use the augmented assignment operator to calculate the running total of bugs collected
# After the loop, print the total bugs collected
total_bugs_collected = 0
for day in range(1, 6):
    total_bugs_collected += int(input("Enter number of bugs collected on day " + str(day) + ": "))
print(f'You collected a total of {total_bugs_collected} bugs.')

## Question 4 - Distance Traveled
# Prompt the user for the speed and hours traveled
# Print the table header before the loop
# Loop for each hour and calcuate the speed multipled by that hour value
# Print the hour value and the total distance based on the spped multipled by the hour
speed = int(input("What is the speed of the vehicle in mph? "))
hours = int(input("How many hours has it traveled? "))
print("Hour     Distance Traveled")
print("----------------------------")
for hour in range(1, hours + 1):
    print(str(hour) + "        " + str((speed * hour)))
    
# Question 11 - Weight Loss
# Prompt the user for their starting weight
# Loop over each month, or 6 months, and subtract 4 pounds from their weight
# Print their projected weight for each month in the loop
weight = int(input("Enter your starting weight in pounds: "))
for month in range(1, 7):
    weight -= 4
    print(f'Projected weight after month {month} is {weight} pounds')

# Question 14 - Print pattern
# There are a total of 7 lines
# The pattern starts off with 7 asterisks on first line, 6 on second line, 5 on third line, etc
# Loop over 7 times and staring with 7 asterisks, and each iteration reduce the number or astericks by one.
for line in range(8, 1, -1):
    output = ""
    for symbol in range (line - 1):
        output += "*"
    print(output)