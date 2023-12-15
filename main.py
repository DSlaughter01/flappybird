from flap_var import *
from flap_func import *
from flap_class import *

pygame.init()
pygame.font.init()
pygame.display.set_caption("Flappy bird")

def main():
                            
    clock = pygame.time.Clock()

    ground = Ground()
    player = Player()
    pipes = [LowPipe(WIDTH, 200), HighPipe(WIDTH, 200)]

    ground_scroll, bg_scroll, score = 0, 0, 0

    run = True
    
    while run:
            
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.y >= 0:
                    player.move_up()

        if game_over(player, [ground, *pipes]) == True:
            run = False
            render_game_over(score)

        ground_scroll += SCREEN_SHIFT
        bg_scroll += SCREEN_SHIFT / 4
        score += SCORE_CHANGE

        if ground_scroll >= WIDTH: ground_scroll -= WIDTH
        if bg_scroll >= WIDTH: bg_scroll -= WIDTH

        pipes = handle_movement(ground_scroll, player, pipes)
        draw_screen(ground, player, pipes, ground_scroll, bg_scroll, score)

if __name__ == "__main__":
    main()