# The application script with which the user interacts

from cars import *
from linkedList import *
from rentalcar import *

# Populating the Linked Lists:
types_of_cars = insert_car_types()
each_car = insert_cars()


# Introduction/Heading
print("*"*60)
print("*"*60)
print("\n")
print("~~~~~~~   Welcome to TrulyExpensive Auto Rentals!   ~~~~~~~")
print("\n")
print("*"*60)
print("*"*60)
print("\nWe would like to match you with a rental car.\n\n")

# The contorl-flow of the application
# While start = True, the program will continue to loop. Therefore, the user will be able to continue to
start = True
while start:
    first_choice = input(f"\nStart typing out the type of vehicle you would like to rent (Ex: 's' for sedan, SUV, etc...) and then press 'Enter': ")
    # Creates a list of the car types that begin with the letters that were entered
    reduced_types = find_car_type(first_choice, types_of_cars)
    
    # If there is more than one option, the user needs to continue to widdle it down
    while len(reduced_types) > 1:
        print("\nThese are our options for the letters you entered:\n")
        # Shows the types in a list format:
        print(make_types_readable(reduced_types))
        # Requires the user to narrow the car type and stores it in a new variable
        second_choice = input("\nWhich of these would you like to see options for (type the first few letters and press 'Enter': ")
        # Re-assigns reduced_types to the second choice
        reduced_types = find_car_type(second_choice, types_of_cars)
    # Checks to ensure there is one type selected and assigns a new variable to this value
    if len(reduced_types) == 1:
        chosen_type = reduced_types[0]
    # If there are no types, the will go back to the start of the first while loop
    if len(reduced_types) < 1:
        print("\nSorry, there are no types of cars that match those letters in our inventory. Please try again.\n")
        continue
    
    # Shows the chosen type as a list of one
    print(make_types_readable(reduced_types))
    # Populates a list of all the cars from the each_car linked list   
    options = find_cars(chosen_type, each_car)
    # Asks if the user would like to see all the vehicles available of the chosen type
    choose_car = input(f"Do you want to see a list of {chosen_type}'s ('y' or 'n')?\n")
    # Ensures a valid choice was made
    while (choose_car != 'y') and (choose_car != 'n'):
        choose_car = input(f"Invalid choice. Do you want to see a list of {chosen_type}'s ('y' or 'n')?\n")
    
    # If the user wants to see the vehicles, the script will display all the of them that fall within that type
    if choose_car == 'y':
        print(f"\nThese are the available {chosen_type}'s:\n")
        print(make_cars_readable(options))
        # Asks user if they want to search for more cars.
        more = input("Do you want to find other types of cars ('y' or 'n')? ")
        # Ensures a valid choice was made
        while more != 'n' and more != 'y':
            more = input("Invalid choice. Do you want to find other types of cars ('y' or 'n')? ")
        # If the user doesn't want to see more cars, the script is terminated
        if more == 'n':
            print("Thank you for choosing TrulyExpensive Auto Rentals! \n     Bye!")
            start = False
            break
        # If the user does want to see more cars, the script loops back to the first while loop
        if more == 'y':
            continue


