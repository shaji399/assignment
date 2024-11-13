"""import random

# Generate and print 10 random numbers between 1 and 100
for _ in range(10):
    print(random.randint(1, 100), end=" ")"""
"""import random

def play_game(rounds):
    score = 0  # Initialize the score

    # Loop for the specified number of rounds
    for round_num in range(1, rounds + 1):
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        # Display the player's number
        print(f"Round {round_num}:")
        print(f"Your number is: {player_number}")
        
        # Ask the player to guess if their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's number? (Enter 'higher' or 'lower'): ").strip().lower()

        # Check if the player's guess is correct
        if (guess == 'higher' and player_number > computer_number) or (guess == 'lower' and player_number < computer_number):
            print("Correct! You get a point.")
            score += 1
        else:
            print(f"Incorrect. The computer's number was: {computer_number}")
        
        print()  # Print a blank line to separate rounds

    # Display the final score after all rounds
    print(f"Game Over! Your final score is: {score}/{rounds}")

# Start the game with a specified number of rounds
rounds = 5  # You can change this number for more or fewer rounds
play_game(rounds)"""
"""# Step 1: Prompt the user for their weight on Earth
earth_weight = float(input("Enter your weight on Earth (in kilograms): "))

# Step 2: Calculate the weight on Mars
mars_weight = earth_weight * 0.378

# Step 3: Round the result to two decimal places
mars_weight_rounded = round(mars_weight, 2)

# Step 4: Print the result
print(f"Your weight on Mars would be: {mars_weight_rounded} kilograms")"""
"""def main():
    # Create a list called fruit_list with the given fruits
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit_list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit_list:", fruit_list)

# Call the main function to run the program
main()"""
"""# Function to access an element by index
def access_element(my_list, index):
    if index < 0 or index >= len(my_list):
        return "Error: Index out of range"
    return my_list[index]

# Function to modify an element by index
def modify_element(my_list, index, new_value):
    if index < 0 or index >= len(my_list):
        return "Error: Index out of range"
    my_list[index] = new_value
    return my_list

# Function to slice the list
def slice_list(my_list, start_index, end_index):
    # Handle index out of range cases by adjusting the indices
    if start_index < 0:
        start_index = 0
    if end_index > len(my_list):
        end_index = len(my_list)
    if start_index > end_index:
        return "Error: Start index cannot be greater than end index"
    return my_list[start_index:end_index]

# Game loop for interacting with the list
def list_game():
    # Initialize a sample list
    my_list = ['apple', 7, 'banana', 12, 'orange']

    print("Welcome to the List Manipulation Game!")
    print("Here's the list you will work with:")
    print(my_list)

    # Game loop
    while True:
        # Ask the user which operation they want to perform
        print("\nSelect an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit the game")

        choice = input("Enter the number of your choice: ")

        if choice == '1':  # Access an element
            index = int(input("Enter the index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == '2':  # Modify an element
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            if new_value.isdigit():
                new_value = int(new_value)  # Convert to integer if the new value is numeric
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == '3':  # Slice the list
            start_index = int(input("Enter the start index for slicing: "))
            end_index = int(input("Enter the end index for slicing: "))
            result = slice_list(my_list, start_index, end_index)
            print("Sliced list:", result)

        elif choice == '4':  # Quit the game
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the game
list_game()"""











