import random

if __name__ == "__main__":

    capitals_dict = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Colorado': 'Denver'
    }

    state, capital = random.choice(list(capitals_dict.items()))
    print(random.choice(list(capitals_dict.items())))

    checker = True
    while checker == True:
        answer_user = input("Whats the name of the capital from the " + state + ": \n").lower()
        if answer_user == capital.lower():
            print("That is great")
            checker = False
        else:
            print("Try again")
