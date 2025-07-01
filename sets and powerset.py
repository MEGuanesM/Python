from ListNodeDouble import ListNodeDouble

class MyLinkedList:

    """ Class to represent a linked list

 

    Attributes

    ----------

    size : int

        the number of elements on the list

    start : ListNodeDouble

        the first node in the list

    end : ListNodeDouble

        the last node in the list

    current : ListNodeDouble

        the current node in the list when used as an iterator

    """

 

    def __init__(self):

        """Initialize an empty list

        """

        self.__start = None

        self.__end = None

        self.__current = None

        self.__size = 0

 

    @property
    def size(self):

        """ The number of elements stored in the list

        """

        return self.__size

 

    @property

    def is_full(self):

        """ Returns True if the list is full

        """

        return False

 

    @property

    def is_empty(self):

        """ Return True if the list is empty

        """

        return self.size == 0

 

    @property

    def debug_start(self):

        """ Returns the start node (for testing only)

        """

        return self.__start

 

    @property

    def debug_end(self):

        """ Returns the end node (for testing only)

        """

        return self.__end

   

    @property

    def debug_current(self):

        """ Returns the current node (for testing only)

        """

        return self.__current

 

    def append(self, value):

        """ Adds the provided value to the end of the list

 

        This method will raise a RuntimeError if the list is full

 

        Parameters

        ----------

        value : <any>

            the value to be added onto the end of the list

        """

        node = ListNodeDouble(value)

        if self.size == 0:

            self.__end = node

            self.__start = node

        else:

            self.__end.next_node = node

            node.previous_node = self.__end

            self.__end = node

        self.__size += 1

       

    def prepend(self, value):

        """ Adds the provided value to the start of the list

 

        This method will raise a RuntimeError if the list is full

 

        Parameters

        ----------

        value : <any>

            the value to be added onto the start of the list

        """

        node = ListNodeDouble(value)

        if self.size == 0:

            self.__end = node

            self.__start = node

        else:

            self.__start.previous_node = node

            node.next_node = self.__start

            self.__start = node

        self.__size += 1

       

    def insert(self, value, index):

        """ Adds the provided value to the given index of the list

        All subsequent elements will be shifted toward the end

 

        This method will raise a TypeError if the index is not an integer

        This metod will raise a ValueError if the index is invalid

 

        Parameters

        ----------

        value : <any>

            the value to be added onto the start of the list

        index : int

            the index to insert the value

        """

        if not isinstance(index, int):

            raise TypeError("index is not an integer")

        if index < 0 or index > self.size:

            raise ValueError("index is not inside of list")

        if index == 0:

            self.prepend(value)

        elif index == self.size:

            self.append(value)

        else:

            node = ListNodeDouble(value)

            next_node = self.__start

            for i in range(1, index):

                next_node = next_node.next_node

            node.next_node = next_node.next_node

            next_node.next_node.previous_node = node

            node.previous_node = next_node

            next_node.next_node = node

            self.__size += 1

 

    def remove_first(self):

        """ Removes the frontmost element from the list and returns it

 

        This method will raise a RuntimeError if the list is empty

        """

        if self.is_empty:

            raise RuntimeError("Cannot delist from an empty list")

        node = self.__start

        self.__start = self.__start.next_node

        if self.__start is None:

            self.__end = None

        else:

            self.__start.previous_node = None

        self.__size -= 1

        return node.item

   

    def remove_last(self):

        """ Removes the endmost element from the list and returns it

 

        This method will raise a RuntimeError if the list is empty

        """

        if self.is_empty:

            raise RuntimeError("Cannot delist from an empty list")

        node = self.__end

        self.__end = self.__end.previous_node

        if self.__end is None:

            self.__start = None

        else:

            self.__end.next_node = None

        self.__size -= 1

        return node.item

   

    def remove(self, index):

        """ Removes the element at the given index from the list

        and returns it

 

        This method will raise a TypeError if the index is not an integer

        This metod will raise a ValueError if the index is invalid

       

        Parameters

        ----------

        index : int

            the index to remove the value

        """

        if not isinstance(index, int):

            raise TypeError("index is not an integer")

        if index < 0 or index >= self.size:

            raise ValueError("index is not inside of list")

        if index == 0:

            return self.remove_first()

        elif index == self.size - 1:

            return self.remove_last()

        else:

            next_node = self.__start

            for i in range(1, index):

                next_node = next_node.next_node

            node = next_node.next_node

            next_node.next_node = node.next_node

            next_node.next_node.previous_node = next_node

            self.__size -= 1

            return node.item

 

    def peek(self):

        """ Returns the topmost element from the list without removing it

 

        This method will raise a RuntimeError if the list is empty

        """

        if self.is_empty:

            raise RuntimeError("Cannot peek an empty list")

        return self.__start.item

   

    def peek_last(self):

        """ Returns the last element from the list without removing it

 

        This method will raise a RuntimeError if the list is empty

        """

        if self.is_empty:

            raise RuntimeError("Cannot peek an empty list")

        return self.__end.item

   

    def get(self, index):

        """ Gets and returns the item on the list at the given index

       

        This method will raise a TypeError if the index is not an integer

        This metod will raise a ValueError if the index is invalid

       

        Parameters

        ----------

        index : int

            the index to find the value

        """

        if not isinstance(index, int):

            raise TypeError("index is not an integer")

        if index < 0 or index >= self.size:

            raise ValueError("index is not inside of list")

        next_node = self.__start

        i = 0

        while i < index:

            next_node = next_node.next_node

            i += 1

        return next_node.item

   

    def find(self, value):

        """ Finds the depth of the element on the list

        (the number of elements above it)

       

        It will return -1 if the element is not found

       

        Parameters

        ----------

        value : <any>

            the value to find on the list

        """

        next_node = self.__start

        i = 0

        while next_node is not None:

            if next_node.item == value:

                return i

            next_node = next_node.next_node

            i += 1

        return -1

   

    def reset(self):

        """ Resets the iterator back to the beginning by setting current to None

        """

        self.__current = None

       

    def next(self):

        """ Moves the iterator to the next element and returns it.

       

        It will return None at the end of the list

        """

        if self.is_empty:

            return None

        if self.__current is None:

            self.__current = self.__start

        else:

            self.__current = self.__current.next_node

        if self.__current is None:

            return None

        else:

            return self.__current.item

       

    def delete_current(self):

        """ Removes the current item from the list without modifying the item

        such that the iterator will still continue to work

       

        This method will raise a RuntimeError if the current node is None

        """

        if self.__current is None:

            raise RuntimeError("The current node should not be None")

        if self.__current.previous_node is not None:

            self.__current.previous_node.next_node = self.__current.next_node

        else:

            self.__start = self.__current.next_node

        if self.__current.next_node is not None:

            self.__current.next_node.previous_node = self.__current.previous_node

        else:

            self.__end = self.__current.previous_node

        self.__size -= 1      

 

    def copy(self):

        """ This method will return a shallow copy of the list

        """

        list = MyLinkedList()

        next_node = self.__start

        while next_node is not None:

            list.append(next_node.item)

            next_node = next_node.next_node

        return list

 

    def __str__(self):

        """ Returns a string representation of this list

        """

        output = ""

        next_node = self.__start

        while next_node is not None:

            output += "{}\n".format(next_node)

            next_node = next_node.next_node

        return output

 

    @staticmethod

    def test():

        """ Method to test List operations

 

        This is called when the list is executed as a

        a standalone script

       

        It will call each of the methods of the List class

        It DOES NOT check for proper use of exceptions

        """

        list = MyLinkedList()

        print("===EMPTY LIST===")

        print("Size: {} Empty: {} Full: {}".format(

            list.size, list.is_empty, list.is_full))

       

        print("===APPEND===")

        list.append(1)

        list.append(2)

        list.append(3)

        print(list)

       

        print("===PREPEND===")

        list.prepend(1)

        list.prepend(2)

        list.prepend(3)

        print(list)

       

        print("===INSERT===")

        list.insert(1, 3)

        list.insert(2, 3)

        list.insert(3, 3)

        print("Size: {} Empty: {} Full: {}".format(

            list.size, list.is_empty, list.is_full))

        print(list)

 

        print("===PEEK===")

        print(list.peek())

       

        print("===PEEK LAST===")

        print(list.peek_last())

       

        print("===GET===")

        print(list.get(2))

        print(list.get(4))

       

        print("===FIND===")

        print(list.get(1))

        print(list.get(2))

        print(list.get(3))

        print(list.find(4))

       

        print("===ITERATE===")

        list.reset()

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

        print(list.next())

       

        print("===DELETE CURRENT===")

        list.reset()

        list.next()

        list.next()

        list.next()

        list.next()

        print(list)

        list.delete_current()

        print(list)

       

        print("===REMOVE FIRST===")

        print(list)

        list.remove_first()

        list.remove_first()

        print(list)

       

        print("===REMOVE LAST===")

        print(list)

        list.remove_last()

        list.remove_last()

        print(list)

       

        print("===REMOVE===")

        print(list)

        list.remove(1)

        list.remove(0)

        print(list)

       

        print("===COPY===")

        copy = list.copy()

        print(list)

        print(copy)

 

