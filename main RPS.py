import random

com_dict = {"R": "Rock", "P":"Paper", "S":"Scissors"}

def complay():
    com_player = random.choice(list(com_dict))
    return com_player


while True:

    player_input = (input("Choose between Rock as R , Paper as P and Scissors as S: ")).upper()

    complayer = complay()
    if player_input == complayer:
        print("There is a tie, Try again")
    elif player_input == "R":
        if complayer == "S":
            print("Player ROCK Beats computer  " + com_dict[complayer])
        else:
            print(f"Computer {com_dict[complayer]} beats players Rock")
    elif player_input == "P":
        if complayer == "R":
            print("Player Paper Beats computer  " + com_dict[complayer])
        else:
            print(f"Computer {com_dict[complayer]} beats players Paper")
    elif player_input == "S":
        if complayer == "P":
            print("Player Scissors Beats computer " + com_dict[complayer])
        else:
            print(f"Computer {com_dict[complayer]} beats players Scissors")
    else:
        print("Wrong Alphabet, Try either, R, P or S")


   
    try_again = input("Play again? (yes/no): ")
    if try_again.lower() != "yes":
        break
