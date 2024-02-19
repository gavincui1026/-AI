import pygame
from move import Move
class Evaluate:
    def __init__(self, board):
        self.board = board
        self.move = Move(board)

    def is_solution(self):
        return all(self.board.board[x][y].color == '黑' for x in range(3) for y in range(3))

    def backtrack(self, depth=0):
        if self.is_solution():
            return True
        if depth > 9:
            return False

        for x in range(3):
            for y in range(3):
                self.move.click(x, y)
                self.board.display()
                pygame.display.flip()
                pygame.time.delay(500)
                if self.backtrack(depth + 1):
                    return True
                self.move.click(x, y)

        return False


