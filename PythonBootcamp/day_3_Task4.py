# TASK 4 a)
# 4. Given is a list called "list_99" between numbers from 0 to 100. Create a new list variable and code the following case:
# a) All numbers which have a 9 as a digit like: 9, 19, 99 should be counted, multiplied by 2 and stored in a new list variable.
# a list with numbers between 0 and 100
# all numbers with the digit 9 shall be counted, multiplied by 2 and stored into a new list

# use * (called unpacking-operator) in order to create a list with range() function
list_99 = [*range(0, 101)]
print(list_99)
new_list_99 = []

for i in list_99:
    if "9" in str(i):
        p = i * 2
        new_list_99.append(p)
print(new_list_99)

# TASK 4 b)
# b) Return  (print)  the very last element of that list only.
# to display the last element of a list use [-1] of the existing list
# TIP: Negative indexing starts at the end of the list, thus array[-1] will always be the last element in the list, array[-2] the second last and so forth.
print(new_list_99[-1])


# TASK 4 extra)
# extra) All numbers which have a 7 as a digit like 7, 17, 97 should be removed from the previous list "list_99". Your goal is to get a new list without the 7's.
# with the remove() function you remove certain elements from a list
for i in list_99:
    if "7" in str(i):
        list_99.remove(i)
print(list_99)