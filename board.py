from piece import Piece
import pygame
class Board:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.cell_size = 100
        self.board = [[Piece('白') for _ in range(cols)] for _ in range(rows)]
        pygame.init()
        self.window = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('黑白翻翻棋')

    def flip(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.board[x][y].toggle()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                self.board[nx][ny].toggle()

    def is_win(self):
        return all(self.board[x][y].color == '黑' for x in range(3) for y in range(3))

    # 动态渲染出一个3x3棋盘ui
    def display(self):
            self.window.fill((153,101,21))
            for x in range(self.rows):
                for y in range(self.cols):
                    piece = self.board[x][y]
                    center_x, center_y = x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2
                    if piece.color == '白':
                        pygame.draw.circle(self.window, (255, 255, 255), (center_x, center_y), self.cell_size // 2)
                        pygame.draw.circle(self.window, (0, 0, 0), (center_x, center_y), self.cell_size // 2,
                                           2)  # 2 is the line width
                    elif piece.color == '黑':
                        pygame.draw.circle(self.window, (0, 0, 0), (center_x, center_y), self.cell_size // 2)
            pygame.display.flip()
    pygame.quit()

