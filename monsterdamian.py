import pygame
from character import *

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background = pygame.image.load('background.png').convert_alpha()
    monster= Monster()
    monster.setInitialPosition(width, height, hero)


    # game loop
    stop_game = False
    game_over = False
    soundPlayd = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.changeDirection(0,hero.maxspeed)
                elif event.key == KEY_UP:
                    hero.changeDirection(0,-hero.maxspeed)
                elif event.key == KEY_LEFT:
                    hero.changeDirection(hero.maxspeed, 0)
                elif event.key == KEY_RIGHT:
                    hero.changeDirection(-hero.maxspeed, 0)




            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.update(width, height)
        hero.update(width, height, 32)
        # fill background color
        screen.blit(background)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        hero.render(screen)
        if not game_over:
            monster.render(screen)
        else:
            # play sound
            if not soundPlayd:
                sound = pygame.mixer.Sound('win.wav')
                sound.play()

        if character.checkCollision(hero,monster):
            game_over = True

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
