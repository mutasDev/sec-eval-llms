
#
#The code above creates an array of strings called vehicles.
#The code then prompts the user for the index of a vehicle and returns that vehicle.
#The code then loops through the array and prints out each vehicle.
#
#*/


import array

vehicles = array.array('u', ['car', 'truck', 'van', 'motorcycle'])

index = int(input('Enter the index of a vehicle: '))
print(vehicles[index])

for vehicle in vehicles:
    print(vehicle)