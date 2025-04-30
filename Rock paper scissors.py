import random
options = ["Rock , Paper , Scissors"]
user_choice = input("Choose Rock, Paper, or Scissors")
computor_choice = random.choice(options)
print("Your choice: ", user_choice)
print("The computer chose: ", computor_choice)
if user_choice == computor_choice:
    print("It's a tie")
elif user_choice == "Rock" and computor_choice == "Scissors":
    print("You win!")
elif user_choice == "Paper" and computor_choice == "Rock":
    print("You win!")
elif user_choice == "Scissors" and computor_choice == "Paper":
    print("You win!")
else:
    print("You lose!")