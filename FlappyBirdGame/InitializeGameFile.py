import pygame
import random

# Initialize Pygame
pygame.init()

# Setup Display
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Define Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Constants
FPS = 30
GRAVITY = 1
JUMP = -15
PIPE_WIDTH = 70
PIPE_GAP = 150

# Load Bird Image
bird_img = pygame.Surface((30, 30))
bird_img.fill((255, 255, 0))

class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.vel = 0
        self.rect = pygame.Rect(self.x, self.y, 30, 30)

    def update(self):
        self.vel += GRAVITY
        self.y += self.vel
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        self.vel = JUMP

    def draw(self):
        win.blit(bird_img, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= 5
        self.top.topleft = (self.x, 0)
        self.bottom.topleft = (self.x, self.height + PIPE_GAP)

    def draw(self):
        pygame.draw.rect(win, GREEN, self.top)
        pygame.draw.rect(win, GREEN, self.bottom)

class Game:
    def __init__(self):
        self.score = 0  # Initialize score

    def game_over(self):
        font_big = pygame.font.SysFont(None, 72)
        font_small = pygame.font.SysFont(None, 36)

        # Render the "Game Over" text & the score
        game_over_text = font_big.render("Game Over", True, BLACK)
        score_text = font_big.render(f"Score: {self.score}", True, BLACK)
        restart_text = font_small.render("Press any key to Exit", True, BLACK)

        win.fill(WHITE)
        win.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        win.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 100))
        pygame.display.update()

        self.wait_for_exit()

    def wait_for_exit(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def main(self):
        clock = pygame.time.Clock()
        bird = Bird()  # Ensure bird is initialized at the start of the game
        pipes = [Pipe()]
        self.score = 0  # Reset the score for a new game
        font = pygame.font.SysFont(None, 36)

        run = True
        while run:
            clock.tick(FPS)

            # Handle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    bird.jump()

            # Update bird and pipes
            bird.update()
            if pipes[-1].x < WIDTH // 2:
                pipes.append(Pipe())

            for pipe in pipes[:]:
                pipe.update()
                if pipe.x + PIPE_WIDTH < 0:
                    pipes.remove(pipe)
                    self.score += 1

            # Check collisions
            for pipe in pipes:
                if bird.rect.colliderect(pipe.top) or bird.rect.colliderect(pipe.bottom):
                    self.game_over()  # Call game_over method if a collision occurs
                    run = False

            # Draw Everything
            win.fill(WHITE)
            bird.draw()
            for pipe in pipes:
                pipe.draw()
            score_text = font.render(f"Score: {self.score}", True, BLACK)
            win.blit(score_text, (10, 10))

            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.main()    # Start the game using the main method
