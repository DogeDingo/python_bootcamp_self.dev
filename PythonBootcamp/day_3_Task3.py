# 3. Given is a list called community_members with names of our members (strings) in it.
# All members which have at least the letter "a" 1x in
# should be filtered and stored in a new list variable.
# Please return the total number of entries of that list.
# Please copy the list down below in the example for your  community_members.
# given is a list with community members
# sort out all member names which include the letter "a"


# for schleife
# for x in [name_liste]:
#   print(x)



community_members = ["starving", "pinsaregood", "arth", "blazertherazer", "snow", "tess", "morne", "darthtilda"]
community_members_with_letter_a = []

for i in community_members:
    if "a" in i:
        community_members_with_letter_a.append(i)

print(community_members_with_letter_a)
print(len(community_members_with_letter_a))