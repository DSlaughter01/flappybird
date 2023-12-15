import pygame 
from random import randint
from os.path import join
from flap_var import * 
from flap_class import *

pygame.font.init()

def draw_screen(ground, player, pipes, ground_scroll, bg_scroll, score):

    for i in range(2): WIN.blit(SKY, (-i * bg_scroll, 0))
    for pipe in pipes: pipe.draw()
    ground.draw(ground_scroll)
    player.draw()

    score_text = SCORE_FONT.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))
    pygame.display.update()


def handle_movement(ground_scroll, player, pipes):

    player.move()
    
    for pipe in pipes: pipe.move()
    if pipes[0].rect.x < -PIPE_WIDTH: del(pipes[0])
    if pipes[-1].rect.x < WIDTH - 200: 
        low_height = randint(200, 400)
        pipes.append(LowPipe(WIDTH, low_height))
        pipes.append(HighPipe(WIDTH, low_height))

    return pipes


def game_over(player, objects):
    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            return True
    else: return False

def render_game_over(score):

    go_text = GAME_OVER_FONT.render("GAME OVER", True, BLACK)
    score_text = GAME_OVER_FONT.render(f"Score: {score}", True, BLACK)
    WIN.blit(go_text, ((WIDTH - go_text.get_width()) // 2, (HEIGHT - go_text.get_height()) // 2 - 50))
    WIN.blit(score_text, ((WIDTH - score_text.get_width()) // 2, (HEIGHT - score_text.get_height()) // 2 + 50))

    pygame.display.update()
    pygame.time.delay(3000)