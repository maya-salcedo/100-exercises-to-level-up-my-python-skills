# EXERCISE 4
#Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.Suppose the following input is
# supplied to the program.
#34,67,55,33,12,98
#Then, the output should be:

#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

my_number = input("Enter a sequence of number:")

def list_and_tuple(my_numbers):
    new_list = my_numbers.split(sep=',')
    new_tuple = tuple(new_list)
    return new_list, new_tuple

print(list_and_tuple(my_number))