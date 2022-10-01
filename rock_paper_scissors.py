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

#Write your code below this line 👇
import random
game_on=True
while game_on:
  player1=int(input("What is your choice ? 0 for Rock, 1 for Paper, 2 for Scissor. \n"))
  print(f"You choose {player1}")
  if player1==0:
    print(rock)
  elif player1==1:
    print(paper)
  elif player1==2:
    print(scissors)
  else:
    print("You Typed Invalid Number!")
    
  computer=random.randint(0,2)
  print(f"Computer choose {computer} ")
  if computer==0:
    print(rock)
  elif computer==1:
    print(paper)
  else:
    print(scissors)
    
  if player1==0 and computer==2:
    print("Congratulations. You won the Game!")
  elif player1==2 and computer==1:
    print("Congratulations. You won the Game!")
  elif player1==1 and computer==0:
    print("Congratulations. You won the Game!")
  elif player1==computer:
    print("It's a Draw!")
    
  else:
    if computer==0 and player1==2:
      print("You Loose. Computer won the game!")
    elif computer==2 and player1==1:
      print("You Loose. Computer won the game!")
    elif computer==1 and player1==0:
      print("You Loose. Computer won the game!")
      
  Play_on=input("Do you want to play again ? Yes or No.  ")
  if Play_on.lower()[0]=='y':
    game_on=True
  else:
    game_on=False