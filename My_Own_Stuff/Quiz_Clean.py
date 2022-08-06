def quiz_start():
    print("Hello to my quiz")
    answer = input("Do you want to play my game? ").lower()
    if answer == "yes":
        print("Okay let's go!")
    elif answer != "yes":
        print("Thanks for playing! Have a wonderful day")
        quit()


quiz_start()

while True:
    print("Which difficulty do you dare to play?")
    answer = input("Easy: 1, Medium: 2, Hard: 3").lower()
    if answer == "1":
        answer2 = input("You have chosen: Easy difficulty. Are you sure and want to proceed?").lower()
        if answer2 == "yes":
            print("Okay let's do this")
            x = "1"
            break
        else:
            print("Okay let's chose another difficulty")
            continue

    if answer == "2":
        answer2 = input("You have chosen: Medium difficulty. Are you sure and want to proceed?").lower()
        if answer2 == "yes":
            print("Okay let's do this")
            x = "2"
            break
        else:
            print("Okay let's chose another difficulty")
            continue

    if answer == "3":
        answer2 = input("You have chosen: Hard difficulty. Are you sure and want to proceed?").lower()
        if answer2 == "yes":
            print("Okay let's do this")
            x = "3"
            break
        else:
            print("Okay let's chose another difficulty")
            continue


def quiz_easy():
    user_score = 0
    question1 = input("What's 1 + 1? (Numbers only)")
    if question1 != "2":
        print("Wrong answer! We will continue with the next question")
    else:
        print("That's the right answer! You are a math genius")
        user_score += 1

    question2 = input("What's 2 + 2? (Numbers only")
    if question2 != "4":
        print("Wrong answer!")
    else:
        print("That's the right answer! You are the best")
        user_score += 1
    print("The game is over here. Your score is:")
    return print(user_score)


def quiz_medium():
    f = open("test.txt", "r") #lower case r for reading, w writing, a appending, r+ for reading and writing

    print(f.read())

    f.close() # have to close the file


def quiz_difficulty(x):
    if x == "1":
        print("The quiz will be in Easy Mode")
        quiz_easy()
    elif x == "2":
        print("The quiz will be in Medium Mode")
        quiz_medium()
    elif x == "3":
        print("The quiz will be in Hard Mode")
        # quiz_hard()

quiz_difficulty(x)

#small changes

