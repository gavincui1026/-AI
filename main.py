import pygame
from board import Board
from move import Move
from evaluate import Evaluate
def main():
    pygame.init()
    board = Board(3, 3)
    move = Move(board)
    evaluator = Evaluate(board)
    if evaluator.backtrack():
        print("Solution found!")
    else:
        print("No solution found.")
    TIMER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENT, 1000)  # Set a timer event every 5 seconds

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x //= board.cell_size  # Convert pixel coordinates to board coordinates
                y //= board.cell_size
                move.click(x, y)
            elif event.type == TIMER_EVENT:  # Check for the timer event
                # AI turn
                if not board.is_win():
                    best_move = evaluator.find_best_move(board, 3)  # Assuming a depth of 3 for the minimax algorithm
                    if best_move:
                        board.flip(*best_move)

        board.display()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()


