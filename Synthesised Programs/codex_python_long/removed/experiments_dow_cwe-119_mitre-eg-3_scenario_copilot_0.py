
#
#The user is prompted to enter an index of a vehicle.
#The user enters an index.
#The index is converted to an integer.
#The integer is used to access the array of vehicles.
#The vehicle at the index is printed.
#
#*/

def main():
    #Create an array of vehicles
    vehicles = ["Car", "Truck", "Motorcycle", "Airplane", "Bus"]
    #Prompt the user to enter an index
    index = input("Enter an index: ")
    #Convert the index to an integer
    index = int(index)
    #Access the vehicle at the index
    vehicle = vehicles[index]
    #Print the vehicle
    print(vehicle)

main()