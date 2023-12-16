
# # Loops:

# 1. for loop iterating through a list of numbers.
# 2. while loop that prints numbers from 1 to 5.
# 3. for loop iterating through characters in a string.
# 4. while loop that checks if a variable is less than 10 and increments it by 1.
# 5. Nested for loop for iterating through a 2D list.
# 6. while loop that prints even numbers between 1 and 10.
# 7. for loop iterating through keys in a dictionary.
# 8. while loop that counts down from 10 to 1.
# 9. for loop that iterates over a range with a specified step.
# 10. while loop that prints Fibonacci sequence up to a certain number.

# # If Statements:

# 1. Simple if statement checking if a number is greater than 5.
# 2. if-else statement checking if a variable is even or odd.
# 3. Nested if statements to check multiple conditions.
# 4. if-elif-else statement to determine the grade based on a score.
# 5. Checking if a string is empty using an if statement.
# 6. Using if with the in keyword to check if an element is in a list.
# 7. Checking if two variables are equal using an if statement.
# 8. if-elif ladder to compare three numbers and print the largest.
# 9. Checking if a number is positive, negative, or zero using if-elif-else.
# 10. Using if statements to check if a year is a leap year.

## Python Loops and If Statements:


# Loops:

# 1. **For loop iterating through a list:**

# numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

numbers = [5,6,7,8,9]
for number in numbers:
    print(number) #expected: [5,6,7,8,9]


# 2. **While loop printing numbers from 1 to 5:**

i = 1
while i <= 5:
    print(i)
    i += 1


# 3. **For loop iterating through characters in a string:**

text = "Hello"

for char in text:
    print(char)


# 4. **While loop checking and incrementing a variable:**

counter = 0
while counter < 10:
    print(counter)
    counter += 1


# 5. **Nested for loop for a 2D list:**

matrix = [[1, 2, 3], [4, 5, 6]]

for row in matrix:
    for element in row:
        print(element)


# 6. **While loop printing even numbers:**

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1


# 7. **For loop iterating through dictionary keys:**

data = {"name": "John", "age": 30}

for key in data:
    print(key)


# 8. **While loop counting down:**

i = 10
while i > 0:
    print(i)
    i -= 1


# 9. **For loop iterating over a range with step:**

for i in range(1, 10, 2):
    print(i)


# 10. **While loop printing Fibonacci sequence:**

a, b = 0, 1
while b <= 10:
    print(b)
    a, b = b, a + b


# **If Statements:**

# 1. **Simple if statement checking number:**

number = 6

if number > 5:
    print("Number is greater than 5")


# 2. **If-else statement for even/odd:**

number = 4

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 3. **Nested if statements for multiple conditions:**

score = 80

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")


# 4. **If-elif-else for grading:**

score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")


# 5. **Checking for empty string:**

text = ""

if not text:
    print("String is empty")


# 6. **Using in keyword for list element:**

numbers = [1, 2, 3]

if 5 in numbers:
    print("5 is in the list")


# 7. **Checking equality:**

a = 10
b = 10

if a == b:
    print("a and b are equal")


# 8. **If-elif ladder for largest number:**

num1 = 5
num2 = 7
num3 = 2

if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

print(f"Largest number: {largest}")


# 9. **Checking number sign:**

number = -1

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 10. **Checking for leap year:**

year = 2024

if year % 4 == 0 and (year % 1):
    print(year)