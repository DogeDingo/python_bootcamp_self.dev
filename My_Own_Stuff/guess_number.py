import random
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# range_specified = input("Chose a range to guess from 1 - X. What's your X? ")
# x = int(range_specified)
def guess(x):
    random_number = random.randint(1, x)
    guess = 0 # guessed number will never be 1 or higher so loop will start
    # when do we want to iterate through the loop again? whenever our guess is not equal to random number
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 - {x}: "))
        if guess > random_number:
            print("Your guess is too high")
        elif guess < random_number:
            print("Your guess is too low")

    print(f"Hoora, you won the jackpot. Your guessed number equals to the random number: {random_number}")

# guess was defined as 0 which will never equal the random number so the while loop starts
# guess of the user will be between 1 - x
# if guess == random number we break out of loop otherwise while loop starts again

# guess(x)


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"The computer has guess your number, {guess}, correctly!")

computer_guess(10)




