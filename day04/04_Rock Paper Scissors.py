rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
import random
choice_player = int(input("Whats your choice? (0 - rock), (1 - paper) or (2 - scissors)"))
choice_com = random.randint (0, 2)

if choice_player >= 3 or choice_player < 0:
    print("type invalid")
else:
    print("You choice:")
    print(game_images[choice_player])

    print("Com choice:")
    print(game_images[choice_com])

    if choice_player == 0 and choice_com == 2:
        print("You win!")
    elif choice_com == 0 and choice_player == 2:
        print("you lose!")
    elif choice_com > choice_player:
        print("You lose")
    elif choice_player > choice_com:
        print("you win!")
    elif choice_player == choice_com:
        print("Its draw!")
