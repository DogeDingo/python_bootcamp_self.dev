# normal for loop

values = ["a", "b", "c", "d"]

for value in values:
    print(value)

# >>> a
# >>> b
# >>> c

# now with the index
index = 0

for value in values:
    print(index, value)
    index += 1

# >>> 0 a
# >>> 1 b
# >>> 2 c

# nun zur enumerate() function
# Nachteil: kann immer nur einen Schritt gehen und nicht zB jedes zweites Element oder drittes

for count, value in enumerate(values):
    print(count, value)
# When you use enumerate(), the function gives you back two loop variables:
# 1. The count of the current iteration
# 2. the value of the item at the current iteration
# count and value can be named as you like

# to change the start value of the counter you can do this...:

for count, value in enumerate(values, start=1):
    print(count, value)

# >>> now it starts with 1 instead of 0
# 1 a
# 2 b
# 3 c
# 4 d

# Conditional Statements to Skip Items
# Sometimes you might need to perform an action
# on only the very first iteration of a loop, as in this example:

users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        # if the index equals 0, which is Test User in this case print the following
       print("This was added to:", user)
    print(user)
# >>>
# This was added to: Test User
# Test User
# Real User 1
# Real User 2

def even_items(iterable):
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            print(index)
            values.append(value)
    return values

testing = [1,2,3,4,5,6,7,8,9,10]
print(even_items(testing))

