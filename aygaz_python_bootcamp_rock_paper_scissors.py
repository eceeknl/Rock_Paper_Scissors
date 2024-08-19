# -*- coding: utf-8 -*-
"""Aygaz Python Bootcamp_Rock_Paper_Scissors.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o1e-TRvfkWGwCNqpZMSTwBxA4UlH19_Q
"""

def tas_kagit_makas_ECE_KANLI():

  import random

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

  game = [rock, paper, scissors]

  print("Welcome to one of the most famous games in the world.!.")
  print("In this famous game that is with you in your most difficult moments, you are faced with the computer this time.!")
  print("Here's ROCK, PAPER and SCISSORS!!!!!!!!!!!!!!!")
  print("The rules of the game are as follows: ")
  print("1. Whoever gets 2 wins first.")
  print("2. Rock blunts scissors.")
  print("3. Paper covers rock.")
  print("4. Scissors cut paper.")
  print("5. If you do not want to play, write 'exit'.")
  print("The game starts NOW! \n")

  player_score = 0
  computer_score = 0
  game_number = 1
  round_number = 1

  game_continue = True

  while game_continue:

    print(f"#### GAME {game_number}, ROUND {round_number} #### \n")

    your_chose = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors or exit \n").lower()

    if your_chose == "exit":
      print("Then why do you want to play!!!")
      game_continue = False

    elif int(your_chose) > 2 or int(your_chose) < 0:
      print("You typed an invalid number, try again!")

    else:
      your_chose_index = print(game[int(your_chose)])

      computer_chose = random.randint(0,2)
      computer_chose_index = game[computer_chose]
      print(f"Computer chose:\n{computer_chose_index}")

      if game[int(your_chose)] == game[computer_chose]:
        print("It's a draw")

      elif (int(your_chose) == 2 and computer_chose == 1) or (int(your_chose) == 1 and computer_chose == 0) or (int(your_chose) == 0 and computer_chose == 2):
        print("You win")
        player_score += 1

      else:
        print("You lose")
        computer_score += 1

      print(f"Player = {player_score} , Computer = {computer_score}\n")

      print("###################################################### \n")

      if computer_score == 2 or player_score == 2:

        if computer_score == 2:
          print("The computer won this tour")

        else:
          print("You won this tour.")

        answer = ["yes", "no"]
        computer_answer_chose = random.randint(0,1)
        computer_answer = answer[computer_answer_chose]

        player_answer = input("Do you want to play another game? Yes/No ").lower()
        print(f"Do you want to play another game? Yes/No: {computer_answer}")

        if player_answer == computer_answer == "yes":
          print("I'm glad you're back.")
          game_continue = True

          player_score = 0
          computer_score = 0
          game_number += 1
          round_number = 1

        else:
          game_continue = False
          print("Goodbye. See you later.")

      else:
          round_number += 1

tas_kagit_makas_ECE_KANLI()