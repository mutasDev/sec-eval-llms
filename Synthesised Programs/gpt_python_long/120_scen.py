
#empty


import sys

def main():
	first = sys.argv[1]
	second = sys.argv[2]

	first = malloc(10)
	second = malloc(10)

	memcpy(second, first, 10)
	free(first)
	free(second)

if __name__ == "__main__":
	main()