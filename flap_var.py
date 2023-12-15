import pygame
from os.path import join

pygame.font.init()

# --VISUAL--
# Colours 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Width and height of the screen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Size of images
GROUND_HEIGHT = HEIGHT // 10
PIPE_GAP, PIPE_WIDTH = HEIGHT // 5, WIDTH // 15
SPRITE_WIDTH, SPRITE_HEIGHT = WIDTH // 15, HEIGHT // 15

# Fonts
SCORE_FONT = pygame.font.SysFont('comicsans', 30)
GAME_OVER_FONT = pygame.font.SysFont('comicsans', 70)

# Images
SPRITE = pygame.transform.scale(pygame.image.load(join('Assets', 'flappy_sprite.png')),
                                (SPRITE_WIDTH, SPRITE_HEIGHT)).convert_alpha()
GROUND = pygame.transform.scale(pygame.image.load(join('Assets', 'ground.png')),
                                (2*WIDTH, GROUND_HEIGHT))
SKY = pygame.transform.scale(pygame.image.load(join('Assets', 'background-day.png')),
                              (WIDTH, HEIGHT))
PIPE_LOW = pygame.image.load(join('Assets', 'pipe.png'))
PIPE_LOW = pygame.transform.scale_by(PIPE_LOW, PIPE_WIDTH / PIPE_LOW.get_width())
PIPE_HIGH = pygame.transform.rotate(PIPE_LOW, 180)

# --MOVEMENT--
SCREEN_SHIFT = 3                    # Horizontal
MAX_DOWN_VEL, GRAVITY = 4, 2       # Downwards
UPWARDS = -18                        # Up on spacebar
SCORE_CHANGE = 1                    # Score change/frame
FPS = 60