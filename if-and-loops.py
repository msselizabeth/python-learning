# Operator if...else, elif...else
print("# Operator if...else and elif..else:")
age = 20
# Checking eligibility to enter in a club.
if age < 18:
    print("You are not eligible to enter.")
else:
    print("You can enter.")

# Checking type of discount
if age < 18:
    print("You can count on a 15% discount.")
elif age > 18 and age < 60:
    print("You can count on a 7% discount.")
else: 
    print("You can count on a 12% discount.")
    
# Operator while
# Write a program that asks the user for a number and increases it by 1 at each step until it reaches 12.

# If the number is 5, the program should skip this step using continue.
# If the number reaches 8, the program should terminate with break.
# At the end, the program should print a termination message (unless the exit was due to break).
print("# Operator while")
# num = int(input("Enter an integer value for a loop:"))
num = 9

while num <= 12:
    if(num == 5): 
        num += 1
        continue
  
    if num == 8:
        print("Loop interrupted at", num)
        break  
  
    print("Num is: ", num)
    num += 1
else:
    print("Increasing of value was finished.")
    
#Operator for..in, range
# Write a program that loops through the numbers from 1 to 15 (inclusive) using a for loop.
# If the number is divisible by 3, the program should skip it using continue.
# If the number is 13, the program should terminate the loop early using break.
# After the loop has completed, if it was not interrupted, the program should print a message that the loop was completed successfully.
print("#Operator for..in")
for i in range(1,16):
    if i % 3 == 0:
        continue
    if i == 14:
        break
    print("Number:", i)