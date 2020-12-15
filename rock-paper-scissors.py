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

shapes = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if choice >= 3 or choice < 0:
  print('you typed an invalid number, you lose!')
else:
  print(shapes[choice])

  computer = random.randint(0,2)
  print('computer chose:')
  print(shapes[computer])

  if choice == 0 and computer == 2:
    print('you win')
  elif computer == 0 and choice == 2:
    print('you lose')
  elif computer > choice:
    print('you lose')
  elif computer < choice:
    print('you win')
  elif computer == choice:
    print('it is a draw')
