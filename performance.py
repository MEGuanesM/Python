import sys
from time import time


class Slow:

    def __init__(self):
        """ Initializes the class and creates the ignored words list        
        """
        self.__ignore = ["your", "you", "year", "would", "work", "with", "will", "who", "which", "when", "what", "well", "we", "way", "want", "use", "us", "up", "two", "to", "time", "this", "think", "they", "these", "there", "then", "them", "their", "the", "that", "than", "take", "some", "so", "she", "see", "say", "people", "over", "out", "our", "other", "or", "only", "one", "on", "of", "now", "not", "no", "new", "my", "most", "me", "make", "look", "like", "know", "just", "its", "it", "into", "in", "if", "i", "how", "his", "him", "her", "he", "have", "good", "go", "give", "get", "from", "for", "first", "even", "do", "day", "could", "come", "can", "by", "but", "because", "be", "back", "at", "as", "any", "and", "an", "also", "all", "after", "about", "a"]

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
        indexer = Slow()
        with open(args[1]) as scanner:
            start = time()
            index = indexer.index(scanner, indexer.__ignore)
            end = time()
            elapsed = (end - start) * 1000
            indexer.print_results(index)
            print("Unique Words: {}".format(len(index)))
            print("Time Elapsed: {} ms".format(elapsed))

    def index(self, scanner, ignore):
        if scanner is not None and ignore is not None:
            """ Method to create the index

            Params:
            -------
            scanner: an opened file object
            ignore: a list of words to be ignored
            """
            index = []
            cur_line = 1
            for line in scanner: #runs troguth each line
                flag = False
                text = line.strip()
                words = text.split(" ")
                #print(words)
                #print(words)
                for word in words: #for each word in the line we repeat
                    #print(word)
                    flag = False
                    if word not in ignore: #only if the word is not part of the ignored words
                        #print("not in ignore")
                        for t in index: #check de index list that contains a tuple of (key, value) = (word, line_appears)
                            #print("t[0]: {} word: {} t[1]: {}".format(t[0], word, t[1]))
                            if t[0] == word: #if any of the elements inside the tuple at the key position equals the word then we append the new line to the end of the value position of the tuple
                                flag = True
                                #print("lalalalallalalalalalallalaalala")
                                if cur_line not in t[1]:
                                    t[1].append(cur_line)
                                    #print("xxxxxxxxxnot in t[1]")
                                #word in index 
                                #if isinstance(t[1], list):
                                 #   if cur_line not in t[1]:
                                 #       t[1].append(cur_line)
                                #else:
                                #    if cur_line != t[1]:
                                #        t[1].append(cur_line)
                        #print(flag)
                        if flag == False: #if the 
                            #print("t[0] not word")
                            new_list = []
                            new_list.append(cur_line)
                            new_tuple = (word, new_list)
                            index.append(new_tuple)
                        
                cur_line = cur_line + 1

            
            # =================================
            # create the index here
            # =================================
            #print(index)
            #print(len(index))
            return index

    def print_results(self, index):
        """ Method to print the index

        Params:
        -------
        index: the created index returned from index()
        """
        # =================================
        # sort and print the index here
        # =================================
        index.sort()
        #print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>")
        for line in index:
            line[1].sort()

        for line in index:
            x = str(line[1])
            x = x.replace('[', '')
            x = x.replace(']', '')
            x = x.replace(' ', '')
            print("{} {}".format(line[0], x))



# main guard
if __name__ == "__main__":
    Slow.main(sys.argv)


import sys
from time import time


class Fast:

    def __init__(self):
        """ Initializes the class and creates the ignored words list        
        """
        self.ignore = {"your", "you", "year", "would", "work", "with", "will", "who", "which", "when", "what", "well", "we", "way", "want", "use", "us", "up", "two", "to", "time", "this", "think", "they", "these", "there", "then", "them", "their", "the", "that", "than", "take", "some", "so", "she", "see", "say", "people", "over", "out", "our", "other", "or", "only", "one", "on", "of", "now", "not", "no", "new", "my", "most", "me", "make", "look", "like", "know", "just", "its", "it", "into", "in", "if", "i", "how", "his", "him", "her", "he", "have", "good", "go", "give", "get", "from", "for", "first", "even", "do", "day", "could", "come", "can", "by", "but", "because", "be", "back", "at", "as", "any", "and", "an", "also", "all", "after", "about", "a"}

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
        indexer = Fast()
        with open(args[1]) as scanner:
            start = time()
            index = indexer.index(scanner, indexer.ignore)
            end = time()
            elapsed = (end - start) * 1000
            indexer.print_results(index)
            print("Unique Words: {}".format(len(index)))
            print("Time Elapsed: {} ms".format(elapsed))

    def index(self, scanner, ignore):
        """ Method to create the index

        Params:
        -------
        scanner: an opened file object
        ignore: a list of words to be ignored
        """
        index = {}
        
        # =================================
        # create the index here
        # =================================
        if scanner is not None and ignore is not None:
            index = {} #shall be a dictionary
            # dict2 = {"key1": 1, "test2": 2}
            line_number = 1
            for line in scanner:
                text = line.strip()
                words = text.split(" ")
                for word in words:
                    if word not in ignore:
                        #print("line: {} word: {}".format(line_number, word))
                        if index.get(word):
                            x = index.get(word) #set
                            #print("current set of lines: {} for word {}".format(x, word))
                            x.add(line_number)
                            #print("set of lines after adding new number: {}".format(x))
                            index.update({word: x})
                        else:
                            new_set = set()
                            new_set.add(line_number)
                            index.update({word: new_set})
                line_number = line_number + 1

        return index

    def print_results(self, index):
        """ Method to print the index

        Params:
        -------
        index: the created index returned from index()
        """
        # =================================
        # sort and print the index here
        # =================================
        for x, y in sorted(index.items()):
            t = str(y)
            #jane {1, 2, 4}
            t = t.replace('{', '')
            t = t.replace('}', '')
            t = t.replace(' ', '')
            print(x, t)
# main guard
if __name__ == "__main__":
    Fast.main(sys.argv)
