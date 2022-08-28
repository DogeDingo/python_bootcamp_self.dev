# list_dict = [{"name": "long"},
#              {"name": "jonney"},
#              {"name": "10act"}]
#
# new_properties = ["number_one","number_two","number_zree"]
#
# for index_counter,x in enumerate(list_dict):
#     x['new_property'] = new_properties[index_counter]
#
# print(list_dict)
# def test(x):
#     if x % 2 == True:
#         return "rest ist true"
#     else:
#         return "kein rest ist false"
#
# print(test(4))

liste = [1,2,3,4,1,2,5,5,1,1,1]
counter = 0
for x in liste:
    if x == 1:
        counter += 1
print(counter)