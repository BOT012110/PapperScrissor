import random

# define the function with the game
def game():
    # player choose the pappe rock or scrissors
    player = input("[p] for papper, [s] for scrissors, [r] for rock: ")
    # computer choose the pappe rock or scrissors
    computer = random.choice(["r", "p", "s"])
    
    if player == computer:
        return "It's tie"
    
    if is_win(player, computer):
        return "You win!"
    
    # if none of statment was call the you're lost
    return "You lost!"

def is_win(player_1, computer_1):
    # all possible winners variations
    if (player_1 == "r" and computer_1 == "s") or (player_1 == "s" and computer_1 == "p") \
        or (player_1 == "p" and computer_1 == "r"):
            
        return True
# call the game method
print(game())