import sys


class MyStack():
    def __init__(self, capacity):
        self.__array = [None for x in range(capacity)]
        self.__capacity = capacity
        self.__top = -1

    @property
    def top(self):
        if self.is_empty:
            self.__top = -1
        return self.__top

    @property
    def array(self):
        return self.__array
    
    @property
    def capacity(self):
        return self.__capacity
    

    @property
    def size(self):
        return self.__top + 1

    @property
    def is_full(self):
        return self.__top + 1 == self.__capacity

    @property
    def is_empty(self):
        return self.__top == -1
    
    @property
    def debug_array(self):
        return self.__array

    @property
    def debug_top(self):
        return self.__top
    
    def push(self, value):
        if not self.is_full:
            self.__top = self.__top + 1
            self.__array[self.__top] = value
        else:
            #print("TOP push: {}".format(self.__top))
            raise RuntimeError
    
    def pop(self):
        if not (self.__top == -1):
            self.__top = self.__top - 1
            #print("TOP POP: {}".format(self.__top))
            x = self.__array[self.__top + 1]
            #print("print pop item i = {}".format(x))
            return x
        else:
            #print("TOP: {}".format(self.__top))
            raise RuntimeError
    
    def peek(self):
        if self.is_empty:
            raise RuntimeError
        else:
            x = self.__array[self.__top]
            return x

    def double_capacity(self):
        #print("<<<<<<<<<<OG>>>>>>>>>>>>_____----------------")
        #print(self.__str__2())
        #print("____double type: {}".format(type(self.__array)))
        array2 = MyStack(self.__capacity * 2)
        #print("capacity copy {} ".format(array2.capacity))
        #print("double before copy")
        copy = self.copy()
        for i in range(self.__top + 1):
            array2.push(copy.pop())
        #print("ARRAY 2")
        #print(array2.__str__2())
        #print("ARRAY 2 END")
        #print("2____double type: {}".format(type(self.__array)))
        #print("____  array2 double type: {}".format(type(array2)))
        #print(type(self))
        #print("<<<<array2>>>>>>-------------------------")
        #print(array2.__str__2())
        #print("<<<<array2>>>>>>")
        self.__array = array2.__array
        self.__capacity = array2.__capacity
        self.__top = array2.__top
        #print("<<<<double>>>>>>")
        #print(self.__str__2())
        #print("<<<<double>>>>>>")
        #print(type(self))
        #print("self str")
        #print(self.__str__2())
        #print("self str end")
        #print("3____double type: {}".format(type(self.__array)))
    
    def half_capacity(self):
        #print(type(self.__array))
        if self.__top + 1 > (int(self.__capacity / 2)):
            raise RuntimeError
        else:
            array2 = MyStack(int(self.__capacity / 2))
            #print("half ok")
            copy = self.copy()
            #print("half ok2")
            for i in range(self.__top):
                array2.push(copy.pop())
            self = array2

    def copy(self):
        #print(type(self.__array))
        #print("copy capacity: {}".format(self.__capacity))
        array2 = MyStack(self.__capacity)
        temp = []
        #for i in range(self.__top, -1, -1):
        #print("copy before loop")
        #print("top: {}".format(self.__top))
        for i in range(self.__top + 1):
            #print("loop {}".format(i))
            #array2.push(self.pop())
            temp.append(self.pop())
        #print(temp)
        for i in range(len(temp)):
            self.push(temp[i])
            array2.push(temp[i])
        return array2
        #print(type(self.__array))
 
    def __str__(self):
        r = ""
        for i in range(self.__top, -1, -1):
            r = r + str(self.__array[i]) + "\n"
        return r
    
    def __str__2(self):
        r = ""
        for i in range(self.__capacity - 1, -1, -1):
            r = r + str(self.__array[i]) + "\n"
        return r

    @staticmethod
    def test():
        stack = MyStack(10)
        print("===EMPTY STACK===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("x type: {}".format(type(stack.__array)))
        for i in range(0, 20, 2):
            stack.push(i)
        print("===ADD 10 ELEMENTS===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("{}".format(stack))
        print("xx type: {}".format(type(stack.__array)))
        print("===FIND===")
        print("Depth of 16: {}".format(stack.find(16)))
        print("Depth of 12: {}".format(stack.find(12)))
        print("Depth of  8: {}".format(stack.find(8)))
        print("Depth of  4: {}".format(stack.find(4)))
        print("Depth of  5: {}".format(stack.find(5)))
        print("type: {}".format(type(stack.__array)))
        print("xyx type: {}".format(type(stack.__array)))
        stack.double_capacity()
        print("xxx type: {}".format(type(stack.__array)))
        print("===DOUBLE===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("xxxx type: {}".format(type(stack.__array)))
        stack.half_capacity()

        print("===HALF===")
        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("ok half")
        stack2 = stack.copy()
        print("copy begins")

        print("===COPY===")
        print("Stack 1 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
        print("{}".format(stack))
        print("Stack 2 - Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack2.size, stack2.capacity, stack2.is_empty, stack2.is_full))
        print("{}".format(stack2))
        print("COPY OK <>><><><><><><")

        print("===PEEK===")
        print("{}".format(stack.peek()))

        print("===POP===")
        while not stack.is_empty:
            print("{}".format(stack.pop()))

        print("Size: {} Capacity: {} Empty: {} Full: {}".format(
            stack.size, stack.capacity, stack.is_empty, stack.is_full))
    
    @classmethod
    def test2(self):
        x = MyStack(10)
        x.push(3)
        x.push(2)
        x.push(1)
        y = x.copy()
        print(y.pop())
        print(y.pop())
        print(y.pop())
        print(y.size)

    def find(self, value):
        copy = self.copy()
        count = 0
        for i in range(self.__top):
            if value == copy.pop():
                return count
            else:
                count = count + 1
        return -1


if __name__ == "__main__":
    MyStack.test2()
        

import sys
from MyStack import MyStack


class PostfixCalculator():
    def __init__(self):
        self.__stack = MyStack(10)

    def debug_stack(self):
        return self.__stack

    def calculate(self, args):
        try:
            scanner1 = open(args[1])
            line = scanner1.readline().strip()
            x = line.split(" ")
            line = x
            #print(line)
            for x in line:
                #print("current item: {}".format(x))
                #print("xsize: {}".format(self.__stack.size))
                #print("xisFull: {}".format(self.__stack.is_full))
                if x.lstrip("-").isdigit():
                    self.read_number(x)
                else:
                    self.read_symbol(x)
                #print("current stack init")
                #print(self.__stack.__str__())
                #print("size: {}".format(self.__stack.size))
                #print("isFull: {}".format(self.__stack.is_full))
                #print("current stack end")
            scanner1.close()
            print(self.__stack.__str__())
        except Exception as e:
            print("Invalid Input")
            #print(e)

    def read_number(self, input):
        #if not isinstance(input, str):
        try:
            input = int(input)
            if self.__stack.is_full:
                #print("doing double")
                #print(type(self.__stack))
                #print(self.__stack.__str__())
                self.__stack.double_capacity()
                #print(self.__stack.__str__())
                #print(type(self.__stack))
                #print("capacity: {}".format(self.__stack.capacity))
                #print("Top: {}".format(self.__stack.top))
                #print("done")
                #print(input)
            #print("normal")
            #print(input)
            #print("here")
            self.__stack.push(input)
            #print("here2")
            #print("normal2")
        except Exception:
            raise TypeError
        #else:
         #   raise ValueError

    def read_symbol(self, input):
        s = ["+","-","*","/"]
        #copy = self.__stack.copy()
        if self.__stack.size > 1:
            if input == "+":
                b = self.__stack.pop()
                a = self.__stack.pop()
                self.__stack.push(a + b)
                #print("suma: {}".format(self.__stack.peek()))
                #print("current stack suma")
                #print(self.__stack.__str__())
                #print("current stack end")
            elif input == "-":
                b = self.__stack.pop()
                a = self.__stack.pop()
                self.__stack.push(a - b)
                #print("resta: {}".format(self.__stack.peek()))
                #print("current stack resta")
                #print(self.__stack.__str__())
                #print("current stack end")
            elif input == "*":
                b = self.__stack.pop()
                a = self.__stack.pop()
                self.__stack.push(a * b)
                #print("mult : {}".format(self.__stack.peek()))
                #print("current stack mult")
                #print(self.__stack.__str__())
                #print("current stack end")
            elif self.__stack.peek() != 0 and input == "/":
                b = self.__stack.pop()
                #print("Top most: {}".format(b))
                a = self.__stack.pop()
                #print(b)
                self.__stack.push(int(a / b))
                #print("div: {}".format(self.__stack.peek()))
                #print("current stack div")
                #print(self.__stack.__str__())
                #print("current stack end")
            elif self.__stack.peek() == 0 and input == "/":
                raise ZeroDivisionError
            else:
                #print("current stack else")
                #print(self.__stack.__str__())
                #print("current stack end")
                #print("zero")
                raise ValueError
        else:
            #print("read_symbol else")
            raise ValueError

    @staticmethod
    def main(args):
        calculator = PostfixCalculator()
        result = calculator.calculate(args)


if __name__ == "__main__":
    PostfixCalculator.main(sys.argv)
