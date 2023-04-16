
#
#The open() function creates a new file or opens an existing file.
#The O_CREAT flag tells open() to create the file if it doesn't exist.
#The O_TRUNC flag tells open() to truncate the file to 0 bytes if it already exists.
#The O_WRONLY flag tells open() to open the file for writing only.
#The O_EXCL flag tells open() to fail if the file already exists.

def main():
    # create an empty file
    with open("empty.txt", "w") as f:
        pass

    # create an empty file and truncate to 0 bytes
    with open("empty_truncated.txt", "w") as f:
        f.truncate()

    # create a file and write some string to it
    with open("my_file.txt", "w") as f:
        f.write("my first line\n")
        f.write("my second line\n")

    # create a file and write some string to it
    with open("my_file.txt", "r") as f:
        print(f.read())

    # create a file and write some string to it, then read it and print
    with open("my_file.txt", "w+") as f:
        f.write("my third line\n")
        f.write("my fourth line\n")
        f.seek(0)
        print(f.read())

    # create a file and write some string to it
    with open("my_file.txt", "wb") as f:
        f.write(b"my fifth line\n")
        f.write(b"my sixth line\n")

    # create a file and write some string to it
    with open("my_file.txt", "rb") as f:
        print(f.read())

if __name__ == "__main__":
    main()