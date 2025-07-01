import sys


def main(args):
    if len(args) != 2:
        print("Program requires a file as a command-line argument")
        return
    with open(args[1]) as scanner:
        line = scanner.readline().split(" ")
        a = int(line[0])
        b = int(line[1])
        print(recursive_sum(a, b))


def recursive_sum(a, b):
    #print("a: {} b {} ".format(a, b))
    if b == 0:
        #print("zero")
        #print(type(a))
        #print("a: {}".format(a))
        return (a)
    elif b >= 1:
        if (a + b) == (a + 1) and b > 1:
            #print("a: {} b: {} a + b: {} a + 1: {}".format(a, b, a + b, a + 1))
            return recursive_sum(a, b - 1)
        else:
            return recursive_sum(a + 1, b - 1)
    else:
        return -1


# main guard
if __name__ == "__main__":
    main(sys.argv)
import sys


def main(args):
    if len(args) != 2:
        print("Program requires a file as a command-line argument")
        return
    with open(args[1]) as scanner:
        line = scanner.readline().split(" ")
        a = int(line[0])
        b = int(line[1])
        print(recursive_power(a, b))
        

def recursive_power(a, b):
    #print(a)
    #print(b)
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    elif b > 1:
        #print(a)
        #print(b)
        return a * recursive_power(a, b - 1)
    else:
        return -1


# main guard
if __name__ == "__main__":
    main(sys.argv)

import sys


def main(args):
    if len(args) != 2:
        print("Program requires a file as a command-line argument")
        return
    with open(args[1]) as scanner:
        line = scanner.readline().split(" ")
        print(recursive_find(line[0], line[1]))
        

def recursive_find(haystack, needle):
    print(haystack)
    if haystack == needle:
        return True
    elif len(haystack) <= len(needle):
        return False
    else:
        back = recursive_find(haystack[1:], needle)
        front = recursive_find(haystack[:len(haystack) - 1], needle)
        return back or front


# main guard
if __name__ == "__main__":
    main(sys.argv)

import sys


def main(args):
    if len(args) != 2:
        print("Program requires a file as a command-line argument")
        return
    with open(args[1]) as scanner:
        a = int(scanner.readline())
        memo = [-1] * (a + 1)  # create memoization list 
        memo[0] = 0            # set Fib(0)
        memo[1] = 1            # set Fib(1)
        print(memo_fib(a, memo))
        

def memo_fib(a, memo):
    if len(memo) > 3:
        if memo[len(memo) - 1] == -1:
            #print(memo)
            memo[len(memo) - a + 1] = memo[len(memo) - a] + memo[len(memo) - a - 1]
            #print("new")
            #print(memo)
            memo_fib(a - 1, memo)
        return memo[len(memo) - 1]
    else:
        return 1



# main guard
if __name__ == "__main__":
    main(sys.argv)
