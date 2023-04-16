
#
#The user is prompted to enter an index of a vehicle.
#The user enters an index.
#The index is converted to an integer.
#The integer is used to access the array of vehicles.
#The vehicle at the index is printed.
#
#*/


import sys

def main():
    vehicles = ["car", "truck", "motorcycle", "bicycle"]
    print("Please enter an index of a vehicle:")
    index = int(input())
    print(vehicles[index])

if __name__ == "__main__":
    main()