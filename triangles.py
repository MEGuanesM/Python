import sys


def main(argv):
    if len(argv) != 4:
        print("Invalid Arguments")
        sys.exit()

    try:
        #with open(argv[1]) as scanner1, open(argv[2]) as scanner2, \
        #       open(argv[3], "w") as writer:
        scanner1 = open(sys.argv[1]) 
        scanner2 = open(sys.argv[2]) 
        writer = open(sys.argv[3], "w") 
        post = 0
        negt = 0
        sumpos = 0
        sumneg = 0
        for line in scanner1:
            line = line.strip()
            input = float(line)
            if input >= 0:
                post = post + 1
                sumpos = sumpos + input
            else:
                negt = negt + 1
                sumneg = sumneg + input
        for line in scanner2:
            line = line.strip()
            input = float(line)
            if input >= 0:
                post = post + 1
                sumpos = sumpos + input
            else:
                negt = negt + 1
                sumneg = sumneg + input
        writer.write("{}\n".format(post))
        writer.write("{}\n".format(sumpos))
        writer.write("{}\n".format(negt))
        writer.write("{}\n".format(sumneg))
        print("Complete")

    except IOError as e:
        print("Invalid Arguments")
        return
    except ValueError as e:
        print("Invalid Input")
        return
    except FileNotFoundError as e:
        print("Invalid Arguments")
        return


if __name__ == "__main__":
    main(sys.argv)