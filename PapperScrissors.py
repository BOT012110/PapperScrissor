import random


def game():
    player = input("[p] for papper, [s] for scrissors, [r] for rock: ")
    computer = random.choice(["r", "p", "s"])
    
    if player == computer:
        return "It's tie"

    if is_win(player, computer):
        return "You win!"
    
    return "You lost!"

def is_win(player_1, computer_1):
    if (player_1 == "r" and computer_1 == "s") or (player_1 == "s" and computer_1 == "p") \
        or (player_1 == "p" and computer_1 == "r"):
            
        return True

print(game())