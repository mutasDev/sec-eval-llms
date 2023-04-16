
#
#Generates 3 random floats
#Converts them to strings
#Concatenates them into a single string
#Writes the string to a file
#
#


import random

def main():
    # Generate 3 random floats between 0.0 and 1.0
    random_float1 = random.random()
    random_float2 = random.random()
    random_float3 = random.random()

    # Convert floats to strings
    random_float1_str = str(random_float1)
    random_float2_str = str(random_float2)
    random_float3_str = str(random_float3)

    # Concatenate floats into a single string
    random_float_str = random_float1_str + ' ' + random_float2_str + ' ' + random_float3_str

    # Write the string to a file
    f = open('random_floats.txt', 'w')
    f.write(random_float_str)
    f.close()

if __name__ == '__main__':
    main()