from cars import *
from linkedList import *
from rentalcar import *


types_of_cars = insert_car_types()
each_car = insert_cars()


# The program:

print("*"*60)
print("*"*60)
print("\n")
print("~~~~~~~   Welcome to TrulyExpensive Auto Rentals!   ~~~~~~~")
print("\n")
print("*"*60)
print("*"*60)
print("\nWe would like to match you with a rental car.\n\n")
first_choice = input(f"Start typing out the type of vehicle you would like to rent (Ex: 's' for sedan etc...) and then press 'Enter': ")
reduced_types = find_car_type(first_choice, types_of_cars)
print("\nThese are our options for those letters:\n")
print(make_types_readable(reduced_types))
second_choice = input("\nWhich of these would you like to see options for (type the first few letters and press 'Enter': ")
chosen_type = find_car_type(second_choice, types_of_cars)
options = find_cars(chosen_type[0], each_car)
print("\n\n")
print(f"Here is a list of {chosen_type[0]}'s of that type...\n")
print(make_cars_readable(options))