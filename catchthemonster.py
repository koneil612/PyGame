import pygame
import time
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
collide = False
level = 1
# goblins = []

class Monster(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.move_x = 5
        self.move_y = 0
        self.time = time.time()
        self.img = pygame.image.load('monster.png').convert_alpha()

    def move (self, width, height):
        self.x += self.move_x
        self.y += self.move_y
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
        if time.time() - self.time > 2:
            self.move_y = random.randint(-5, 5)
            self.move_x = random.randint(-5, 5)
            self.time = time.time()
    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))


class Goblin(object):
    def __init__(self):
        self.x = 290
        self.y = 300
        self.move_x = 5
        self.move_y = 0
        self.time = time.time()
        self.img = pygame.image.load('goblin.png').convert_alpha()

    def move (self, width, height):
        self.x += self.move_x
        self.y += self.move_y
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
        if time.time() - self.time > 2:
            self.move_y = random.randint(-1, 2)
            self.move_x = random.randint(-1, 2)
            self.time = time.time()
    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

class Hero(object):
    def __init__(self):
        self.img =  pygame.image.load('hero.png').convert_alpha()
        self.x = 256
        self.y = 240
        self.move_x = 0
        self.move_y = 0
    def move(self, width, height):
        self.x += self.move_x
        self.y += self.move_y
        if self.x > 460:
            self.move_x = -5
        if self.x < 40:
            self.move_x = 5
        if self.y == 440:
            self.move_y = -5
        if self.y < 40:
            self.move_y = 5
    def render(self, screen):
        screen.blit(self.img, (self.x, self.y))

def collision(x1, x2, y1, y2):
    return (x1 + 32 > x2) and (x2 + 32 > x1) and (y1 + 32 > y2) and (y2 + 32 > y1)

def main():
    # global goblins
    global level
    # declare the size of the canvas
    width = 512
    height = 480

    # initialize the pygame framework
    pygame.init()
    time.time()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Catch The Monster')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background = pygame.image.load('background.png').convert_alpha()
    monster = Monster()
    hero = Hero()
    goblin = Goblin()
    sound = pygame.mixer.Sound('music.wav')
    sound.play()
    soundPlayed = True

    # game loop
    stop_game = False
    game_win= False
    game_lost = False
    soundPlayed = False
    nextlevel = False


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
                    hero.move_y = 5
                elif event.key == KEY_UP:
                    hero.move_y  = -5
                elif event.key == KEY_LEFT:
                    hero.move_x  = -5
                elif event.key == KEY_RIGHT:
                    hero.move_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.move_y = 0
                elif event.key == KEY_UP:
                    hero.move_y = 0
                elif event.key == KEY_LEFT:
                    hero.move_x = 0
                elif event.key == KEY_RIGHT:
                    hero.move_x = 0
                elif event.key == pygame.K_RETURN:
                    game_win=False
                    game_lost = False
                    soundPlayed=False
                    monster.move
                    # monster.setInitialPosition(width, height,hero)
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.move(width, height)
        hero.move(width, height)
        goblin.move(width,height)



        # fill background color
        screen.blit(background, [0, 0])


        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        hero.render(screen)

        # game_over up top is set to false so it's saying if TRUE:::
        if not game_win:
            monster.render(screen)
            goblin.render(screen)
            nextlevel = False

        if collision(hero.x,monster.x, hero.y, monster.y):
            game_win = True

        if collision(goblin.x,hero.x, goblin.y, hero.y):
            game_lost = True

        if game_win == True:
            if nextlevel == False:
                level += 1
            sound = pygame.mixer.Sound('win.wav')
            sound.play()
            soundPlayed = True
            font = pygame.font.SysFont("Corbel", 20)
            text = font.render("Good job! Hit ENTER to go to the next level!", 0, (255,255,255))
            screen.blit(text, (100,250))
            pygame.display.set_caption('Level %r' % (level))
            nextlevel = True


        if game_lost == True:
            level = 1
            pygame.display.set_caption('Level %r' % (level))
            sound = pygame.mixer.Sound('lose.wav')
            sound.play()
            soundPlayed = True
            font = pygame.font.SysFont("Corbel", 20)
            text = font.render("You Loose :( Hit ENTER to play again", 0, (255,255,255))
            screen.blit(text, (100,250))



        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
