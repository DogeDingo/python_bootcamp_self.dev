import json
from datetime import datetime

today = datetime.today()

# member_list = {}
# with open("selfdev_members.json", "r") as f:
#     data = json.load(f)
#     for x in data:
#         entry = x
#         # for key, value in entry.items():
#         #     print(key, ": ", value)
#         print(">>>", entry["name"], "(", entry["discord_name"], ") likes to learn how to program because",
#               entry["reason_to_code"])

def add_key(chosen_key, chosen_value,chosen_member):
    today = datetime.today()
    new_list = []
    temp_dict = {}
    temp_dict[str(chosen_key)] = str(chosen_value)
    with open("selfdev_members.json", "r") as f:
        data = json.load(f)
        for x in data:
            new_list.append(x)
        moduled_list = {**new_list[chosen_member], **temp_dict}
        dict_of_member = new_list[chosen_member]
        name_of_member = dict_of_member.get("name")
        # why can"t I use dict_of_member["name"] here?


        with open("selfdev_members_enriched.json", "a") as v:
            v.write(">>> New changes were made on " + str(today) + "\n")
            v.write(">>> KEY: " + str(chosen_key) + " and VALUE: " + str(chosen_value) + " were added to member: " +
                    name_of_member + "\n")
            v.write("{" + "\n")
            for key, value in moduled_list.items():
                print(key + ": " + value)
                v.write("'" + key + "'" + ": " + "'" + value + "'" + "\n")
            v.write("}" + "\n")
            # v.write(str(moduled_list) + "\n")


add_key("pc", "mac",1)




