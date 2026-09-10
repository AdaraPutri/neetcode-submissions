import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not self.checkRow(board, len(board[0])):
            return False
        if not self.checkCol(board, len(board[0])):
            return False
        subBoard = [[0]*3 for i in range(3)]
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                subBoard = [[board[i+x][j+y] for x in range(3) for y in range(3)]] 
                if not self.checkSub(subBoard, len(subBoard[0])):
                    return False
        return True

    # each row
    def checkRow(self, board: List[List[str]], value):
        print("at first")
        for i in range(9):
            countDots, expAmount, actAmount = 0, 0, 0
            if '.' in board[i]:
                for j in range(9):
                    if board[i][j] == '.':
                        countDots+=1
            expAmount = 9 - countDots
            actAmount = len(set(board[i])) - 1
            if expAmount != actAmount:
                return False
        return True

    # each column
    def checkCol(self, board: List[List[str]], value):
        print("at second")
        for i in range(9):
            currCol = []
            countDots, expAmount, actAmount = 0, 0, 0
            for j in range(9):
                currCol.append(board[j][i])
            if '.' in currCol:
                for k in range(9):
                    if currCol[k] == '.':
                        countDots+=1
            expAmount = 9 - countDots
            actAmount = len(set(currCol)) - 1
            if expAmount != actAmount:
                return False
        return True

    # each sub-box
    def checkSub(self, board: List[List[str]], value):
        print(board)
        vals = [cell for row in board for cell in row if cell != '.']
        return len(vals) == len(set(vals)) 