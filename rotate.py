import pygame
import random
pygame.init()

wn_x, wn_y = (500, 500)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Python Royale");

#Sprite and sount imports
player_image = pygame.image.load('player.gif')
picture = pygame.transform.scale(player_image, (50, 50))
rect = picture.get_rect()

background = pygame.image.load('background1.png')
background2 = pygame.image.load('background2.png')
background3 = pygame.image.load('background8.png')


clock = pygame.time.Clock()

def event_handler():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key ==K_ESCAPE):
            pygame.quit()
            sys.exit()

def rotate_and_center(wn, x, y, image, degrees):
    rotated = pygame.transform.rotate(image, degrees)
    rect = rotated.get_rect()


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
        you.rot_speed -= you.vel
    if keys[pygame.K_d] and you.x < wn_x - you.x_char:
        you.rot_speed += you.vel
    if keys[pygame.K_w] and you.y > you.vel:
        you.y -= you.vel
    if keys[pygame.K_s] and you.y < wn_y - you.y_char:
        you.y += you.vel


    drawGame()

pygame.quit()
