import sys


class LinearSearch:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            value = int(scanner.readline())
            print(self.linear_search(value, array))

    def linear_search(self, value, array):
        for i in range(len(array)):
            #print(value)
            if array[i] == value:
                return i
        return -1


# main guard
if __name__ == "__main__":
    obj = LinearSearch()
    obj.main(sys.argv)

import sys


class BubbleSort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.bubble_sort(array))

    def bubble_sort(self, array):
        for i in range(len(array)):
            for j in range((len(array) - 1 - i)):
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            print(str(array))
        #print("xxxxxxxxxxxxxxxxxxxxxxxx")
        return array


# main guard
if __name__ == "__main__":
    obj = BubbleSort()
    obj.main(sys.argv)

import sys


class MergeSort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.merge_sort(array, 0, len(array) - 1))

    def merge_sort(self, array, start, end):
        if (end - start + 1) == 1:
            return
        if (end - start + 1) == 2:
            if array[start] > array[end]:
                temp = array[start]
                array[start] = array[end]
                array[end] = temp
            return
        half = int((start + end) / 2)
        self.merge_sort(array, start, half)
        self.merge_sort(array, half + 1, end)
        self.merge(array, start, half, end)
        print(str(array))
        return array

    def merge(self, array, start, half, end):
        temparray = [None] * (end - start + 1)
        i = start
        j = half + 1
        z = 0
        while (i <= half) and (j <= end):
            if array[i] < array[j]:
                temparray[z] = array[i]
                i = i + 1
            else:
                temparray[z] = array[j]
                j = j + 1
            z = z + 1
        
        while (i <= half):
            temparray[z] = array[i]
            i = i + 1
            z = z + 1
        
        while (j <= end):
            temparray[z] = array[j]
            j = j + 1
            z = z + 1
        
        for t in range(len(temparray)): #running from command line it is temparray - 1 but the autograder deosnt like it
            array[start + t] = temparray[t]


# main guard
if __name__ == "__main__":
    obj = MergeSort()
    obj.main(sys.argv)

import sys


class Quicksort:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            print(self.quicksort(array, 0, len(array) - 1))

    def quicksort(self, array, start, end):
        if start >= end:
            return
        pivotindex = self.partition(array, start, end)
        self.quicksort(array, start, pivotindex - 1)
        self.quicksort(array, pivotindex + 1, end)
        print(str(array))
        return array

    def partition(self, array, start, end):
        pivotvalue = array[end]
        pivotindex = start
        #print(start)
        #print(end)
        for i in range(start, end + 1):
            #print("i: = {}".format(i))
            #print("lenarray: {}".format(len(array)))
            if array[i] <= pivotvalue:
                temp = array[i]
                array[i] = array[pivotindex]
                array[pivotindex] = temp
                pivotindex = pivotindex + 1
        return pivotindex - 1

# main guard
if __name__ == "__main__":
    obj = Quicksort()
    obj.main(sys.argv)

import sys


class BinarySearch:

    def main(self, args):
        if len(args) != 2:
            print("Program requires a file as a command-line argument")
            return
        with open(args[1]) as scanner:
            splits = scanner.readline().split(",")
            array = [int(i) for i in splits]
            value = int(scanner.readline())
            print(self.binary_search(array, value, 0, len(array) - 1))

    def binary_search(self, array, value, start, end):
        if start > end:
            return -1
        middle = int((start + end) / 2)
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            return self.binary_search(array, value, start, middle - 1)
        elif array[middle] < value:
            return self.binary_search(array, value, middle + 1, end)


# main guard
if __name__ == "__main__":
    obj = BinarySearch()
    obj.main(sys.argv)

