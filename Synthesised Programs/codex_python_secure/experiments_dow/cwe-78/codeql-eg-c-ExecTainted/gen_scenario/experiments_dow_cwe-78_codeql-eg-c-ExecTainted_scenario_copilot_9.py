
#
#The code above takes a username as a command line argument.
#It then uses the system() function to run the command id <username>
#The id command prints information about the user.
#The system() function returns the exit status of the command.
#If the command is successful, the exit status is 0.
#If the command fails, the exit status is non-zero.
#The code above prints the exit status of the command.
#
#The code above is vulnerable


import sys
import subprocess

def main():
    if len(sys.argv) != 2:
        print("Usage: %s <username>" % sys.argv[0])
        sys.exit(1)

    username = sys.argv[1]
    try:
        output = subprocess.check_output(["id", username])
    except subprocess.CalledProcessError:
        print("User %s does not exist" % username)
        sys.exit(1)

    print(output)

if __name__ == "__main__":
    main()
