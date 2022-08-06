# create a list which has numbers in range from 0 to 100
# 1. Given is a list between numbers from 0 to 100 and it should be output every number in the terminal, which is divisible by 2.
my_list = []

# get numbers by using a for loop
for i in range(0, 101):
    if i % 2 == 0:
        my_list.append(i)

print(my_list)

# dies ist eine aenderung