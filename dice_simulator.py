import random
import time

print("🎲 Dice Options:")
print("1 - Dice with higher chance of SIX")
print("2 - Dice with higher chance of ONE")
print("3 - Normal fair dice")

Dice = input("Enter which dice you want to play with (1, 2, or 3): ")

# Define dice based on choice
if Dice == "1":
    possible_outcomes = [1, 2, 3, 4, 5] + [6] * 10  # High chance of 6
elif Dice == "2":
    possible_outcomes = [2, 3, 4, 5, 6] + [1] * 8   # High chance of 1
elif Dice == "3":
    possible_outcomes = [1, 2, 3, 4, 5, 6]          # Fair dice
else:
    print("❌ Invalid input. Please enter 1, 2, or 3.")
    exit()

roll = input("Type 'a' to roll the dice: ")
if roll.lower() == "a":
    print("\nRolling the dice...", end="")
    for i in range(3):  # Animation dots
        time.sleep(0.3)
        print(".", end="", flush=True)

    print("\n")

    dice_no = random.choice(possible_outcomes)
    print(f"🎯 You rolled: {dice_no}")
else:
    print("❌ Invalid roll input.")
