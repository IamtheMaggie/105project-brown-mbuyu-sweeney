import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
enemy1hits = 0
playerhits = 0

pump1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-100x100.png')
pump1X = 0
pump1Y = 0

def pump1(x,y):
    screen.blit(pump1Img,(x, y))

enemy1healthbar1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-30x7.png')
enemy1healthbar1Img = pygame.transform.scale(enemy1healthbar1Img, (100, 10))

def enemy1healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

enemy1healthbar2Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-30x7.png')
enemy1healthbar2Img = pygame.transform.scale(enemy1healthbar2Img, (25, 10))

def enemy1healthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

def playerhealthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def playerhealthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

enemy1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-200x200.png')
enemy1Img = pygame.transform.scale(enemy1Img, (350, 350))
enemy1Img = pygame.transform.flip(enemy1Img, 100, 0)
enemy1X = 750
enemy1Y = 200

def enemy1(x,y):
    screen.blit(player1Img, (x + 200, y +250))
    screen.blit(enemy1Img, (x, y))

spit1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-64x64.png')
spit1X = 0
spit1Y = 0
spit1_state = "ready"

def spit1(x,y):
    screen.blit(spit1Img, (spit1X, spit1Y))

def fire_spit1(x,y):
    global spit1_state
    spit1_state = "fire"
    screen.blit(spit1Img, (x, y + 5))

playerImg = pygame.image.load(r'C:\Users\Mmwwa\Downloads\Girl 0.png')
playerImg = pygame.transform.scale(playerImg, (100, 100))
player1Img = playerImg
playerX = 150
playerY = 150
playerY_change = 0
playerX_change = 0

def player(x,y):
    screen.blit(player1Img, (x, y))

bulletImg = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-20x20.png')
bulletX = playerX
bulletY = playerY
bullet_state = "ready"

def bullet(x,y):
    screen.blit(playerImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))



running = True
while running:
    #RBG
    screen.fill((250, 250, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if playerX <= -22:
            playerX = -22
        if playerX >= 922:
            playerX = 935
        if playerY <= -10:
            playerY = -10
        if playerY >= 600:
            playerY = 600
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1Img = pygame.transform.flip(playerImg, 100, 0)
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                player1Img = playerImg
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP:
                playerY_change = 0
            if event.key == pygame.K_DOWN:
                playerY_change = 0
        if event.type == pygame.MOUSEBUTTONDOWN and bullet_state is "ready":
            slopeX, slopeY = pygame.mouse.get_pos()
            fire_bullet(playerX, bulletY)

    playerY += playerY_change
    playerX += playerX_change

    if enemy1hits < 2:
        if spit1_state is "ready":
            spit1X = enemy1X
            spit1Y = enemy1Y
            angle = math.atan2((playerY - enemy1Y), (playerX - enemy1X))
            spit1.angle = math.degrees(angle)
            SPEED = .3
            spit1_state = "fire"
        if spit1_state is "fire":
          #  fire_spit1(spit1X, spit1Y)
            spit1Y += math.sin(angle) * SPEED
            spit1X += math.cos(angle) * SPEED
            if spit1X > 1000 or spit1X < 0 or spit1Y > 800 or spit1Y < 0:
                spit1_state = "ready"
            if playerX - 15 < spit1X < playerX + 40 and playerY - 30 < spit1Y < playerY + 75:
                playerhits += 1
                spit1_state = "ready"
            if pump1X - 35 < spit1X < pump1X + 65 and pump1Y - 10 < spit1Y < pump1Y + 55:
                spit1_state = "ready"
    if enemy1hits == 0:
        enemy1healthbar1(enemy1X + 100, enemy1Y + 300)
        enemy1(enemy1X, enemy1Y)
    if enemy1hits == 1:
        enemy1healthbar2(enemy1X + 23, enemy1Y + 100)
        enemy1(enemy1X, enemy1Y)

    if bullet_state is "ready":
        bulletX = playerX
        bulletY = playerY
        SPEEDbullet = .3
        n = 0
    if bullet_state is "fire" and n == 0:
        anglebullet = math.atan2((slopeY - playerY), (slopeX - playerX))
        n = 1
        bullet.angle = math.degrees(n)
    if bullet_state is "fire" and n == 1:
        fire_bullet(bulletX, bulletY)
        bulletY += math.sin(anglebullet) * SPEEDbullet
        bulletX += math.cos(anglebullet) * SPEEDbullet
    if bulletX > 1000 or bulletX < 0 or bulletY > 700 or bulletY < 0:
        bullet_state = "ready"
    if enemy1X - 5 < bulletX < enemy1X + 85 and enemy1Y + 16 < bulletY < enemy1Y + 71:
        enemy1hits = enemy1hits + 1
        bullet_state = "ready"
    if pump1X - 13 < bulletX < pump1X + 84 and pump1Y + 20 < bulletY < pump1Y + 75:
        bullet_state = "ready"

    if enemy1X - 45 < playerX < enemy1X - 40 and enemy1Y - 18 < playerY < enemy1Y + 250:
        playerX = enemy1X - 45
    if enemy1X < playerX < enemy1X + 2 and enemy1Y - 18 < playerY < enemy1Y + 250:
        playerX = enemy1X + 65
    if enemy1Y - 18 < playerY < enemy1Y - 13 and enemy1X - 45 < playerX < enemy1X + 800:
        playerY = enemy1Y - 18
    if enemy1Y + 245 < playerY < enemy1Y + 250 and enemy1X - 45 < playerX < enemy1X + 800:
        playerY = enemy1Y + 250

    if pump1X - 60 < playerX < pump1X - 55 and pump1Y - 65 < playerY < pump1Y + 65:
        playerX = pump1X - 60
    if pump1X + 55 < playerX < pump1X + 60 and pump1Y - 65 < playerY < pump1Y + 65:
        playerX = pump1X + 60
    if pump1Y - 65 < playerY < pump1Y - 60 and pump1X - 60 < playerX < pump1X + 60:
        playerY = pump1Y - 65
    if pump1Y + 60 < playerY < pump1Y + 65 and pump1X - 60 < playerX < pump1X + 60:
        playerY = pump1Y + 65

    player(playerX, playerY)
    pump1(pump1X, pump1Y)
    pygame.display.update()