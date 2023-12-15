from flap_var import *
import pygame 

class Ground(pygame.sprite.Sprite):

    def __init__(self):
        self.rect = pygame.Rect(0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT)
        self.img = GROUND
        self.mask = pygame.mask.from_surface(self.img)
    
    def draw(self, ground_scroll):
        for i in range(2): WIN.blit(self.img, (-i * ground_scroll, self.rect.y))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.x = (WIDTH - SPRITE_WIDTH) // 2
        self.y = (HEIGHT - SPRITE_HEIGHT) // 2
        self.width = SPRITE_WIDTH
        self.height = SPRITE_HEIGHT
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.img = SPRITE
        self.mask = pygame.mask.from_surface(self.img)
        self.dy = 0
    
    def move(self):
        self.img = pygame.transform.rotate(SPRITE, -self.dy)
        if self.dy <= MAX_DOWN_VEL: self.dy += GRAVITY
        self.rect.y += self.dy
        self.mask = pygame.mask.from_surface(self.img)

    def move_up(self):
        self.dy = UPWARDS

    def draw(self):
        WIN.blit(self.img, (self.rect.x, self.rect.y))


class LowPipe(pygame.sprite.Sprite):

    def __init__(self, x, height):
        self.rect = pygame.Rect(x, HEIGHT - height, PIPE_WIDTH, height)
        self.img = PIPE_LOW
        self.mask = pygame.mask.from_surface(self.img)

    def move(self):
        self.rect.x -= SCREEN_SHIFT
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self):
        WIN.blit(self.img, (self.rect.x, self.rect.y))


class HighPipe(LowPipe):

    def __init__(self, x, low_height):
        super().__init__(x, low_height)
        self.img = PIPE_HIGH
        self.rect = pygame.Rect(x, HEIGHT - low_height - PIPE_GAP - self.img.get_height(), PIPE_WIDTH, self.img.get_height())
        self.mask = pygame.mask.from_surface(self.img)
