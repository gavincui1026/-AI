import pygame

class Piece:
    def __init__(self, color):
        self.color = color  # Initial color is white

    def toggle(self):
        self.color = '黑' if self.color == '白' else '白'

    def draw(self, window, x, y, radius):
        color = (0, 0, 0) if self.color == '黑' else (255, 255, 255)
        pygame.draw.circle(window, color, (x, y), radius)
        if self.color == '白':
            pygame.draw.circle(window, (0, 0, 0), (x, y), radius, 3)  # Draw border for white pieces

    def __str__(self):
        return self.color
