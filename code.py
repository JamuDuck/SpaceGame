import random

# Void Function
def showInstructions():
    print("Welcome to the Space Adventure Game!")
    print("Your goal is to travel back to Earth by answering questions.")
    print("Each time you answer incorrectly, you lose 20 HP and may meet an alien.")
    print("If your HP reaches 0, you lose. If you answer all questions correctly, you win!")

# Alien
def alienEncounter():
    chance = random.randint(1, 100) 
    if chance <= 50:  # 50% chance for an alien encounter
        alien_type = random.randint(1, 4)  
        if alien_type <= 3: 
            print("A friendly alien appeared! +25 HP.")
            return 25
        else: 
            print("A hostile alien attacked! -25 HP.")
            return -25
    print("No alien encountered this time.")
    return 0  # No encounter