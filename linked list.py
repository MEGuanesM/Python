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
    from ListNodeDouble import *
import sys


#start end current size
class MyLinkedList():
    def __init__(self):
        self.__start = None
        self.__end = None
        self.__current = None
        self.__size = [None]

    @property
    def size(self):
        if isinstance(self.__size, list):
            return 0
        return int(self.__size)

    @property
    def is_full(self):
        return False

    @property
    def is_empty(self):
        if isinstance(self.__size, list):
            return True
        else:
            return (self.__size == 0)

    @property
    def debug_start(self):
        return self.__start

    @property
    def debug_end(self):
        return self.__end

    @property
    def debug_current(self):
        return self.__current

    def append(self, value):
        node = ListNodeDouble(value)
        if self.size == 0:
            self.__end = node
            self.__start = node
            #print("end")
            #print(self.__end)
            self.__size = 0
        else:
            #print(self.__size)
            #print(self.size)
            #print(self.__end)
            #print(self.__start)
            #print("node")
            #print(node)
            #print("lala")
            #print(self.__end.next_node)
            self.__end.next_node = node
            node.previous_node = self.__end
            self.__end = node
        self.__size = self.__size + 1

    def prepend(self, value):
        node = ListNodeDouble(value)
        if self.size == 0:
            self.__start = node
            self.__end = node
            self.__size = 1
        else:
            self.__start.previous_node = node
            node.next_node = self.__start
            self.__start = node
            self.__size = self.__size + 1

    def insert(self, value, index):
        if index < 0 or (index > self.size):
            raise ValueError
        elif index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            node = ListNodeDouble(value)
            self.__current = self.__start
            for i in range(0, index - 1):
                self.__current = self.__current.next_node
            node.next_node = self.__current.next_node
            node.previous_node = self.__current
            node.next_node.previous_node = node
            self.__current.next_node = node
            self.__size = self.__size + 1 

    def remove_first(self):
        if self.size == 0:
            raise RuntimeError
        else:
            temp = self.__start
            self.__start = self.__start.next_node
            if self.__start is None:
                self.__end = None
            else:
                self.__start.previous_node = None
            self.__size = self.__size - 1
            return temp.item

    def remove_last(self):
        if self.size == 0:
            raise RuntimeError
        else:
            temp = self.__end
            self.__end = self.__end.previous_node
            if self.__end is None:
                self.__start = None
            else:
                self.__end.next_node = None
            self.__size = self.__size - 1
            return temp.item

    def remove(self, index):
        if index < 0 or index > (self.size - 1):
            raise ValueError
        elif index == 0:
            return self.remove_first()
        elif index == self.size:
            return remove_last()
        else:
            self.__current = self.__start.next_node
            for i in range(1, index - 1):
                self.__current = self.__current.next_node
            self.__current.next_node.previous_node = self.__current.previous_node
            self.__current.previous_node.next_node = self.__current.next_node
            self.__size = self.__size - 1
            return self.__current.item

    def peek(self):
        if self.is_empty:
            return RuntimeError
        else:
            return self.__start.item

    def peek_last(self):
        if self.is_empty:
            return RuntimeError
        else:
            return self.__end.item

    def get(self, index):
        if isinstance(index, int):
            if 0 <= index < self.size:
                node = self.__start
                for i in range(0, index):
                    node = node.next_node
                return node.item

            else:
                raise ValueError
        else:
            raise TypeError

    def find(self, value):
        index = 0
        node = self.__start
        if node.item == value:
            return index
        for i in range(1, self.size):
            node = node.next_node
            index = index + 1
            if node.item == value:
                return index
        return -1
    
    def reset(self):
        self.__current = None
    
    def next(self):
        if self.is_empty:
            return None
        if self.__current is None:
            #print("aqui!!")
            self.__current = self.__start
        else:
            self.__current == self.__current.next_node
            #print("next node!!")
        if self.__current is None:
            return None
        else:
            return self.__current.item

    def delete_current(self):
        self.reset()
        self.next()
        self.__current.next_node
        #print("self current {}".format(self.__current))
        if self.__current is None:
            raise RuntimeError
        if self.__current.previous_node is not None:
            self.__current.previous_node.next_node = self.__current.next_node
        else:
            self.__start = self.__current.next_node
        if self.__current.next_node is not None:
            self.__current.next_node.previous_node = self.__current.previous_node
        else:
            self.__end = self.__current.previous_node
        self.__current = self.__current.previous_node
        self.__size = self.__size - 1

    def copy(self):
        x = MyLinkedList()
        x.__start = self.__start
        x.__end = self.__end
        x.__current = self.__current
        x.__size = self.__size
        return x

    def __str__(self):
        self.reset()
        x = ""
        self.__current = self.__start
        for i in range(0, self.size):
            x = x + self.__current.__str__()
            x = x + "\n"
            self.__current = self.__current.next_node
        return x
        
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
        print(list.__str__())

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
        print("start")
        print(list.__start)
        print("end")
        print(list.__end)
        print("current")
        print(list.__current)
        print("isempty")
        print(list.is_empty)
        list.delete_current()
        print(list)
        print("delete ok")

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


from MyLinkedList import *
import sys


class Sieve:
    
    def __init__(self):
        pass
        

    @staticmethod
    def main(args):
        """ Method to test Sieve operations

        This is called when the program is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        sieve_of_eratosthenes function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        sieve = Sieve()
        with open(args[1]) as scanner:
            print(sieve.sieve_of_eratosthenes(int(scanner.readline())))


# main guard
if __name__ == "__main__":
    Sieve.main(sys.argv)
