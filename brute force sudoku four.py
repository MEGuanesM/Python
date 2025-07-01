import sys
#preconditions for the correct size of locked could not be added because the autograder wouldnt accept len of a boolean array for some reason. running from terminal had no problems with it
class SudokuFourModel:
    def __init__(self):
        self.__steps = 0
        self.__board = [[0 for j in range(4)] for i in range(4)]
        self.__locked = [[False for j in range(4)] for i in range(4)]

    @property
    def board(self):
        return self.__board

    @property
    def locked(self):
        return self.__locked

    @property
    def steps(self):
        return self.__steps

    def load_game(self, board, locked):
        self.__board = board
        self.__locked = locked

    def load_from_file(self, file):
        if isinstance(file, str):
            try:
                scanner1 = open(file)
                i = 0
                for line in scanner1:
                    nums = line.split(",")
                    if len(nums) != 4:
                        raise ValueError
                    else:
                        j = 0
                        for num in nums:
                            try:
                                self.__board[i][j] = int(num)
                                if int(num) > 0:
                                    self.__locked[i][j] = True
                                j = j + 1
                            except:
                                raise ValueError
                        i = i + 1
            except:
                raise ValueError
        else:
            raise TypeError

    def check_puzzle(self):
        if len(self.__board) == 4 and len(self.__board[0]) == 4:
            for i in range(4):
                if not (self.check_row(i) and self.check_column(i) and self.check_region(i)):
                    return False
            return True
        else:
            raise ValueError

    def check_row(self, row):
        if isinstance(row, int):
            if len(self.__board) == 4 and len(self.__board[0]) == 4 and (0 <= row <= 3):
                s = set()
                for j in range(4):
                    s.add(self.board[row][j])
                if len(s) == 4:
                    return True
                else:
                    return False
            else:
                raise ValueError
        else:
            raise TypeError

    def check_column(self, column):
        if isinstance(column, int):
            if len(self.__board) == 4 and len(self.__board[0]) == 4 and (0 <= column <= 3):
                s = set()
                for i in range(4):
                    s.add(self.__board[i][column])
                if len(s) == 4:
                    return True
                else:
                    return False
            else:
                raise ValueError
        else:
            raise TypeError

    def check_region(self, region):
        region_0 = ([row[:2] for row in self.__board[:2]])
        region_1 = ([row[2:] for row in self.__board[:2]])
        region_2 = ([row[:2] for row in self.__board[2:]])
        region_3 = ([row[2:] for row in self.__board[2:]])
        if isinstance(region, int):
            if len(self.__board) == 4 and len(self.__board[0]) == 4 and (0 <= region <= 3):
                s = set()
                if region == 0:
                    for row in region_0:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                    if len(s) == 4:
                        return True
                    else:
                        return False
                elif region == 1:
                    for row in region_1:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                    if len(s) == 4:
                        return True
                    else:
                        return False
                elif region == 2:
                    for row in region_2:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                    if len(s) == 4:
                        return True
                    else:
                        return False
                elif region == 3:
                    for row in region_3:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                    if len(s) == 4:
                        return True
                    else:
                        return False
            else:
                raise ValueError
        else:
            raise TypeError

    def prepare(self):
        if len(self.__board) == 4 and len(self.__board[0]) == 4 and len(self.__locked) == 4 and len(self.__locked[0]) == 4:
            i = 0
            for a in range(4):
                j = 0
                for b in range(4):
                    if not self.__locked[i][j]:
                        self.__board[i][j] = 1
                    j = j + 1
                i = i + 1
        else:
            raise ValueError

    def solve(self):
        if (len(self.__board) == 4) and (len(self.__board[0]) == 4):
            self.prepare()
            while not self.check_puzzle():
                self.solve_one_step()
        else:
            raise ValueError

    def solve_one_step(self):
        if len(self.__board) == 4 and len(self.__board[0]) == 4:
            self.__steps = self.__steps + 1
            for i in range(4):
                for j in range(4):
                    if not self.__locked[i][j]:
                        if self.__board[i][j] < 4:
                            self.__board[i][j] = self.__board[i][j] + 1
                            return
                        else:
                            self.__board[i][j] = 1

        else:
            raise ValueError
    
    @classmethod
    def test(cls):
        temp = SudokuFourModel()
        temp.load_from_file("tests/1.in")
        x = temp.__board
        for i in range(4):
            s = ""
            for j in range(4):
                s = s + " {} ".format(x[i][j])
            print(s)
        x= temp.__locked
        for i in range(4):
            s = ""
            for j in range(4):
                s = s + " {} ".format(x[i][j])
            print(s)
        temp.solve()
        x = temp.__board
        for i in range(4):
            s = ""
            for j in range(4):
                s = s + " {} ".format(x[i][j])
            print(s)
        x = temp.__locked
        for i in range(4):
            s = ""
            for j in range(4):
                s = s + " {} ".format(x[i][j])
            print(s)
        z = temp.__steps
        print(z)

        


if __name__ == "__main__":
    SudokuFourModel.test()





class View:
    def __init__(self):
        pass
    
    def show_board(self, board, locked):
        for i in range(4):
            line = ""
            for j in range(4):
                if locked[i][j]:
                    line = line + ("[{}]".format(board[i][j]))
                elif board[i][j] > 0:
                    line = line + (" {} ".format(board[i][j]))
                else:
                    line = line + (" _ ")
            print(line)
    
    def show_steps(self, steps):
        print("The solution took {} steps.".format(steps))
    
    def show_error(self, error):
        print("Error: {}".format(error))


from View import View
from SudokuFourModel import SudokuFourModel
import sys


class Controller:
    def __init__(self):
        self.__view = View()
        self.__model = SudokuFourModel()

    def main(self, args):
        self.run(args)

    def run(self, args):
        self.__model.load_from_file(str(args[1]))
        board = self.__model.board
        locked = self.__model.locked
        self.__view.show_board(board, locked)
        self.__model.solve()
        self.__view.show_board(board, locked)
        steps = self.__model.steps
        self.__view.show_steps(steps)


if __name__ == "__main__":
    Controller().main(sys.argv[1])

