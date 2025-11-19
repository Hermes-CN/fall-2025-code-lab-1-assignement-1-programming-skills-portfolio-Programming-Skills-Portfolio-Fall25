names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # Creating a list

Looking_for = input("Enter the name you are looking for: ") # Ask for an input 

if Looking_for in names: # Creating a statement in case the input matches an element of the list
    print(f"The name {Looking_for} was found in the list.")
else:
    print(f"The name {Looking_for} was not found in the list.")
