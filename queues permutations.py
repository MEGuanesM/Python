import sys


class MyQueue():
    def __init__(self, capacity):
        if capacity:
            if isinstance(capacity, int):
                if capacity > 0:
                    self.__capacity = capacity
                else:
                    raise ValueError
            else:
                raise TypeError
        else:
            self.__capacity = 10
        self.__start = -1
        self.__end = 0
        self.__array = [None] * self.__capacity

    @property
    def size(self):
        if self.__start == -1:
            return 0
        elif self.__start == self.__end:
            return self.__capacity
        elif self.__start < self.__end:
            return self.__end - self.__start
        else:
            return (self.__capacity - self.__start + self.__end)
    
    @property
    def capacity(self):
        return self.__capacity
    
    @property
    def is_full(self):
        return self.__start == self.__end
    
    @property
    def is_empty(self):
        return self.__start == -1
    
    @property
    def debug_array(self):
        return self.__array
    
    @property
    def debug_start(self):
        return self.__start

    @property
    def debug_end(self):
        return self.__end

    def enqueue(self, value):
        if not self.is_full:
            self.__array[self.__end] = value
            self.__end = (self.__end + 1) % (len(self.__array))
            if self.__start == -1:
                self.__start = 0
        else:
            raise RuntimeError
    
    def dequeue(self):
        if not self.is_empty:
            item = self.__array[self.__start]
            self.__start = (self.__start + 1) % (len(self.__array))
            if self.__start == self.__end:
                self.__start = -1
                self.__end = 0
            return item
        else:
            raise RuntimeError
    
    def peek(self):
        if not self.is_empty:
            return self.__array[self.__start]
        else: 
            raise RuntimeError
    
    def find(self, value):
        depth = 0
        for i in self.__array:
            if i == value:
                return depth
            depth = depth + 1
        return -1
    
    def double_capacity(self):
        new_array = [None] * (self.__capacity * 2)
        length = self.size
        for i in range(length):
            new_array[i] = self.dequeue()
        self.__start = 0
        self.__end = length
        self.__array = new_array
        self.__capacity = self.__capacity * 2

    def half_capacity(self):
        if self.size > (self.capacity / 2):
            raise RuntimeError
        else:
            new_array = [None] * int(self.__capacity / 2)
            length = self.size
            for i in range(length):
                new_array[i] = self.dequeue()
            self.__start = 0
            self.__end = length % len(new_array)
            self.__array = new_array
            self.__capacity = int(self.__capacity / 2)

    def copy(self):
        nq = MyQueue(self.__capacity)
        length = self.size
        for i in range(length):
            nq.enqueue(self.__array[i])
        return nq

    def __str__(self):
        st = ""
        for i in range(self.size):
            next = (self.__start + i) % self.__capacity
            st = st + str(self.__array[next]) + "\n"
        return st
    
    @staticmethod
    def test():
        """ Method to test Queue operations

        This is called when the queue is executed as a
        a standalone script

        It will call each of the methods of the Queue class
        It DOES NOT check for proper use of exceptions
        """
        queue = MyQueue(10)
        print("===EMPTY QUEUE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        for i in range(0, 20, 2):
            queue.enqueue(i)

        print("===ADD 10 ELEMENTS===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))
        print("{}".format(queue))

        print("===FIND===")
        print("Depth of 16: {}".format(queue.find(16)))
        print("Depth of 12: {}".format(queue.find(12)))
        print("Depth of  8: {}".format(queue.find(8)))
        print("Depth of  4: {}".format(queue.find(4)))
        print("Depth of  5: {}".format(queue.find(5)))

        queue.double_capacity()

        print("===DOUBLE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        queue.half_capacity()

        print("===HALF===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))

        queue2 = queue.copy()

        print("===COPY===")
        print("Queue 1 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))
        print("{}".format(queue))
        print("Queue 2 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue2.size, queue2.capacity, queue2.is_empty, queue2.is_full))
        print("{}".format(queue2))

        print("===PEEK===")
        print("{}".format(queue.peek()))

        print("===POP===")
        while not queue.is_empty:
            print("{}".format(queue.dequeue()))

        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            queue.size, queue.capacity, queue.is_empty, queue.is_full))


# Main Guard
if __name__ == "__main__":
    MyQueue.test()




from MyQueue import *
import sys


class PermutationGenerator:
    def __init__(self):
        pass
    
    def permutations(self, input):
        if isinstance(input, str):
            for i in input:
                f = 0
                for j in input:
                    if i == j:
                        f = f + 1
                    if f > 1:
                        raise ValueError
        else:
            raise TypeError

        q = MyQueue(self.factorial(len(input)))
        q.enqueue("")
        output = [None] * (self.factorial(len(input)))
        index = 0
        while not q.is_empty:
            item = q.dequeue()
            if len(item) == len(input):
                #print("len input: {}".format(len(input)))
                #print("index: {}".format(index))
                #print("len output: {}".format(len(output)))
                output[index] = item
                index = index + 1
            else:
                for i in input:
                    if i not in item:
                        if not q.is_full:
                            q.enqueue(item + i)
                        else:
                            q.double_capacity()
                            q.enqueue(item + i)
        x = sorted(output)
        output = ''.join(x)
        return x
                
    def factorial(self, number):
        if isinstance(number, int):
            if number > 0:
                if number == 1:
                    return number
                else:
                    return number * self.factorial(number - 1)
            else:
                raise ValueError
        else:
            raise TypeError

    @staticmethod
    def main(args):
        """ Method to test PermutationGenerator operations

        This is called when the generator is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        permutations function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        generator = PermutationGenerator()
        with open(args[1]) as scanner:
            print(generator.permutations(scanner.readline()))


# main guard
if __name__ == "__main__":
    PermutationGenerator.main(sys.argv)
