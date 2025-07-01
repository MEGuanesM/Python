import sys
from time import time
from collections import deque

class Matcher:

    def __init__(self):
        """ Initializes the class and creates the ignored words list        
        """
        self.__brackets = {'[': ']', '{' : '}', '<' : '>', '(' : ')'}
    @staticmethod
    def main(args):
        """ Method to test Indexer operations

        This is called when the program is executed as a
        a standalone script

        It will simply pass the contents of the input file to the
        index function and print the result

        Params:
        -------
        args: the command-line arguments
        """
        matcher = Matcher()
        try:
          with open(args[1]) as scanner:
              for line_num, line in enumerate(scanner, 1):
                #print(line)
                line = line.strip()
                #print("ok")
                #if not any([matcher.is_open(char) or matcher.is_close(char) for char in line]):
                #  matcher.out(line_num, line, "No Brackets")
                #else:
                #  matcher.check(line_num, line)

                bracket = False
                for c in line:
                  #print("ok for loop char")
                  if matcher.is_open(c) or matcher.is_close(c):
                    #print("ok3")
                    bracket = True
                    break
                #print("ok4")
                if not bracket:
                  #print("ok5")
                  matcher.out(line_num, line, "No Brackets")
                else:
                  #print("ok6")
                  matcher.check(line_num, line)

                  
              #print("ok")



        except FileNotFoundError:
          print("File Error")
        except Exception as E:
          print("File Error {}".format(E))



    def check(self, line_num, line):
      stack = deque()
      for i, char in enumerate(line):
        if self.is_open(char):
          stack.append(char)
        elif self.is_close(char):
          if not stack:
            #write Error
            self.out(line_num, line, "{} at index {}, does not have opening bracket".format(char, i))
            return
          top = stack.pop()
          if self.matching_open_bracket(char) != top:
            #write log
            self.out(line_num, line, "{} at index {}, does not match {} at index {}".format(char, i, top, (len(line) - len(stack) - i)))
            return
      
      if stack:
        open_bracket = stack.pop()
        #write log
        self.out(line_num, line, "{} at index {}, does not have closing bracket".format(open_bracket, (len(line) - len(stack) - 1)))
      else:
        #log ok
        self.out(line_num, line, "brackets Match")
          

    def is_open(self, c):
      return c in self.__brackets.keys()
    
    def is_close(self, c):
      return c in self.__brackets.values()
    
    def matching_open_bracket(self, c):
      for open, close in self.__brackets.items():
        if close == c:
          return open
      return None
    
    def out(self, line_num, line, result):
      with open("Report.txt", "a") as report_result:
        report_result.write("Line {}: {}\n".format(line_num, line))
        report_result.write(result)
        report_result.write("\n\n")

    




        


# main guard
if __name__ == "__main__":
    Matcher.main(sys.argv)
