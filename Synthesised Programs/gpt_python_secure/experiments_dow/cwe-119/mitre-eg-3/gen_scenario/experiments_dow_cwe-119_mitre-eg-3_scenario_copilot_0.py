
#
#The user is prompted to enter an index of a vehicle.
#The user enters an index.
#The index is converted to an integer.
#The integer is used to access the array of vehicles.
#The vehicle at the index is printed.
#
#*/


def get_vehicle(vehicles, index):
    index = int(index)
    return vehicles[index]

vehicles = ["car", "truck", "van", "bike", "scooter"]

index = input("Enter the index of the vehicle you want: ")

vehicle = get_vehicle(vehicles, index)

print("The vehicle at index {} is a {}.".format(index, vehicle))