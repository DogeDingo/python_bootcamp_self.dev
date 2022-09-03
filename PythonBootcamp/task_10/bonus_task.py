# task 10 bonus to train my fundamentals

words = ["its", "all", "up", "to", "you"]*10
print(f"sum: {sum(len(x) for x in words)}")
print(f"sum: {type(len(x) for x in words)}")
a = (len(x) for x in words)
print(a)
# chars = 0
# for x in words:
#     chars += len(x)
# print(f"sum: {chars}")


# Given is a list like words = ['its', 'all', 'up', 'to' ,'you']
# Write a one line code snippet which counts and prints the amount of all characters
# of all words of that given list.

text = 'Some text from your file that you have read into this variable'
print(type(text.split()))
my_list = text.split()
print(list(map(len, my_list)))
print(sorted(map(len, my_list)))

import timeit as ti

print(ti.timeit(("sum(len(x) for x in {})".format(words))))
# for each {} in string you have to add a variable in the .format()
print(ti.timeit(("sum([len(x) for x in {}])".format(words))))


# generator objects (read about it) used to save memory
