import pygame
import random
pygame.init()

wn_x, wn_y = (800, 800)
wn = pygame.display.set_mode((wn_x, wn_y))
pygame.display.set_caption("Python Royale");

#Sprite and sount imports
player_image = pygame.image.load('player.gif')
picture = pygame.transform.scale(player_image, (50, 50))

background1 = pygame.image.load('background1.png')
background = pygame.transform.scale(background1, (800, 800))

background2 = pygame.image.load('background2.png')
background3 = pygame.image.load('background8.png')


clock = pygame.time.Clock()

class player():
    def __init__(self, x, y, x_char, y_char):
        self.x = x
        self.y = y
        self.x_char = x_char
        self.y_char = y_char
        self.vel = 8
        self.hitbox = (self.x, self.y, 40, 40)


        #rotation speed

    def movement(self):
        self.rot_speed = 0
        if keys[pygame.K_a] and self.x > self.vel:
            self.x -= self.vel
        if keys[pygame.K_d] and self.x < wn_x - self.x_char:
            self.x += self.vel
        if keys[pygame.K_w] and self.y > self.vel:
            self.y -= self.vel
        if keys[pygame.K_s] and self.y < wn_y - self.y_char:
            self.y += self.vel

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 255, 0), (self.x, self.y, self.x_char, self.y_char))
        #wn.blit(picture, (self.x, self.y))
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)

class NPC():
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.hitbox = (self.x, self.y, 40, 40)

    def movement(self):
        if keys[pygame.K_j] and self.x > self.vel:
            self.x -= self.vel
        if keys[pygame.K_l] and self.x < wn_x - self.width:
            self.x += self.vel
        if keys[pygame.K_i] and self.y > self.vel:
            self.y -= self.vel
        if keys[pygame.K_k] and self.y < wn_y - self.height:
            self.y += self.vel

    def draw(self, wn):
        pygame.draw.rect(wn, (0, 0, 255), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)


class ball():
    def __init__(self, x, y, radius, colour, xspeed, yspeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.hitbox = (self.x, self.y, 40, 40)
        self.xspeed = xspeed
        self.yspeed = yspeed
        #self.vel = 8

    #first 5 iterations loop through full speed after 5 start adding friction
    def movement(self):
        if self.x > 0 and self.x + self.radius < wn_x:
            for i in range(3):
                self.x = self.x + self.xspeed
            self.xspeed = self.xspeed *0.981

        #ball bouncing at edges
        else:
            print("TURNNN")
            self.xspeed = -10

        if self. y > 0 and self.y +self.radius < wn_y:
            for i in range(3):
                self.y = self.y + self.yspeed
            self.yspeed = self.yspeed *0.981

        #ball bouncing at edges
        else:
            print("TURNNN")
            self.yspeed = -10


    def draw(self, wn):
        self.movement()
        pygame.draw.circle(wn, self.colour, (int(self.x), int(self.y)), self.radius)
        self.hitbox = (self.x, self.y, 40, 40)
        pygame.draw.rect(wn, (255,0,0), self.hitbox, 2)





def drawGame():
        wn.blit(background, (0,0))
        player1.draw(wn)
        player2.draw(wn)
        ball_1.draw(wn)
        pygame.display.update()

#def game_menu():
    #Game menu: select character and background


player1 = player(50, 50, 40, 40)
player2 = NPC(100, 100, 40, 40)
ball_1 = ball(200, 200, 10, (255,0,0), 0, 0)



run = True
#increase interaction to prevent ball going through player too fast
interaction = 10
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    keys = pygame.key.get_pressed()
    player1.movement()
    player2.movement()

    #print(player1.hitbox)
    if player1.hitbox[0] + player1.hitbox[2] < ball_1.hitbox[0] and player1.hitbox[0] + player1.hitbox[2] > ball_1.hitbox[0] -interaction:
        if player1.hitbox[1] + player1.hitbox[3] > ball_1.hitbox[1] and player1.hitbox[1] < ball_1.hitbox[1] + ball_1.hitbox[3]:
            ball_1.xspeed += 2
            print("kick-right")

    if player1.hitbox[0] > ball_1.hitbox[0] + ball_1.hitbox[2] and ball_1.hitbox[0] + ball_1.hitbox[2] > player1.hitbox[0] - interaction:
        if player1.hitbox[1] + player1.hitbox[3] > ball_1.hitbox[1] and player1.hitbox[1] < ball_1.hitbox[1] + ball_1.hitbox[3]:
            ball_1.xspeed -= 2
            print("kick-left")

    if player1.hitbox[1] + player1.hitbox[3] < ball_1.hitbox[1] and player1.hitbox[1] + player1.hitbox[3] > ball_1.hitbox[1] -interaction:
        if player1.hitbox[0] + player1.hitbox[2] > ball_1.hitbox[0] and player1.hitbox[0] < ball_1.hitbox[0] + ball_1.hitbox[2]:
            ball_1.yspeed += 2
            print("kick-down")

    if player1.hitbox[1] > ball_1.hitbox[1] + ball_1.hitbox[3] and ball_1.hitbox[1] + ball_1.hitbox[3] > player1.hitbox[1] - interaction:
        if player1.hitbox[0] + player1.hitbox[2] > ball_1.hitbox[0] and player1.hitbox[0] < ball_1.hitbox[0] + ball_1.hitbox[2]:
            ball_1.yspeed -= 2
            print("kick-up")



    #print(player2.hitbox)
    if player2.hitbox[0] + player2.hitbox[2] < ball_1.hitbox[0] and player2.hitbox[0] + player2.hitbox[2] > ball_1.hitbox[0] -interaction:
        if player2.hitbox[1] + player2.hitbox[3] > ball_1.hitbox[1] and player2.hitbox[1] < ball_1.hitbox[1] + ball_1.hitbox[3]:
            ball_1.xspeed += 2
            print("kick-right")

    if player2.hitbox[0] > ball_1.hitbox[0] + ball_1.hitbox[2] and ball_1.hitbox[0] + ball_1.hitbox[2] > player2.hitbox[0] - interaction:
        if player2.hitbox[1] + player2.hitbox[3] > ball_1.hitbox[1] and player2.hitbox[1] < ball_1.hitbox[1] + ball_1.hitbox[3]:
            ball_1.xspeed -= 2
            print("kick-left")

    if player2.hitbox[1] + player2.hitbox[3] < ball_1.hitbox[1] and player2.hitbox[1] + player2.hitbox[3] > ball_1.hitbox[1] -interaction:
        if player2.hitbox[0] + player2.hitbox[2] > ball_1.hitbox[0] and player2.hitbox[0] < ball_1.hitbox[0] + ball_1.hitbox[2]:
            ball_1.yspeed += 2
            print("kick-down")

    if player2.hitbox[1] > ball_1.hitbox[1] + ball_1.hitbox[3] and ball_1.hitbox[1] + ball_1.hitbox[3] > player2.hitbox[1] - interaction:
        if player2.hitbox[0] + player2.hitbox[2] > ball_1.hitbox[0] and player2.hitbox[0] < ball_1.hitbox[0] + ball_1.hitbox[2]:
            ball_1.yspeed -= 2
            print("kick-up")




    drawGame()

pygame.quit()
