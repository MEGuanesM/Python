import sys


def main(argv):
    # If an argument is present, we are reading from a file
    # specified in sys.argv[1]
    if len(argv) > 1:
        reader = open(argv[1])

    # If no argument, read from stdin  
    else:
        reader = sys.stdin

    x = int(reader.readline())

    # -=-=-=-=- MORE CODE GOES HERE -=-=-=-=- 

    if x < 0:
        print("0")
    else:
        if x % 3 == 0:
            sum = 0
        else:
            sum = x
        for i in range(x):
            if i % 3 != 0:
                sum = sum + i
        print(sum)
# main guard


if __name__ == "__main__":
    main(sys.argv)
