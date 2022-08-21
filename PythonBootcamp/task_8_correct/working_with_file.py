import json
# importing json module hehe

# task 8 B)

# with open("selfdev_members.json", "r") as f:
#     data = json.load(f)
#     for i in data["selfdev_members"]:
#         print(">>>", i["name"], "(", i["discord_name"], ") likes to learn how to program because",
#                i["reason_to_code"])

# Output:
# >>> Julio ( blazertherazer12#0001 ) likes to learn how to program because he wants to shift energy from gaming to something blazeful
# >>> oetzi ( ÖtziOfficial#5666 ) likes to learn how to program because he wants to be the best fortnite player
# >>> 10act ( 10act#9342 ) likes to learn how to program because he wants to trash talk others and to be a trader
# >>> Mvx ( mvxxwvll#4359 ) likes to learn how to program because he wants to get the latest gadgets and custom keyboards
# >>> Jonny ( Jonney#7007 ) likes to learn how to program because he to work at the beach in Vietnam

# task 8 C)


def add_key_value(chosen_key,chosen_value0,chosen_value1,chosen_value2,chosen_value3,chosen_value4):
    # new_entry = {}
    # new_entry[chosen_key] = chosen_value

    new_value_list = [chosen_value0,chosen_value1,chosen_value2,chosen_value3,chosen_value4]
    new_entry = {}
    new_dict_member = {}
    new_dict_member["selfdev_members"] = []
    with open("selfdev_members.json", "r") as f:
        data = json.load(f)
        # mit load() laedt er erstmal die .json datei und sammelt alle Daten in der Variable data
        # dadurch ist es moeglich nun durch die einzelnen dictionaries zu iterieren
        counter = 0
        for i in data["selfdev_members"]:
            # counter = 0
            test = new_value_list[counter]
            if counter <= 4:
                new_entry[chosen_key] = test
                print(new_entry)
                moduled_dict = {**i, **new_entry}
            # with line 41 you merge dictionaries together
                i.update(moduled_dict)
                # updating 2 dictionary > logic is put new dict (modu..) into old dict (i)
            # print(i)
                new_dict_member["selfdev_members"].append(i)

                counter = counter + 1
        print(new_dict_member)

    with open("selfdev_members_test.json", "w") as v:

        json.dump(new_dict_member, v, indent=3)

    # print(new_entry)

add_key_value("pc", "mac", "win", "mac", "mac", "win")