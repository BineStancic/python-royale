import pygame
import random
pygame.init()

wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Python Royale");

#Sprite and sount imports
player_image = pygame.image.load('player.gif')
picture = pygame.transform.scale(player_image, (50, 50))

background = pygame.image.load('background1.png')
background2 = pygame.image.load('background2.png')
background3 = pygame.image.load('background8.png')


clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 5
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self, wn):
        #pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.x_char, self.y_char))
        wn.blit(picture, (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)

class NPC():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x, self.y, 40, 40)

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 0, 255), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)


class projectle():
    def __init__(self, x, y, radius, colour, vel):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.vel = 8

    def draw(self, wn):
        pygame.draw.circle(wn, self.colour, (self.x, self.y), self.radius)





def drawGame():
        wn.blit(background, (0,0))

        you.draw(wn)
        enemy.draw(wn)



        pygame.display.update()

#def game_menu():
    #Game menu: select character and background


you = player(50, 50, 40, 40)
enemy = NPC(100, 100, 40, 40)



run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and you.x > you.vel:
        you.x -= you.vel
    if keys[pygame.K_d] and you.x < wn_x - you.x_char:
        you.x += you.vel
    if keys[pygame.K_w] and you.y > you.vel:
        you.y -= you.vel
    if keys[pygame.K_s] and you.y < wn_y - you.y_char:
        you.y += you.vel


    drawGame()

pygame.quit()
