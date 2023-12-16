
# Here are 3 practice problems building up to FizzBuzz, focusing on different aspects of conditional logic:

# 1. Check if a number is even or odd:

# This is a basic problem that introduces the concept of using the modulo operator (%) to check for divisibility. Write a function that takes a number as input and returns True if it's even and False if it's odd.

# Example:

def is_even(number):
  return number % 2 == 0

print(is_even(4))  # True
print(is_even(5))  # False

# 2. Check if a number is within a range:

# This introduces the concept of comparing numbers with multiple conditions. Write a function that takes a number and a range (represented by two numbers) as input and returns True if the number is within the range, False otherwise.

# Example:

def is_within_range(number, min_range, max_range):
  return number >= min_range and number <= max_range

print(is_within_range(7, 5, 10))  # True
print(is_within_range(12, 5, 10))  # False

# 3. Count the multiples of a number in a list:

# This combines the previous concepts and introduces iteration. Write a function that takes a list of numbers and a target number as input and returns the count of how many numbers in the list are multiples of the target number.

# Example:

def count_multiples(numbers, target):
  count = 0
  for number in numbers:
    if number % target == 0:
      count += 1
  return count

print(count_multiples([2, 4, 6, 8, 10], 2))  # 5
print(count_multiples([1, 3, 5, 7], 3))  # 0