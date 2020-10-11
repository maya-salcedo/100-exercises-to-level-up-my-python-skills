# EXERCISE 1
# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

numbers = []
for n in range(2000, 3201):
    if n % 7 == 0 and n % 5 != 0:
        numbers.append(n)

print(numbers)

# EXERCISE 2

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
from math import factorial

print(factorial(int(input('Type a number and I will return its factorial:'))))

# I know what you are thinking. But I know that factorial is a common math concept and I am pretty sure that
# it is in math module that solves the problem.

# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is supplied to the
# program: 8
#Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# EXERCISE 3

def program(number):
    dict = {}
    for i in range(1, number+1):
        dict[i] = i*i
        dict.update()
    return dict

print(program(int(input("Enter a number:"))))