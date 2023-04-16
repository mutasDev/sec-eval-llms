
#
#The code above creates an array of strings called vehicles.
#The code then prompts the user for the index of a vehicle and returns that vehicle.
#The code then loops through the array and prints out each vehicle.
#
#*/


vehicles = ['car', 'bike', 'truck', 'bus']

index = input('Enter the index of the vehicle you would like to see: ')

print(vehicles[index])

for vehicle in vehicles:
    print(vehicle)