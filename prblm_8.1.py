import random


# core function of game


def game(user1):
    if user1 == 'rock' and cpu == 'paper':
        print("Cpu wins!")
    elif user1 == 'rock' and cpu == 'scissor':
        print("u1 wins!")
    elif user1 == 'paper' and cpu == 'scissor':
        print("Cpu wins!")
    else:
        print("DRAW!")
    return 0


moves = ['rock', 'scissor', 'paper']
choice = ''
while choice != 'q':
    u1 = input("What is your move?:")  # ask for choice from the user
    cpu = random.choice(moves)
    game(u1)
    choice = input("press q to exit and c to continue:")
