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
from MyLinkedList import *


class MyHashMap():
    def __init__(self, capacity=16):
        if not isinstance(capacity, int):
            raise TypeError
        if capacity <= 0:
            raise ValueError
        self.__container = [MyLinkedList() for i in range(capacity)]
        self.__size = 0
        self.__load_factor = 0.75

    @property
    def size(self):
        return self.__size
    
    @property
    def capacity(self):
        return len(self.__container)
    
    @property
    def is_empty(self):
        return self.__size == 0
    
    @property
    def debug_container(self):
        return self.__container
    
    def compute_index(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        index = self.compute_index(key)
        self.__container[index].reset()
        current = self.__container[index].next()
        #print(type(current))
        while current is not None:
            #print(type(current))
            #print("current[0]: {} current[1]: {}".format(current[0], current[1]))
            #print("key: {}".format(key))
            if current[0] == key:
                self.__container[index].delete_current()
                #i = self.__container[index].find(current)
                #print("lalalala")
                #print(type(current))
                #print("type container index:{}".format(self.__container[index]))
                #self.__container[index].insert((key, value), i)
                #self.__container[index].remove(i + 1)
                #self.__container[index].__item = (1, 1)
                #self.__container[index].remove(i)
                self.__container[index].append((key, value))
                return
            current = self.__container[index].next()
        self.__container[index].append((key, value))
        self.__size = self.__size + 1
        if self.__size / self.capacity > self.__load_factor:
            self.__double_capacity()
        
    def __double_capacity(self):
        new_capacity = self.capacity * 2
        new_container = [MyLinkedList() for i in range(new_capacity)]
        for i in range(self.capacity):
            self.__container[i].reset()
            node = self.__container[i].next()
            while node is not None:
                key, value = node[0], node[1]
                #new_index = self.compute_index(key)
                new_index = hash(key) % new_capacity
                new_container[new_index].append((key, value))
                node = self.__container[i].next()
        self.__container = new_container
    
    def get(self, key):
        index = self.compute_index(key)
        self.__container[index].reset()
        current = self.__container[index].next()
        while current is not None:
            if current[0] == key:
                return current[1]
            current = self.__container[index].next()
        return None
    
    def remove(self, key):
        index = self.compute_index(key)
        self.__container[index].reset()
        current = self.__container[index].next()
        while current is not None:
            if current[0] == key:
                self.__container[index].delete_current()
                self.__size = self.__size - 1
                return current[1]
            current = self.__container[index].next()
        return None
    
    def contains_key(self, key):
        return self.get(key) is not None
    
    def contains_value(self, value):
        for i in range(self.capacity):
            self.__container[i].reset()
            current = self.__container[i].next()
            while current is not None:
                if current[1] == value:
                    return True
                current = self.__container[i].next()
        return False
    
    def copy(self):
        new_map = MyHashMap(self.capacity)
        for i in range(self.capacity):
            self.__container[i].reset()
            current = self.__container[i].next()
            while current is not None:
                new_map.put(current[0], current[1])
                current = self.__container[i].next()
        return new_map

    def __str__(self):
        r = ""
        for i in range(self.capacity):
            self.__container[i].reset()
            current = self.__container[i].next()
            while current is not None:
                r = r + "({}, {})".format(current[0], current[1])
                r = r + "\n"
                current = self.__container[i].next()
        return r
    @staticmethod
    def test2():

        map = MyHashMap(4)

        print ("putting ('A', 2)")

        map.put("A", 2)

        print("printing map Expecting (A,2)")

        print(map.__str__())

        print ("putting ('A', 5)")

        map.put("A", 5)

        print("printing map Expecting (A,5)")

        print(map.__str__())
    
    @staticmethod
    def test():
        """ Method to test map operations

        This is called when the map is executed as a
        a standalone script

        It will call each of the methods of the map class
        It DOES NOT check for proper use of exceptions
        """
        map = MyHashMap(4)
        print("===EMPTY MAP===")
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))

        print("===PUT===")
        map.put(1, 4)
        map.put(2, 5)
        map.put(3, 6)
        print(map.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        print(*map.debug_container)

        print("===GET===")
        print(map.get(1))
        print(map.get(2))
        print(map.get(3))
        print(map.get(4))

        print("===CONTAINS KEY===")
        print(map.contains_key(1))
        print(map.contains_key(2))
        print(map.contains_key(3))
        print(map.contains_key(4))

        print("===CONTAINS VALUE===")
        print(map.contains_value(4))
        print(map.contains_value(5))
        print(map.contains_value(6))
        print(map.contains_value(3))

        print("===PUT AND DOUBLE===")
        map.put(4, 3)
        map.put(5, 2)
        map.put(6, 1)
        print(map.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        print(*map.debug_container)

        print("===PUT AND REPLACE===")
        map.put(4, 5)
        map.put(4, 5)
        map.put(4, 5)
        map.put(4, 5)
        map.put(4, 5)
        map.put(4, 5)
        map.put(5, 6)
        map.put(6, 4)
        print(map.__str__())

        print("===COPY===")
        copy = map.copy()
        print(map.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        # print(*map.debug_container)
        print("======")
        print(copy.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        # print(*map.debug_container)

        print("===REMOVE===")
        print(map.remove(4))
        print(map.remove(5))
        print(map.remove(6))
        print(map.remove(6))
        print(map.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        print(*map.debug_container)

        print(map.remove(3))
        print(map.remove(2))
        print(map.remove(1))
        print(map.remove(1))
        print(map.__str__())
        print("Size: {} Capacity: {} Empty: {}".format(map.size, map.capacity, map.is_empty))
        print(*map.debug_container)

    @staticmethod
    def test3():
        map = MyHashMap(4)
        map.put(4, 5)
        print(map)
        print(*map.debug_container)
        map.put(4, 5)
        map.put(4, 6)
        print(map)
        print(*map.debug_container)





# Main Guard
if __name__ == "__main__":
    MyHashMap.test()


from MyHashMap import MyHashMap
import sys

class SearchIndexer:
    
    def __init__(self):
        pass

    @staticmethod
    def main(args):
        """ Method to test SearchIndexer operations

        This is called when the program is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        index function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        indexer = SearchIndexer()
        with open(args[1]) as scanner:
            indexer.print_results(indexer.index(scanner))
    
    def index(self, scanner):
        map = MyHashMap()
        map.put("A", 0)
        map.put("B", 0)
        map.put("C", 0)
        map.put("D", 0)
        map.put("E", 0)
        map.put("F", 0)
        map.put("G", 0)
        map.put("H", 0)
        map.put("I", 0)
        map.put("J", 0)
        map.put("K", 0)
        map.put("L", 0)
        map.put("M", 0)
        map.put("N", 0)
        map.put("O", 0)
        map.put("P", 0)
        map.put("Q", 0)
        map.put("R", 0)
        map.put("S", 0)
        map.put("T", 0)
        map.put("U", 0)
        map.put("V", 0)
        map.put("W", 0)
        map.put("X", 0)
        map.put("Y", 0)
        map.put("Z", 0)
        #print(map.__str__())
        for line in scanner:
            #print(line)
            name, sex, count = line.strip().split(",")
            first_letter = name[0].upper()
            #print("first: {} count: {} ".format(first_letter, count))
            counted = map.get(str(first_letter))
            if counted is None:
                print(line)
                print(count)
                print(counted)
            map.put(first_letter, int(counted) + int(count))

        return map

    def print_results(self, res):
        print(res.__str__())


# main guard
if __name__ == "__main__":
    SearchIndexer.main(sys.argv)
