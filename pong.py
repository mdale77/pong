# 7/12/16
import pygame
import random

WIDTH = 480
HEIGHT = 360
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (0, 200, 0)
DARK_RED = (200, 0, 0)

font_name = pygame.font.match_font('arial')

def draw_score_or_win(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 0
        self.score = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy += -8
        if keystate[pygame.K_DOWN]:
            self.speedy += 8
        self.rect.y += self.speedy
        if keystate[pygame.K_r]:
            self.score = 0
            p2.score = 0
            b.__init__()


        if self.rect.top < HEIGHT - HEIGHT:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Player_Two(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((8, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 0
        self.score = 0
        self.move = True

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy += -8
        if keystate[pygame.K_s]:
            self.speedy += 8
        self.rect.y += self.speedy
        #STRONG AI BELOW
        #if self.move == False:
        #    self.speedy += random.randrange(-8, 8)
        #elif self.move == True:
        #    self.rect.y += b.speedy - random.randrange(-8, 8)

        if self.rect.top < HEIGHT - HEIGHT:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 12))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedy = -3
        self.speedx = 3
        self.size = 15
        self.colors = [RED, GREEN, BLUE]

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        #Walls check
        if self.rect.right > WIDTH + 5:
            self.__init__()
            p2.score += 1

        if self.rect.left < -4:
            self.__init__()
            self.speedx = -5
            p1.score += 1

        if self.rect.bottom > HEIGHT:
            self.speedy *= -1
            self.rect.y += self.speedy

        if self.rect.top < 0:
            self.speedy *= -1
            self.rect.y += self.speedy

        #Paddle check
        if self.rect.collidepoint(p1.rect.topleft) or self.rect.collidepoint((p1.rect.topleft[0], p1.rect.topleft[1] - 10)):
            print ("HIT")
            self.speedx *= -1.5
            self.image.fill(BLUE)
        elif self.rect.collidepoint(p1.rect.bottomleft):
            self.speedx *= -1.5
            self.image.fill(BLUE)
        elif self.rect.collidepoint(p1.rect.center):
            self.speedx *= -1
            self.image.fill(BLUE)
        elif pygame.sprite.collide_rect(p1, self):
            self.speedx *= -1
            self.image.fill(BLUE)
        #if self.rect.collidepoint(p1.rect.midleft):
        #    self.speedx *= -1
        #if pygame.sprite.collide_rect(p1, self):
        #if self.rect.collidepoint(p2.rect.midright):
        #    self.speedx *= -1

        if self.rect.collidepoint(p2.rect.topright):
            self.speedx *= -1.5
            self.image.fill(GREEN)
        elif self.rect.collidepoint(p2.rect.bottomright):
            self.speedx *= -1.5
            self.image.fill(GREEN)
        elif self.rect.collidepoint(p2.rect.center):
            self.speedx *= -1
            self.image.fill(GREEN)
        elif pygame.sprite.collide_rect(p2, self):
            self.speedx *= -1
            self.image.fill(GREEN)


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
#Player instances
p1 = Player(WIDTH - 30, HEIGHT / 2)
p2 = Player_Two(WIDTH - 450, HEIGHT / 2)
b = Ball()
#Sprites being added to sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(p2)
all_sprites.add(b)
# Game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    # print (p1.rect.topleft[1])
    # print (p1.rect.topleft[1] - 10)
    # # print (p1.rect.bottomleft)
    # # print (p1.rect.center)


    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_score_or_win(screen, str(p1.score), 20, WIDTH - 100, 10)
    draw_score_or_win(screen, str(p2.score), 20, WIDTH - 380, 10)

    if p1.score == 10:
        draw_score_or_win(screen, "Player 1 Wins!", 30, WIDTH / 2, 130)
        b.speedx = 0
        b.speedy = 0

    elif p2.score == 10:
        draw_score_or_win(screen, "Player 2 Wins!", 30, WIDTH / 2, 130)
        b.speedx = 0
        b.speedy = 0

    # AFTER DRAWING EVERYTHING, FLIP THE DISPLAY
    pygame.display.flip()

pygame.quit()
