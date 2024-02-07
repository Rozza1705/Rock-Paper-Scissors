import random

playing = True

values = {1: 'rock', 2: 'paper', 3: 'scissors'}
# ask for player choice
# computer choice
# compare values
# display result
# p-r,r-s,s-p


def player_choice():
    while True:
        choice = str(input('Please choose rock,paper or scissors').lower())
        if choice == 'rock':
            print('Player: ' + choice)
            return choice
        elif choice == 'paper':
            print('Player: ' + choice)
            return choice
        elif choice == 'scissors':
            print('Player: ' + choice)
            return choice
        else:
            print('Invalid choice')
            continue


def computer_choice():
    choice = values[random.randint(1, 3)]
    print('Computer: ' + choice)
    return choice


while playing:

    player = player_choice()
    computer = computer_choice()

    if player == computer:
        print('draw')
    elif player == 'rock' and computer == 'scissors':
        print('you win')
    elif player == 'paper' and computer == 'rock':
        print('you win')
    elif player == 'scissors' and computer == 'paper':
        print('you win')
    else:
        print('you lose')

    play_again = input('Play again? (y/n)')
    if not play_again == 'y':
        playing = False
