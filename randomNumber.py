import random

def guess(num):
    random_number = random.randint(1,num) #define range 
    guess = 0
    while guess != random_number:      #     !=  7
        guess = int(input(f"Enter the number between 1 and {num}: "))
        if guess < random_number:
            print("Sorry, Try Again. Too Low")
        elif guess > random_number:
            print("Sorry, Try Again. Too High")
    print(f"Yay!!!, You have Guessed the {random_number} Correct Number")
guess(50)