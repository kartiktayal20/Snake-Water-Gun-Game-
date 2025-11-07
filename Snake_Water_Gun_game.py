import random

computer = random.choice([1, 2, 3])

print("Let's start the game- Snake, Water and Gun")
print("Enter your choice:- s-> Snake, w-> Water and g-> Gun")

str = input("Enter your choice: ")
dict = {"s": 1, "w": 2, "g": 3}
dict2 = {1: "Snake", 2: "Water", 3: "Gun"}

user = dict[str]

print(f"You choose: {dict2[user]}\nComputer choose: {dict2[computer]}")

if(computer == user):
    print("It's draw")

else:
    if(computer == 1 and user == 2):
        print("You Lose!")

    elif(computer == 1 and user == 3):
        print("You Win!")

    elif(computer == 2 and user == 1 ):
        print("You Win!")

    elif(computer == 2 and user == 3):
        print("You Lose!")

    elif(computer == 3 and user == 1):
        print("You Lose!")

    elif(computer == 3 and user == 2):
        print("You Win!")
        
    else:
        print("Something went wrong try again.")
