# program 1

birthYear = [1989, 1990, 1991, 1992]
ages = []
for x in range(len(birthYear)):
    print(x) # 0 1 2 3
    print(birthYear[x])     # Print the birth year
    print(2023 - birthYear[x])
    x = 2023 - birthYear[x] # Update the loop variable x with the calculated age
    ages.append(x) # Append the age to the ages list
print(ages)# Print the list of ages 34  33 2

# program 2
#
#
marks = [34, 55, 66, 7, 2, 44, 55, 66, 99, 77]

above50 = [] # Empty list to store marks above 5

# Loop through each element in the marks list
for item in marks:
    # Check if the mark is above 50
    if item > 50:
        # Append the mark to the above50 list
        above50.append(item)

# Print the list of marks above 50
print(above50)  #55 66 55 66 99 77



#
# # program 3


totals = [11, 22, 33]
# Variable to store the sum
sum = 0
# Loop through each element in the totals list
for item in totals:
    # Add the item to the sum
    sum = sum + item
# Print the sum
print(sum) #66
#
#
# # program 4
#
#
# cities = ["ahemdabad", "banglore", "chennai"]
#
# # Loop through each element in the cities list
# for item in cities:
#     # Print a welcome message for each city
#     print("welcome " + item)
#
