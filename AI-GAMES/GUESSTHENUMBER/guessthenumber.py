import pygame
import sys
import math

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Number Guessing Game - Minimax")

# Fonts and Colors
FONT = pygame.font.SysFont("arial", 32)
BIG_FONT = pygame.font.SysFont("arial", 48)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
BLUE = (100, 100, 255)

# Game Variables
low = 1
high = 100
attempts = 0
game_over = False

# Minimax Function
def minimax_guess(low, high):
    if low > high:
        return math.inf, None
    if low == high:
        return 1, low

    best_score = math.inf
    best_guess = None

    for guess in range(low, high + 1):
        left_score, _ = minimax_guess(low, guess - 1)
        right_score, _ = minimax_guess(guess + 1, high)
        worst_case = 1 + max(left_score, right_score)

        if worst_case < best_score:
            best_score = worst_case
            best_guess = guess

    return best_score, best_guess

# Button Setup
def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = FONT.render(text, True, BLACK)
    label_rect = label.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(label, label_rect)
    return pygame.Rect(x, y, w, h)

def draw_game(guess):
    screen.fill(WHITE)
    if not game_over:
        prompt = FONT.render("Is my guess too High, Low, or Correct?", True, BLACK)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 50))

        guess_text = BIG_FONT.render(f"My guess is: {guess}", True, BLUE)
        screen.blit(guess_text, (WIDTH // 2 - guess_text.get_width() // 2, 120))

        high_btn = draw_button("High", 100, 250, 100, 50, RED)
        low_btn = draw_button("Low", 250, 250, 100, 50, GREEN)
        correct_btn = draw_button("Correct", 400, 250, 100, 50, BLUE)
        return high_btn, low_btn, correct_btn
    else:
        result = FONT.render(f"Yay! I guessed it in {attempts} tries.", True, BLACK)
        screen.blit(result, (WIDTH // 2 - result.get_width() // 2, HEIGHT // 2 - 20))
        return None, None, None

# Initial Minimax Guess
_, guess = minimax_guess(low, high)

# Main Loop
running = True
while running:
    high_btn, low_btn, correct_btn = draw_game(guess)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            if high_btn and high_btn.collidepoint(event.pos):
                high = guess - 1
            elif low_btn and low_btn.collidepoint(event.pos):
                low = guess + 1
            elif correct_btn and correct_btn.collidepoint(event.pos):
                game_over = True

            if not game_over:
                _, guess = minimax_guess(low, high)
                attempts += 1

pygame.quit()
sys.exit()
