
#
#The first while loop is a standard loop that will run until the condition is false.
#
#The second while loop is a do-while loop. It will run at least once, and then continue to run until the condition is false.
#
#The third while loop is a while loop that will run until the condition is false.
#
#The fourth while loop is a do-while loop. It will run at least once, and then continue to run until the condition is false


#while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# do while loop
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# while loop
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# do while loop
i = 1
while True:
    if i % 2 == 0:
        print(i)
    i += 1
    if i > 10:
        break