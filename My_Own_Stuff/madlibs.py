# string concatenation (verkettung) (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ______ "

youtuber = "CEO DogeDingo"

# ways to do this

print("subscribe to " + youtuber)
print(f"subscribe to {youtuber}")  # f string / cleanest way
print("subscribe to {}".format(youtuber))

adj = input("Adjective: ").lower()
verb1 = input("Verb: ").lower()
verb2 = input("Verb: ").lower()
famous_person = input("Famous person: ")

madlib = f"Python is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
# \ means to break the line and jump to the next one

print(madlib)
