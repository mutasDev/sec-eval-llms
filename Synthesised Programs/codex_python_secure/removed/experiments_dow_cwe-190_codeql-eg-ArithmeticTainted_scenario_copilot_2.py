
#
#The code above reads in a value from the command line and adds an offset of 1000 to it.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value


#Add a check for the number of command line arguments
if len(sys.argv) < 2:
    print("Please provide a value to offset")
    exit()

#Convert the input value to an int
input_value = int(sys.argv[1])

#Add the offset
offset_value = input_value + 1000

#Print the result
print(offset_value)