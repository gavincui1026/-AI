import pygame
from board import Board

class Move:
    def __init__(self, board):
        self.board = board

    def get_move(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    row = y // self.board.cell_size
                    col = x // self.board.cell_size
                    self.board.flip(row, col)
                    self.board.display()
                    if self.board.is_win():
                        print("游戏胜利！")
                        running = False

    def click(self, pixel_x, pixel_y):
        x = pixel_x // self.board.cell_size
        y = pixel_y // self.board.cell_size
        self.board.flip(x, y)