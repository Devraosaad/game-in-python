import time

def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest. You need to find a way out.")
    time.sleep(2)
    print("You come to a crossroad. Which way do you want to go?")
    time.sleep(0)

def crossroad():
    print("\nYou are at a crossroad.")
    print("1. Go left into a cave.")
    print("2. Go straight ahead through the forest.")
    print("3. Go right towards a river.")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        cave()
    elif choice == '2':
        forest()
    elif choice == '3':
        river()
    else:
        print("Invalid choice. Try again.")
        crossroad()

def cave():
    print("\nYou enter a dark cave.")
    time.sleep(1)
    print("It is very cold and damp inside.")
    time.sleep(1)
    print("You see a faint light at the end of the cave.")
    time.sleep(1)
    print("Do you want to approach the light?")

    approach = input("Yes/No: ").lower()

    if approach == 'yes':
        print("\nYou cautiously approach the light...")
        time.sleep(2)
        print("Congratulations! You found your way out of the cave!")
    elif approach == 'no':
        print("\nYou decide not to risk it and turn back.")
        crossroad()
    else:
        print("Invalid choice. Try again.")
        cave()

def forest():
    print("\nYou walk through the dense forest.")
    time.sleep(1)
    print("It gets darker as you go deeper.")
    time.sleep(1)
    print("You hear strange noises around you.")
    time.sleep(1)
    print("Suddenly, you see a bear blocking your path!")
    time.sleep(1)
    print("What do you do?")

    action = input("Fight/Run: ").lower()

    if action == 'fight':
        print("\nYou attempt to fight the bear...")
        time.sleep(2)
        print("Unfortunately, the bear is too strong and you are defeated.")
        time.sleep(1)
        print("Game Over.")
    elif action == 'run':
        print("\nYou try to run away from the bear...")
        time.sleep(2)
        print("You manage to escape and find a hidden path out of the forest!")
        time.sleep(1)
        print("Congratulations! You made it out safely!")
    else:
        print("Invalid choice. Try again.")
        forest()

def river():
    print("\nYou reach the bank of a fast-flowing river.")
    time.sleep(1)
    print("The water looks deep and dangerous.")
    time.sleep(1)
    print("There is a boat nearby. Do you want to take the boat across the river?")

    boat = input("Yes/No: ").lower()

    if boat == 'yes':
        print("\nYou decide to take the boat...")
        time.sleep(2)
        print("You successfully navigate across the river!")
        time.sleep(1)
        print("Congratulations! You found your way out!")
    elif boat == 'no':
        print("\nYou decide not to risk it and look for another way.")
        crossroad()
    else:
        print("Invalid choice. Try again.")
        river()

# Main game loop
def play_game():
    intro()
    crossroad()

    replay = input("\nDo you want to play again? (Yes/No): ").lower()
    if replay == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
