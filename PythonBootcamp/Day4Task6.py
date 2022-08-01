# Given an empty list "random_values", write a Python function
# called "random_value_consumer" which takes 2 parameters
# of any data type in and adds the both parameters to that list.

# Write a new function called "analyse_list_elements" which takes 1 parameter.
# The function should print the length of
# each element of that list with its value and type.

random_values = []


def append_values(a, b):
    random_values.append(a)
    random_values.append(b)


def random_value_consumer(a, b) -> list:
    append_values(a,b)
   # random_values.append(b)
    return [random_values]


# return method needs brackets of what is to returned

random_value_consumer("Jonny", 26)

print(random_values)


def analyse_list_elements(random_values):
    for x in random_values:
        p = len(str(x))
        c = type(x)
        # print(c, str(x) + " -> " + str(p))
        print(f"{c} {x} -> {p}")


analyse_list_elements(random_values)
