import random

def play():
    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissers\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"
    # could write something like this as well but not needed:
    # if is_win(computer, user):
    #   return "You lost!"
    return "You lost!"
# r > s, s > p, p > r

def is_win(player, opponent):
    # return true if player wins
    # if (player == 'r') and (opponent == 's'):
    #     return True
    # elif (player == 's') and (opponent == 'p'):
    #     return True
    # elif (player == 'p') and (opponent == 'r'):
    #     return True
    # the whole block of code can be shortened
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

# b/c the function only has return we need to print it in order to see result
print(play())