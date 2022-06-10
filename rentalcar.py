# Functions used to recommend a rental car to a renter
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

