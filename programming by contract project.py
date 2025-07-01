import math
class Project():
    @staticmethod
    def main(args):
        pass

    def __init__(self):
        pass

    def quadratic_equation(self, a, b, c): 
        self.__a = a #a<> 0
        self.__b = b 
        self.__c = c
        #b*b - 4ac >=0
        if isinstance(self.__a, int) and isinstance(self.__b, int) and isinstance(self.__c, int):
            if self.__a != 0 and (self.__b * self.__b - (4 * self.__a * self.__c)) >= 0:
                return (-self.__b + (math.sqrt(self.__b * self.__b - (4 * self.__a * self.__c)))) / (2 * self.__a) + (-self.__b - (math.sqrt(self.__b * self.__b - (4 * self.__a * self.__c)))) / (2 * self.__a)
            else:
                raise ValueError
        else:
            raise TypeError

    def is_palindrome(self, sentence):
        self.__sentence = sentence

        if isinstance(self.__sentence, str) and len(self.__sentence) > 0 and  self.__sentence.islower() and self.__sentence.isalpha():
            is_palindrome = True
            reversed = self.__sentence[::-1]
            for c in range (0,int((len(self.__sentence)) / 2),1):
                if self.__sentence[c] != reversed[c]:
                    is_palindrome = False
            return is_palindrome
        else:
            raise ValueError
    
    def is_cycle(self, array):
        self.__array = array
#1 0 2 false
# i = 0 /// false true false 
# i = 1 ///
# 
# 2 0 1 true
        if isinstance(self.__array, list) and len(self.__array) > 0:
            seen = [False] * len(self.__array)
            flag = False
            index = 0
            First = True
            count = 0
            while False in seen: 
                # need a starting point
                if First:
                    index = self.__array[0] # now index contains 2 need to go to that place
                    First = False
                    seen[0] = True 
                else:
                    if count < len(seen):
                        seen[index] = True
                        index = self.__array[index]
                        count = count + 1


                    else:
                        return False

            return True



    def base_converter(self, value, base):
        self.__value = value
        self.__base = base

        numbers = "0123456789"
        if isinstance(self.__value, str) and isinstance(self.__base, int):
            new_value = 0
            base_place = 1
            reversed = self.__value[::-1]
            for num in reversed:
                if num not in numbers or int(num) >= self.__base:
                    raise ValueError
                else:
                    new_value = new_value + int(num) * self.__base ** (base_place - 1)
                    base_place = base_place + 1
            return new_value
        else:
            raise TypeError

    def time_difference(self, start_hour, start_minute, start_second, end_hour, end_minute, end_second):
        self.__start_hour = start_hour
        self.__start_minute = start_minute
        self.__start_second = start_second
        self.__end_hour = end_hour
        self.__end_minute = end_minute
        self.__end_second = end_second

        if isinstance(self.__start_hour, int) and isinstance(self.__start_minute, int) and isinstance(self.__start_second, int) and isinstance(self.__end_hour, int) and isinstance(self.__end_minute, int) and isinstance(self.__end_second, int):
            if self.__start_hour in range(1,23,1) and self.__end_hour in range(1,23,1) and self.__start_minute in range(0,59,1) and self.__end_minute in range(0,59,1) and self.__start_second in range(0,59,1) and self.__end_second in range(0,59,1):
                if  self.__start_hour > self.__end_hour:
                    raise ValueError
                elif self.__start_hour < self.__end_hour:
                    return ((self.__end_hour - self.__start_hour) * 3600) + ((self.__end_minute * self.__start_minute) * 60) + (self.__end_second - self.__start_second)

                else: 
                    if self.__start_minute > self.__end_minute:
                        raise ValueError
                    elif self.__start_minute < self.__end_minute:
                        return ((self.__end_minute * self.__start_minute) * 60) + (self.__end_second - self.__start_second)
                    else:
                        if self.__start_second > self.__end_second:
                            raise ValueError
                        elif self.__start_second < self.__end_second:
                             return self.__end_second - self.__start_second
                        else:
                            raise ValueError
            else:
                raise ValueError
        else:
            raise TypeError 
            
        
            

