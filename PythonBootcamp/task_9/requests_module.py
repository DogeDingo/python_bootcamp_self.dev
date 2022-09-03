# task 9 C)
import requests
from project_config import URL, c

r = requests.get(URL)

print(r.text)
# line 6 prints the html source code

# dir(r) shows us what methods we can use from the webpage
# help(r) shows us what the methods stand for and what they do
# for example we want to get the html source code so we have to use print(r.text)
# _____________________________________________________________________________________
# now create a new file and save the source into a new file

# with open("apple_homepage_html.txt", "w") as f:
#     f.write(r.text)

# ^^^^^^^^ was used to create .txt file with html source code
# _____________________________________________________________________________________

# Task 9 D)
# if you need help: https://stackoverflow.com/questions/31671685/iterating-over-lines-in-a-file-python
with open("apple_homepage_html.txt", "r") as f:
    text = f.read()
    # counter = 0
    # for line in text:
    #     if line == "e" or line == "E":
    #         counter += 1
    # print(counter)

    letter_count = text.lower().count("e")
    print(f" The letter e appears {letter_count} times in the source code")

    single_word = text.split()
    counter = 0
    for word in single_word:
        if word == "<p>":
            counter += 1
    print(f" The word <p> appears {counter} times in the source code")


