# Quiz Game

# greeting our gamers



while True:
    answer = input("What does CPU stand for? ")
    if answer == "a":
        print("Correct!")
        break
    else:
        print("Incorrect!")
    play_again = input("Do you want to answer the same question again? ").lower()
    if play_again == "yes":
        continue

#
# answer = input("What does GPU stand for? ")
# def restart():
#     answer = input("What does GPU stand for? ")
#     if answer == "central processing unit":
#         print("Correct!")
#     else:
#         print("wrong answer, please try again")
#     play_again = input("Do you want to answer the same question again? ").lower()
# if play_again == "yes":
#     restart()
#
# answer = input("What does CPU stand for? ")
# if answer == "central processing unit":
#     print("Correct!")
# else:
#     print("Incorrect!")
#
#
#
# def start_game():
#
#     print("Welcome to my quiz!")
#
#     # ask the user to type something in
#     # using the input() function
#
#     playing = input("Do you want to play? ")
#     # space after ? for better visualization
#
#     if playing != "yes":
#         print("Thanks for your time. The game is now closing...")
#         quit()
#     # quit() to end the program
#
#     print("Okay! Let's play :)")
#
# if __name__ == "__name__":
#     start_game()