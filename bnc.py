# Import the random library
from random import randint

# Define roles by using an array
roles = ["Bear", "Ninja", "Cowboy"]

# Generate a random number to pick a random element from the array
computer = roles[randint(0,2)]

player = False

while player == False:
    # Get player input
    player = input("Bear, Ninja, or Cowboy? > ")

    #print(computer, player)

    #Replace the print(computer, player) line with the following:
    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", player, "is shot by", computer)
        else: #computer is cowboy, player is ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else: #computer is bear, player is ninja
            print("You lose!", player, "is eaten by", computer)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", player, "is defeater by", computer)
        else: #computer is ninja, player is bear
            print("You win!", player, "eats", computer)

    
    player = False
    computer = roles[randint(0,2)]

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0,2)]
    else:
        break
