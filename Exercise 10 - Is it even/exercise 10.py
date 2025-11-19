# checks if a number is even or odd
def check_even_odd(number):
    # Uses division by 2 to check
    if number / 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function to handle user input
def main():
    try:
        # Asks the user for a number 
        Selected_number = int(input("Enter a Number: "))
        result = check_even_odd(Selected_number)
        
        # Print the result by the function
        print(result)
    except ValueError:
        # Handle invalid input (e.g., letters instead of numbers)
        print("Please enter a valid Number.")

# Entry point of the program
if __name__ == "__main__":
    main()
