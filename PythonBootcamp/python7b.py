my_list = ["strawberry", "apple", "pineapple", "rasberry", "lemon"]

def save_list_into_file(my_list):
    for x in my_list:
        my_first_saved_list = [x for x in my_list if "a" in x and "r" in x]
    print(my_first_saved_list)
    return my_first_saved_list

my_first_saved_list = save_list_into_file(my_list)
print(my_first_saved_list)

with open ("my_first_saved_list1.txt", "w") as f:
    f.write(str(my_first_saved_list))
    # for x in my_first_saved_list:
    #     if x != x[-1]:
    #         f.write(x + ", ")
    #     elif x == x[-1]:
    #         f.write(x)
    # f.write("]")

