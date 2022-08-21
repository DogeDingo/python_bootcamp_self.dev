import json

data = {
    "selfdev_members": [
        {
            "name": "Julio",
            "discord_name": "blazertherazer12#0001",
            "reason_to_code": "he wants to shift energy from gaming to something blazeful"
        },
        {
            "name": "oetzi",
            "discord_name": "ÖtziOfficial#5666",
            "reason_to_code": "he wants to be the best fortnite player"
        },
        {
            "name": "10act",
            "discord_name": "10act#9342",
            "reason_to_code": "he wants to trash talk others and to be a trader"
        },
        {
            "name": "Mvx",
            "discord_name": "mvxxwvll#4359",
            "reason_to_code": "he wants to get the latest gadgets and custom keyboards"
        },
        {
            "name": "Jonny",
            "discord_name": "Jonney#7007",
            "reason_to_code": "he to work at the beach in Vietnam"
        }
    ]
}

# result = json.dumps(data, indent=0)
# The dumps() function of the json module dumps a dictionary into JSON contents, and returns a JSON string.
# line 33 is not needed for this task
# print(result)

with open("selfdev_members.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
# >>> this was used to create the .json file and to import the dictionary into it
# https://moonbooks.org/Articles/How-to-save-a-dictionary-in-a-json-file-with-python-/
