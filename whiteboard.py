# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15] #you should return [10, -65].

def solution(numbers):
    count_postive = 0
    sum_negative = 0
for number in numbers:
    if number > 0:
        count_postive += 1
    elif number < 0:
        sum_negative += number
    if len(numbers) == 0:
        return []
return [count_postive, sum_negative]