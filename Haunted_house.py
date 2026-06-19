import random

score = 0

print("*********************************")
print("WELCOME TO THE HAUNTED HOUSE")
print("*********************************")

print("Oho! You are trapped in my house.")
print("There are three doors in the house.")
print("Behind one door there is a ghost.")
print("Behind another door there is a key to escape.")
print("Behind the last door there is nothing.")
print()

# Key and ghost can never be in the same door
key_random = random.randint(1, 3)

ghost_random = random.randint(1, 3)
while ghost_random == key_random:
    ghost_random = random.randint(1, 3)

x = int(input("Choose a door (1-3): "))

if x == key_random:
    print("Great! You have found the key.")

elif x == ghost_random:
    print("OH NO! You found the ghost.")
    print("GAME OVER")

else:
    print("Nothing here.")

if x == key_random:

    print("\nWELCOME! YOU HAVE ENTERED LEVEL 2")
    print("Answer my three riddles.\n")

    # RIDDLE 1
    print("RIDDLE 1")
    print("What comes down but never goes up?")
    answer1 = input("Enter your answer: ").lower()

    if answer1 == "rain":
        score += 1
        print("Correct answer!")
    else:
        print("Wrong answer!")

    print()

    # RIDDLE 2
    print("RIDDLE 2")
    print("What is the capital of India?")
    answer2 = input("Enter your answer: ").lower()

    if answer2 == "delhi":
        score += 1
        print("Correct answer!")
    else:
        print("Wrong answer!")

    print()

    # RIDDLE 3
    print("RIDDLE 3")
    print("What has hands but never claps?")
    answer3 = input("Enter your answer: ").lower()

    if answer3 == "clock":
        score += 1
        print("Correct answer!")
    else:
        print("Wrong answer!")

    print("\nYour Score:", score, "/3")

    if score == 3:
        print("YOU WIN!")
    else:
        print("GHOST WINS!")

print()
print("********************************")
print("THANKS FOR PLAYING")
print("********************************")# The_haunted_house.py

Enter aa game where your fate depends on luck and intelligence! Choose one of three mysterious doors. Behind one door is a key to escape, behind another is a ghost, and the last is empty. If you find the key, you'll unlock Level 2, where you must solve three riddles to win the game. Answer all riddles correctly to escape the house and claim victory
