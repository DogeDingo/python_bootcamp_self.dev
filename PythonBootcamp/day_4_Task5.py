# - Write a Python function with the name "en_filter" which takes one parameter and checks whether a string has no "e" and "n".
# - Use a list comprehension which loops through the previous list from task 3 (community_members) and call (use) that function in the list comprehension.
#
# If the requirements are met, extend the function "en_filter" by implementing the code to append the string variable to the new list, created by the list comprehension. Print the final list.


def en_filter(check):
    if "e" in str(check) and "n" in str(check):
        print(check + " contains the letters e and n")
    else:
        print(check + " doesn't contain both letters e and b")

en_filter("morne")
en_filter("alina")
# syntax for list comprehension
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if "a" in x]

# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
# en_filter_members = [x for x in community_members if "e" in x and "n" in x]
# print(en_filter_members)

# extending the function with list comprehension

# Example on how to loop through a list with a function
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)

def en_filter(listName):
    for x in listName:
        new_list = [x for x in listName if "e" in x and "n" in x]
    print(new_list)

community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
en_filter(community_members)

# final list printed: ['pinsaregood', 'morne']