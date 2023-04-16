
#
#We create a string with some super secret info.
#We create a file and write the super secret info to it.
#We change the permissions of the file to read-only for the owner.
#We print the name of the file to the screen.
#
#""


import os

def main():
    secret_info = "This is a super secret message."
    file_name = "secret_message.txt"
    file_handle = open(file_name, "w")
    file_handle.write(secret_info)
    file_handle.close()
    os.chmod(file_name, 0o400)
    print(file_name)

if __name__ == "__main__":
    main()

