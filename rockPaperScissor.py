from random import randint
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
print("--------Virtual Rock Paper Scisssor-------\n")
print("Type\nR for Rock\nP for Paper\nS for Scissor\n")
rounds = int(input("How many rounds do you wanna play? "))
while(rounds > 0):
    user = input()
    computer = randint(0, 2)
    # R = 0
    # P = 1
    # S = 2
    if user == "R" or user == "r":
        print(rock)
        if computer == 0:
            print("Bot Chose \n" + rock)
            print("Draw")
        elif computer == 1:
            print("Bot Chose \n" + paper)
            print("You lose")
        else:
            print("Bot Chose \n" + scissors)
            print("You win!")
    elif user == "P" or user == "p":
        print(paper)
        if computer == 0:
            print("Bot Chose \n" + rock)
            print("You win!")
        elif computer == 1:
            print("Bot Chose \n" + paper)
            print("Draw")
        else:
            print("Bot Chose \n" + scissors)
            print("You lose")
    elif user == "S" or user == "s":
        print(scissors)
        if computer == 0:
            print("Bot Chose \n" + rock)
            print("You lose")
        elif computer == 1:
            print("Bot Chose \n" + paper)
            print("You win!")
        else:
            print("Bot Chose \n" + scissors)
            print("Draw")
    else:
        print("Invalid input")
    print("\n")
    rounds -= 1








