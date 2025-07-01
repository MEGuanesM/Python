import sys
class SudokuNineModel:
    def __init__(self):
        self.__steps = 0
        self.__board = [[0 for j in range(9)] for i in range(9)]
        self.__locked = [[False for j in range(9)] for i in range(9)]

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
                scanner1 = open(file, "r")
                i = 0
                for line in scanner1:
                    #print(line)
                    line.strip()
                    nums = line.split(",")
                    #print(nums)
                    if len(nums) != 9:
                        #print("lalala")
                        raise ValueError
                    else:
                        j = 0
                        for num in nums:
                            try:
                                self.__board[i][j] = int(num)
                                if int(num) > 0:
                                    self.__locked[i][j] = True
                                j = j + 1
                            except Exception:
                                raise ValueError
                        i = i + 1
            except Exception:
                raise ValueError
                
        else:
            raise TypeError

    def check_puzzle(self):
        if len(self.__board) == 9 and len(self.__board[0]) == 9:
            for i in range(9):
                if not (self.check_row(i) and self.check_column(i) and self.check_region(i)):
                    return False
            return True
        else:
            raise ValueError

    def check_row(self, row):
        if isinstance(row, int):
            if len(self.__board) == 9 and len(self.__board[0]) == 9 and (0 <= row <= 8):
                s = set()
                for j in range(9):
                    if self.board[row][j] != 0:
                        s.add(self.board[row][j])
                if len(s) == 9:
                    return True
                else:
                    return False
            else:
                raise ValueError
        else:
            raise TypeError

    def check_column(self, column):
        if isinstance(column, int):
            if len(self.__board) == 9 and len(self.__board[0]) == 9 and (0 <= column <= 8):
                s = set()
                for i in range(9):
                    if self.__board[i][column] != 0:
                        s.add(self.__board[i][column])
                if len(s) == 9:
                    return True
                else:
                    return False
            else:
                raise ValueError
        else:
            raise TypeError

    def check_region(self, region): 
        region_0 = ([row[0:3] for row in self.__board[0:3]])
        region_1 = ([row[3:6] for row in self.__board[0:3]])
        region_2 = ([row[6:9] for row in self.__board[0:3]])
        region_3 = ([row[0:3] for row in self.__board[3:6]])
        region_4 = ([row[3:6] for row in self.__board[3:6]])
        region_5 = ([row[6:9] for row in self.__board[3:6]])
        region_6 = ([row[0:3] for row in self.__board[6:9]])
        region_7 = ([row[3:6] for row in self.__board[6:9]])
        region_8 = ([row[6:9] for row in self.__board[6:9]])
        if isinstance(region, int):
            if len(self.__board) == 9 and len(self.__board[0]) == 9 and (0 <= region <= 8):
                s = set()
                if region == 0:
                    for row in region_0:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 1:
                    for row in region_1:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 2:
                    for row in region_2:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 3:
                    for row in region_3:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 4:
                    for row in region_4:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 5:
                    for row in region_5:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 6:
                    for row in region_6:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 7:
                    for row in region_7:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
                elif region == 8:
                    for row in region_8:
                        s.add(int(row[0]))
                        s.add(int(row[1]))
                        s.add(int(row[2]))
                    if len(s) == 9:
                        return True
                    else:
                        return False
            else:
                raise ValueError
        else:
            raise TypeError

    def can_place_row(self, row, number):
        if isinstance(row, int) and isinstance(number, int):
            if len(self.__board) == 9 and (0 <= row <= 8) and (1 <= number <= 9):
                for i in range(9):
                    if self.__board[row][i] == number:
                        return False
                return True
            else:
                raise ValueError
        else:
            raise TypeError
    
    def can_place_column(self, column, number):
        if isinstance(column, int) and isinstance(number, int):
            if len(self.__board) == 9 and (0 <= column <= 8) and (1 <= number <= 9):
                for i in range(9):
                    if self.__board[i][column] == number:
                        return False
                return True
            else:
                raise ValueError
        else:
            raise TypeError

    def can_place_region(self, region, number):
        region_0 = ([row[0:3] for row in self.__board[0:3]])
        region_1 = ([row[3:6] for row in self.__board[0:3]])
        region_2 = ([row[6:9] for row in self.__board[0:3]])
        region_3 = ([row[0:3] for row in self.__board[3:6]])
        region_4 = ([row[3:6] for row in self.__board[3:6]])
        region_5 = ([row[6:9] for row in self.__board[3:6]])
        region_6 = ([row[0:3] for row in self.__board[6:9]])
        region_7 = ([row[3:6] for row in self.__board[6:9]])
        region_8 = ([row[6:9] for row in self.__board[6:9]])
        if isinstance(region, int) and isinstance(number, int):
            if len(self.__board) == 9 and (0 <= region <= 8) and (1 <= number <= 9):
                if region == 0:
                    for i in region_0:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 1:
                    for i in region_1:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 2:
                    for i in region_2:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 3:
                    for i in region_3:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 4:
                    for i in region_4:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 5:
                    for i in region_5:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 6:
                    for i in region_6:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 7:
                    for i in region_7:
                        for j in i:
                            if j == number:
                                return False
                    return True
                if region == 8:
                    for i in region_8:
                        for j in i:
                            if j == number:
                                return False
                    return True
            else:
                raise ValueError
        else:
            raise TypeError
    
    def smart_solve(self):
        if len(self.__board) == 9 and len(self.__board[0]) == 9 and len(self.__locked) == 9 and len(self.__locked[0]) == 9:
            i = 0
            for a in range(9):
                j = 0
                for b in range(9):
                    if not self.__locked[i][j]:
                        self.__board[i][j] = 0
                    j = j + 1
                i = i + 1
            self.__steps = self.__steps + 1
            for i in range(9):
                for j in range(9):
                    if not self.__locked[i][j]:
                        for z in range(1, 10, 1):
                            region = int((i / 3)) * 3 + int((j / 3))
                            if self.can_place_row(i, z) and self.can_place_column(j, z) and self.can_place_region(region, z):
                                self.__board[i][j] = z
                                self.__locked[i][j] = True
                                if self.smart_solve():
                                    self.__locked[i][j] = False
                                    return True
                                else:
                                    self.__locked[i][j] = False
                                    self.__board[i][j] = 0
                        return False
            return self.check_puzzle()



        else:
            raise ValueError

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


class NineView:
    def __init__(self):
        pass
    
    def show_board(self, board, locked):
        for i in range(9):
            line = ""
            for j in range(9):
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

from NineView import NineView
from SudokuNineModel import SudokuNineModel
import sys


class NineController:
    def __init__(self):
        self.__view = NineView()
        self.__model = SudokuNineModel()

    def main(args):
        self.run(self, args)

    def run(self, args):
        self.__model.load_from_file(str(args[1]))
        board = self.__model.board
        locked = self.__model.locked
        self.__view.show_board(board, locked)
        self.__model.smart_solve()
        self.__view.show_board(board, locked)
        steps = self.__model.steps
        self.__view.show_steps(steps)


if __name__ == "__main__":
    NineController().main(sys.argv[1])

