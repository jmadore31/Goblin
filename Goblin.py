import random
import time


start = input("The Goblin stole your coin purse!! go after him? (Y/N): ")

roll_again = "y"
while start == "y" or roll_again == "y":
    print("\nRunning after the Goblin...")
    time.sleep(1)
    
    player = random.randint(1, 6)
    goblin = random.randint(1, 8)

    print("the dice rolls are:")
    print("player =", player, "\ngoblin =", goblin)

    if player > goblin:
        print("you caught up to the Goblin!")
    else:
        print("Try again")

    roll_again = input("\nRoll again? (Y/N)")