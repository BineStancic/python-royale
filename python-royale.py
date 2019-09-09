import pygame
import random
pygame.init()

wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Python Royale");

#Sprite and sount imports
background = pygame.image.load('background1.png')



clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 5
        self.hitbox = (self.x, self.y + 10, 70, 50)

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.x_char, self.y_char))
        self.hitbox = (self.x, self.y + 10, 70, 50)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)

class NPC():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x, self.y, 70, 50)

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 0, 255), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, 70, 50)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)




def drawGame():
        wn.blit(background, (0,0))

        you.draw(wn)
        enemy.draw(wn)

        pygame.display.update()

you = player(50, 50, 40, 40)
enemy = NPC(100, 100, 40, 40)

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and you.x > you.vel:
        you.x -= you.vel
    if keys[pygame.K_RIGHT] and you.x < wn_x - you.x_char:
        you.x += you.vel
    if keys[pygame.K_UP] and you.y > you.vel:
        you.y -= you.vel
    if keys[pygame.K_DOWN] and you.y < wn_y - you.y_char:
        you.y += you.vel

    drawGame()

pygame.quit()
