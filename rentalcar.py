# Program to recommend a rental car to a renter
from cars import *
from linkedList import *


def insert_car_types():
    car_type_list = LinkedList()
    for type in car_type:
        car_type_list.insert_beginning(type)
    return car_type_list

def insert_cars():
    car_list = LinkedList()
    for car in cars:
        car_list.insert_beginning(car)
    return car_list

def find_cars(car_type, linked_list):
    current_node = linked_list.get_head_node()
    present_list = []
    while current_node.next_node:   
        if current_node.get_value()[0] == car_type:
            present_list.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return present_list

def make_cars_readable(ls):  
    for i in ls:
        print("-"*20 + "\n")
        print(f"Make : {i[1]}")
        print(f"Model : {i[2]}")
        print(f"{i[3]} doors")
        print(f"Up to {i[4]} passengers")
        print(f"${i[5]} per day")
        print("\n\n")
    return ""

def find_car_type(string, linked_list):
    current_node = linked_list.get_head_node()
    type_list = []
    while current_node.next_node:   
        if current_node.get_value()[0:len(string)].lower() == string.lower():
            type_list.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return type_list

def make_types_readable(ls):
    for i in ls:
        print("- " + i )
    return ""




# types_of_cars = insert_car_types()
# each_car = insert_cars()


# # The program:

# print("*"*60)
# print("*"*60)
# print("\n")
# print("~~~~~~~   Welcome to TrulyExpensive Auto Rentals!   ~~~~~~~")
# print("\n")
# print("*"*60)
# print("*"*60)
# print("\nWe would like to match you with a rental car.\n\n")
# first_choice = input(f"Start typing out the type of vehicle you would like to rent (Ex: 's' for sedan etc...) and then press 'Enter': ")
# reduced_types = find_car_type(first_choice, types_of_cars)
# print("\nThese are our options for those letters:\n")
# print(make_types_readable(reduced_types))
# second_choice = input("\nWhich of these would you like to see options for (type the first few letters and press 'Enter': ")
# chosen_type = find_car_type(second_choice, types_of_cars)
# options = find_cars(chosen_type[0], each_car)
# print("\n\n")
# print(f"Here is a list of {chosen_type[0]}'s of that type...\n")
# print(make_cars_readable(options))