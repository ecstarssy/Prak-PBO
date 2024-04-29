import pygame
import sys

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CROSS_WIDTH = 15
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
FPS = 60

class TicTacToe:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe')
        self.screen.fill(BG_COLOR)
        self.board = [[' ' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
        self.current_player = 'X'
        self.game_over = False

    def draw_board(self):
        for row in range(1, BOARD_ROWS):
            pygame.draw.line(self.screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        for col in range(1, BOARD_COLS):
            pygame.draw.line(self.screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 'X':
                    pygame.draw.line(self.screen, RED, (col * SQUARE_SIZE + CROSS_WIDTH, row * SQUARE_SIZE + CROSS_WIDTH),
                                     ((col + 1) * SQUARE_SIZE - CROSS_WIDTH, (row + 1) * SQUARE_SIZE - CROSS_WIDTH), CROSS_WIDTH)
                    pygame.draw.line(self.screen, RED, ((col + 1) * SQUARE_SIZE - CROSS_WIDTH, row * SQUARE_SIZE + CROSS_WIDTH),
                                    (col * SQUARE_SIZE + CROSS_WIDTH, (row + 1) * SQUARE_SIZE - CROSS_WIDTH), CROSS_WIDTH)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(self.screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, LINE_WIDTH)

    def mark_square(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.current_player == 'X':
                self.current_player = 'O'
            else:
                self.current_player = 'X'

    def check_win(self):
        # Check rows
        for row in range(BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return True

        # Check columns
        for col in range(BOARD_COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def check_draw(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == ' ':
                    return False
        return True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                self.mark_square(clicked_row, clicked_col)
                if self.check_win():
                    self.game_over = True
                elif self.check_draw():
                    self.game_over = True

    def run_game(self):
        while True:
            self.handle_events()
            self.screen.fill(BG_COLOR)
            self.draw_board()
            self.draw_figures()
            pygame.display.update()
            pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    game = TicTacToe()
    game.run_game()