# Main Guard

if __name__ == "__main__":

    MyLinkedList.test()

import sys


# next_node, previous_node, item
class ListNodeDouble():
    def __init__(self, item, previous_node=None, next_node=None):
        self.__next_node = next_node
        self.__previous_node = previous_node
        self.__item = item

    @property
    def item(self):
        return self.__item
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        self.__next_node = value
    
    @property
    def previous_node(self):
        return self.__previous_node
    
    @previous_node.setter
    def previous_node(self, value):
        self.__previous_node = value
    
    def __str__(self):
        x = None
        y = None
        if self.__previous_node:
            x = self.__previous_node.item
        if self.__next_node:
            y = self.__next_node.item

        return "{} -> {} -> {}".format(str(x), str(self.item), str(y))
    
import sys


class MyQueue():
    def __init__(self, capacity=10):
        if capacity:
            if isinstance(capacity, int):
                if capacity > 0:
                    self.__capacity = capacity
                else:
                    raise ValueError
            else:
                raise TypeError
        #else:
        #    self.__capacity = 10
        self.__capacity = capacity
        #print("queue capacity: {}".format(self.__capacity))
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




from MyLinkedList import *

class MySet():
    def __init__(self):
        self.__container = MyLinkedList()

    @property
    def size(self):
        return self.__container.size
    
    @property
    def is_empty(self):
        return self.__container.is_empty

    @property
    def debug_container(self):
        return self.__container

    def add(self, value):
        if self.contains(value):
            return False
        else:
            self.__container.append(value)
            return True
    
    def remove(self, value):
        self.reset()
        obj = self.__container.next()
        while obj is not None:
            if obj == value:
                self.__container.delete_current()
                return True
            obj = self.__container.next()
        return False
    
    def contains(self, value):
        #print(type(value))
        self.reset()
        obj = self.__container.next()
        #print(obj)
        while obj is not None:
            if obj == value:
                return True
            obj = self.__container.next()
        return False
        
    def reset(self):
        self.__container.reset()

    def next(self):
        return self.__container.next()
    
    def __eq__(self, set):
        if isinstance(set, MySet):
            if set.size != self.size:
                return False
            if set.is_empty and self.is_empty:
                return True
            for i in range(self.__container.size):
                #if self.next() != set.next()
                if self.__container.find(set.next()) == -1:
                    return False
            return True
        else:
            return False

    
    def disjoint(self, set):
        if isinstance(set, MySet):
            if set.is_empty or self.is_empty and not (set.is_empty and self.is_empty):
                return True
            for i in range(self.__container.size):
                if self.__container.find(set.next()) != -1:
                    return False
            return True
        else:
            raise TypeError

    
    def subset(self, set):
        if isinstance(set, MySet):
            if (set.is_empty or self.is_empty) and not ((set.is_empty and self.is_empty)):
                return True
            set.reset()
            for i in range(set.size):
                if self.__container.find(set.next()) == -1:
                    return False
            return True
        else:
            raise TypeError
        
    
    def superset(self, set):
        if isinstance(set, MySet):
            if set.is_empty and self.is_empty:
                return True
            self.reset()
            for i in range(self.size):
                #if self.__container.find(set.next()) == -1:
                if not set.contains(self.__container.next()):
                    return False
            return True
        else:
            raise TypeError
        
    
    def union(self, set):
        if isinstance(set, MySet):
            result = MySet()
            self.reset()
            obj = self.next()
            while obj is not None:
                result.add(obj)
                obj = self.next()
            set.reset()
            obj = set.next()
            while obj is not None:
                result.add(obj)
                obj = set.next()
            return result
        else:
            raise TypeError
    
    def intersection(self, set):
        if isinstance(set, MySet):
            result = MySet()
            self.reset()
            obj = self.next()
            while obj is not None:
                if set.contains(obj):
                    result.add(obj)
                obj = self.next()
            return result
        else:
            raise TypeError

    def difference(self, set):
        if isinstance(set, MySet):
            result = MySet()
            self.reset()
            obj = self.next()
            while obj is not None:
                if not set.contains(obj):
                    result.add(obj)
                obj = self.next()
            return result
        else:
            raise TypeError
        
    
    def copy(self):
        result = MySet()
        result.__container = self.__container.copy()
        return result

    def __str__(self):
        self.reset()
        x = "{" + str(self.__container.next())
        
        for i in range(self.__container.size - 1):
            x = x + "," + str(self.__container.next())
        x = x + "}"
        return x
    
    @staticmethod
    def test():
        """ Method to test MySet operations

        This is called when the set is executed as a
        a standalone script

        It will call each of the methods of the MySet class
        It DOES NOT check for proper use of exceptions
        """
        first = MySet()
        first.add(1)
        first.add(2)
        first.add(3)
        first.add(4)
        first.add(5)

        print("======= SET FIRST ========")
        print(first)
        print("Size: {} Empty: {}".format(first.size, first.is_empty))

        second = MySet()
        second.add(1)
        second.add(3)
        second.add(5)

        print("======= SET SECOND ========")
        print(second)
        print("Size: {} Empty: {}".format(second.size, second.is_empty))

        third = MySet()
        third.add(1)
        third.add(3)
        third.add(5)

        print("======= SET THIRD ========")
        print(third)
        print("Size: {} Empty: {}".format(third.size, third.is_empty))

        fourth = MySet()
        fourth.add(2)
        fourth.add(4)

        print("======= SET FOURTH ========")
        print(fourth)
        print("Size: {} Empty: {}".format(fourth.size, fourth.is_empty))

        print("======= SECOND CONTAINS ========")
        print("1: {}".format(second.contains(1)))
        print("2: {}".format(second.contains(2)))
        print("3: {}".format(second.contains(3)))
        print("4: {}".format(second.contains(4)))
        print("5: {}".format(second.contains(5)))

        print("======= SECOND ADD & REMOVE ========")
        print("Remove 3 True: {}".format(second.remove(3)))
        print("Remove 3 False: {}".format(second.remove(3)))
        print("Add 3 True: {}".format(second.add(3)))
        print("Add 3 False: {}".format(second.add(3)))

        print("======= FIRST ITERATE ========")
        first.reset()
        item = first.next()
        #print("item: {}".format(item))
        while item is not None:
            print(item)
            item = first.next()

        print("======= EQUALS ========")
        print("First EQUALS Second False: {}".format(first == second))
        print("second: {}".format(second.__str__()))
        print("third: {}".format(third.__str__()))
        print("Second EQUALS Third True: {}".format(second == third))
        print("using __eq")
        print("First EQUALS Second False: {}".format(first.__eq__(second)))
        print("Second EQUALS Third True: {}".format(second.__eq__(third)))


        print("======= DISJOINT ========")
        print("First DISJOINT Second False: {}".format(first.disjoint(second)))
        print("Second DISJOINT Fourth True: {}".format(second.disjoint(fourth)))

        print("======= SUBSET ========")
        print("First SUBSET Second False: {}".format(second.subset(first)))
        print("Second SUBSET First True: {}".format(first.subset(second)))

        print("======= SUPERSET ========")
        print("First SUPERSET Second True: {}".format(second.superset(first)))
        print("Second SUPERSET First False: {}".format(first.superset(second)))

        print("======= UNION ========")
        print("First UNION Second: {}".format(first.union(second)))
        print("Second UNION Fourth: {}".format(second.union(fourth)))

        print("======= INTERSECTION ========")
        print("First INTERSECTION Second: {}".format(first.intersection(second)))
        print("Second UNION Fourth: {}".format(second.intersection(fourth)))

        print("======= DIFFERENCE ========")
        print("First DIFFERENCE Second: {}".format(first.difference(second)))
        print("Second DIFFERENCE Fourth: {}".format(second.difference(fourth)))

        print("======= COPY ========")
        fifth = fourth.copy()
        print(fourth)
        print(fifth)

# Main Guard
if __name__ == "__main__":
    MySet.test()


from MySet import MySet
from MyQueue import MyQueue
import sys

class Powerset:
    
    def __init__(self):
        pass
    def powerset(self, set):
        #print("size of set: {}".format(set.size))
        #print("shall be capacity: {}".format(x))
        queue = MyQueue(2 ** (set.size + 1))
        output = MySet()
        empty = MySet()
        queue.enqueue(empty)
        while not queue.is_empty:
            current = queue.dequeue()
            if output.add(current):
                set.reset()
                item = set.next()
                while item is not None:
                    if current.add(item):
                        queue.enqueue(current.copy())
                        current.remove(item)
                    item = set.next()
        return output


    @staticmethod
    def main(args):
        """ Method to test Powerset operations

        This is called when the program is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        powerset function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        pset = Powerset()
        with open(args[1]) as scanner:
            aset = MySet()
            line = scanner.readline()
            while len(line) > 0:
                aset.add(int(line))
                line = scanner.readline()
            print(pset.powerset(aset))


# main guard
if __name__ == "__main__":
    Powerset.main(sys.argv)
