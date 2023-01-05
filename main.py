
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

import random

user_input = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')
user_input = int(user_input)
if (user_input>=3 or user_input<0 ):
    print("You entered invalid number")
game_data=[rock,paper,scissors]

if (user_input == 0):
    print(game_data[0])
elif (user_input== 1):
    print(game_data[1])
else:
    print(game_data)
int_rand = random.randint(0, 2)
print("Computer chose:",int_rand)
if (int_rand == 0):
    print(rock)
elif (int_rand == 1):
    print(paper)
else:
    print(scissors)

if (user_input== 0 and int_rand == 2) or (user_input == 2 and int_rand == 1) or (user_input == 1 and int_rand == 0):
    print("You win")
elif (user_input == 0 and int_rand == 0) or (user_input == 2 and int_rand == 2) or (user_input == 1 and int_rand == 1):
    print("Its a draw")
else:
    print("You lost")
