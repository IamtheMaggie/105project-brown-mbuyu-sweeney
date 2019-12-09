import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
enemy1hits = 0
enemy2hits = 0
playerhits = 0

mushroom1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-100x100(2).png')
mushroom1X = 190
mushroom1Y = 48

mushroom2X = 921
mushroom2Y = 553

mushroom3X = 232
mushroom3Y = 583

mushroom4X = 108
mushroom4Y = 185

mushroom5X = 328
mushroom5Y = 101

mushroom6X = 216
mushroom6Y = 350

mushroom7X = 175
mushroom7Y = 525

mushroom8X = 296
mushroom8Y = 689

mushroom9X = 412
mushroom9Y = 373

mushroom10X = 641
mushroom10Y = 247

mushroom11X = 804
mushroom11Y = 46

mushroom12X = 866
mushroom12Y = 242


def mushroom1(x,y):
    screen.blit(mushroom1Img,(x, y))

enemy1healthbar1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-30x7.png')
enemy1healthbar1Img = pygame.transform.scale(enemy1healthbar1Img, (50, 10))

def enemy1healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

enemy1healthbar2Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-30x7.png')
enemy1healthbar2Img = pygame.transform.scale(enemy1healthbar2Img, (25, 10))

def enemy1healthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

def enemy2healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def enemy2healthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

def playerhealthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def playerhealthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

enemy1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-200x200.png')
enemy1Img = pygame.transform.scale(enemy1Img, (100, 100))
enemy1X = 500
enemy1Y = 500

def enemy1(x,y):
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

enemy2X = 170
enemy2Y = 500

def enemy2(x,y):
    screen.blit(enemy1Img, (x, y))

spit2X = 0
spit2Y = 0
spit2_state = "ready"

def spit2(x,y):
    screen.blit(spit1Img, (spit2X, spit2Y))

def fire_spit2(x,y):
    global spit2_state
    spit2_state = "fire"
    screen.blit(spit1Img, (x, y + 5))

playerImg = pygame.image.load(r'C:\Users\Mmwwa\Downloads\Girl 0.png')
playerImg = pygame.transform.scale(playerImg, (100, 100))
playerX = 150
playerY = 150
playerY_change = 0
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

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
    screen.fill((250, 0, 0))
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
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
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
        angle3 = math.atan2((playerY - enemy1Y), (playerX - enemy1X))
        enemy1.angle3 = math.degrees(angle3)
        enemy1Y += math.sin(angle3) * .05
        enemy1X += math.cos(angle3) * .05
        if spit1_state is "ready":
            spit1X = enemy1X
            spit1Y = enemy1Y
            angle = math.atan2((playerY - enemy1Y), (playerX - enemy1X))
            spit1.angle = math.degrees(angle)
            SPEED = .3
            spit1_state = "fire"
        if spit1_state is "fire":
            fire_spit1(spit1X, spit1Y)
            spit1Y += math.sin(angle) * SPEED
            spit1X += math.cos(angle) * SPEED
            if spit1X > 1000 or spit1X < 0 or spit1Y > 800 or spit1Y < 0:
                spit1_state = "ready"
            if playerX - 15 < spit1X < playerX + 40 and playerY - 30 < spit1Y < playerY + 75:
                playerhits += 1
                spit1_state = "ready"
            if mushroom1X - 27 < spit1X < mushroom1X + 63 and mushroom1Y -20 < spit1Y < mushroom1Y + 67:
                spit1_state = "ready"
            if mushroom2X - 27 < spit1X < mushroom2X + 63 and mushroom2Y - 20 < spit1Y < mushroom2Y + 67:
                spit1_state = "ready"
            if mushroom3X - 27 < spit1X < mushroom3X + 63 and mushroom3Y - 20 < spit1Y < mushroom3Y + 67:
                spit1_state = "ready"
            if mushroom4X - 27 < spit1X < mushroom4X + 63 and mushroom4Y - 20 < spit1Y < mushroom4Y + 67:
                spit1_state = "ready"
            if mushroom5X - 27 < spit1X < mushroom5X + 63 and mushroom5Y - 20 < spit1Y < mushroom5Y + 67:
                spit1_state = "ready"
            if mushroom6X - 27 < spit1X < mushroom6X + 63 and mushroom6Y - 20 < spit1Y < mushroom6Y + 67:
                spit1_state = "ready"
            if mushroom7X - 27 < spit1X < mushroom7X + 63 and mushroom7Y - 20 < spit1Y < mushroom7Y + 67:
                spit1_state = "ready"
            if mushroom8X - 27 < spit1X < mushroom8X + 63 and mushroom8Y - 20 < spit1Y < mushroom8Y + 67:
                spit1_state = "ready"
            if mushroom9X - 27 < spit1X < mushroom9X + 63 and mushroom9Y - 20 < spit1Y < mushroom9Y + 67:
                spit1_state = "ready"
            if mushroom10X - 27 < spit1X < mushroom10X + 63 and mushroom10Y - 20 < spit1Y < mushroom10Y + 67:
                spit1_state = "ready"
            if mushroom11X - 27 < spit1X < mushroom11X + 63 and mushroom11Y - 20 < spit1Y < mushroom11Y + 67:
                spit1_state = "ready"
            if mushroom12X - 27 < spit1X < mushroom12X + 63 and mushroom12Y - 20 < spit1Y < mushroom12Y + 67:
                spit1_state = "ready"
    if enemy1hits == 0:
        enemy1healthbar1(enemy1X + 23, enemy1Y + 100)
        enemy1(enemy1X, enemy1Y)
    if enemy1hits == 1:
        enemy1healthbar2(enemy1X + 23, enemy1Y + 100)
        enemy1(enemy1X, enemy1Y)

    if enemy2hits < 2:
        angle4 = math.atan2((playerY - enemy2Y), (playerX - enemy2X))
        enemy2.angle4 = math.degrees(angle4)
        enemy2Y += math.sin(angle4) * .03
        enemy2X += math.cos(angle4) * .03
        if spit2_state is "ready":
            spit2X = enemy2X
            spit2Y = enemy2Y
            angle2 = math.atan2((playerY - enemy2Y), (playerX - enemy2X))
            spit2.angle2 = math.degrees(angle2)
            SPEED = .3
            spit2_state = "fire"
        if spit2_state is "fire":
            fire_spit2(spit2X, spit2Y)
            spit2Y += math.sin(angle2) * SPEED
            spit2X += math.cos(angle2) * SPEED
            if spit2X > 1000 or spit2X < 0 or spit2Y > 800 or spit2Y < 0:
                spit2_state = "ready"
            if playerX - 15 < spit2X < playerX + 40 and playerY - 30 < spit2Y < playerY + 75:
                playerhits += 1
                spit2_state = "ready"
            if mushroom1X - 27 < spit2X < mushroom1X + 63 and mushroom1Y -20 < spit2Y < mushroom1Y + 67:
                spit2_state = "ready"
            if mushroom2X - 27 < spit2X < mushroom2X + 63 and mushroom2Y - 20 < spit2Y < mushroom2Y + 67:
                spit2_state = "ready"
            if mushroom3X - 27 < spit2X < mushroom3X + 63 and mushroom3Y - 20 < spit2Y < mushroom3Y + 67:
                spit2_state = "ready"
            if mushroom4X - 27 < spit2X < mushroom4X + 63 and mushroom4Y - 20 < spit2Y < mushroom4Y + 67:
                spit2_state = "ready"
            if mushroom5X - 27 < spit2X < mushroom5X + 63 and mushroom5Y - 20 < spit2Y < mushroom5Y + 67:
                spit2_state = "ready"
            if mushroom6X - 27 < spit2X < mushroom6X + 63 and mushroom6Y - 20 < spit2Y < mushroom6Y + 67:
                spit2_state = "ready"
            if mushroom7X - 27 < spit2X < mushroom7X + 63 and mushroom7Y - 20 < spit2Y < mushroom7Y + 67:
                spit2_state = "ready"
            if mushroom8X - 27 < spit2X < mushroom8X + 63 and mushroom8Y - 20 < spit2Y < mushroom8Y + 67:
                spit2_state = "ready"
            if mushroom9X - 27 < spit2X < mushroom9X + 63 and mushroom9Y - 20 < spit2Y < mushroom9Y + 67:
                spit2_state = "ready"
            if mushroom10X - 27 < spit2X < mushroom10X + 63 and mushroom10Y - 20 < spit2Y < mushroom10Y + 67:
                spit2_state = "ready"
            if mushroom11X - 27 < spit2X < mushroom11X + 63 and mushroom11Y - 20 < spit2Y < mushroom11Y + 67:
                spit2_state = "ready"
            if mushroom12X - 27 < spit2X < mushroom12X + 63 and mushroom12Y - 20 < spit2Y < mushroom12Y + 67:
                spit2_state = "ready"
    if enemy2hits == 0:
        enemy2healthbar1(enemy2X + 23, enemy2Y + 100)
        enemy2(enemy2X, enemy2Y)
    if enemy2hits == 1:
        enemy2healthbar2(enemy2X + 23, enemy2Y + 100)
        enemy2(enemy2X, enemy2Y)


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
    if enemy2X - 5 < bulletX < enemy2X + 85 and enemy2Y + 16 < bulletY < enemy2Y + 71:
        enemy2hits = enemy2hits + 1
        bullet_state = "ready"
    if mushroom1X - 4 < bulletX < mushroom1X + 83 and mushroom1Y + 5 < bulletY < mushroom1Y + 85:
        bullet_state = "ready"
    if mushroom2X - 4 < bulletX < mushroom2X + 83 and mushroom2Y + 5 < bulletY < mushroom2Y + 85:
        bullet_state = "ready"
    if mushroom3X - 4 < bulletX < mushroom3X + 83 and mushroom3Y + 5 < bulletY < mushroom3Y + 85:
        bullet_state = "ready"
    if mushroom4X - 4 < bulletX < mushroom4X + 83 and mushroom4Y + 5 < bulletY < mushroom4Y + 85:
        bullet_state = "ready"
    if mushroom5X - 4 < bulletX < mushroom5X + 83 and mushroom5Y + 5 < bulletY < mushroom5Y + 85:
        bullet_state = "ready"
    if mushroom6X - 4 < bulletX < mushroom6X + 83 and mushroom6Y + 5 < bulletY < mushroom6Y + 85:
        bullet_state = "ready"
    if mushroom7X - 4 < bulletX < mushroom7X + 83 and mushroom7Y + 5 < bulletY < mushroom7Y + 85:
        bullet_state = "ready"
    if mushroom8X - 4 < bulletX < mushroom8X + 83 and mushroom8Y + 5 < bulletY < mushroom8Y + 85:
        bullet_state = "ready"
    if mushroom9X - 4 < bulletX < mushroom9X + 83 and mushroom9Y + 5 < bulletY < mushroom9Y + 85:
        bullet_state = "ready"
    if mushroom10X - 4 < bulletX < mushroom10X + 83 and mushroom10Y + 5 < bulletY < mushroom10Y + 85:
        bullet_state = "ready"
    if mushroom11X - 4 < bulletX < mushroom11X + 83 and mushroom11Y + 5 < bulletY < mushroom11Y + 85:
        bullet_state = "ready"
    if mushroom12X - 4 < bulletX < mushroom12X + 83 and mushroom12Y + 5 < bulletY < mushroom12Y + 85:
        bullet_state = "ready"

    if enemy1X - 45 < playerX < enemy1X - 40 and enemy1Y - 75 < playerY < enemy1Y + 60:
        playerX = enemy1X - 45
    if enemy1X + 60 < playerX < enemy1X + 65 and enemy1Y - 75 < playerY < enemy1Y + 60:
        playerX = enemy1X + 65
    if enemy1Y - 75 < playerY < enemy1Y - 70 and enemy1X - 45 < playerX < enemy1X + 65:
        playerY = enemy1Y - 75
    if enemy1Y - 55 < playerY < enemy1Y + 60 and enemy1X - 45 < playerX < enemy1X + 65:
        playerY = enemy1Y + 60

    if enemy2X - 45 < playerX < enemy2X - 40 and enemy2Y - 75 < playerY < enemy2Y + 60:
        playerX = enemy2X - 45
    if enemy2X + 60 < playerX < enemy2X + 65 and enemy2Y - 75 < playerY < enemy2Y + 60:
        playerX = enemy2X + 65
    if enemy2Y - 75 < playerY < enemy2Y - 70 and enemy2X - 45 < playerX < enemy2X + 65:
        playerY = enemy2Y - 75
    if enemy2Y - 55 < playerY < enemy2Y + 60 and enemy2X - 45 < playerX < enemy2X + 65:
        playerY = enemy2Y + 60

    if mushroom1X - 50 < playerX < mushroom1X - 45 and mushroom1Y - 77 < playerY < mushroom1Y + 77:
        playerX = mushroom1X - 50
    if mushroom1X + 50 < playerX < mushroom1X + 55 and mushroom1Y - 77 < playerY < mushroom1Y + 77:
        playerX = mushroom1X + 55
    if mushroom1Y - 77 < playerY < mushroom1Y - 72 and mushroom1X - 50 < playerX < mushroom1X + 55:
        playerY = mushroom1Y - 77
    if mushroom1Y + 72 < playerY < mushroom1Y + 77 and mushroom1X - 50 < playerX < mushroom1X + 55:
        playerY = mushroom1Y + 77

    if mushroom2X - 50 < playerX < mushroom2X - 45 and mushroom2Y - 77 < playerY < mushroom2Y + 77:
        playerX = mushroom2X - 50
    if mushroom2X + 50 < playerX < mushroom2X + 55 and mushroom2Y - 77 < playerY < mushroom2Y + 77:
        playerX = mushroom2X + 55
    if mushroom2Y - 77 < playerY < mushroom2Y - 72 and mushroom2X - 50 < playerX < mushroom2X + 55:
        playerY = mushroom2Y - 77
    if mushroom2Y + 72 < playerY < mushroom2Y + 77 and mushroom2X - 50 < playerX < mushroom2X + 55:
        playerY = mushroom2Y + 77

    if mushroom3X - 50 < playerX < mushroom3X - 45 and mushroom3Y - 77 < playerY < mushroom3Y + 77:
        playerX = mushroom3X - 50
    if mushroom3X + 50 < playerX < mushroom3X + 55 and mushroom3Y - 77 < playerY < mushroom3Y + 77:
        playerX = mushroom3X + 55
    if mushroom3Y - 77 < playerY < mushroom3Y - 72 and mushroom3X - 50 < playerX < mushroom3X + 55:
        playerY = mushroom3Y - 77
    if mushroom3Y + 72 < playerY < mushroom3Y + 77 and mushroom3X - 50 < playerX < mushroom3X + 55:
        playerY = mushroom3Y + 77

    if mushroom4X - 50 < playerX < mushroom4X - 45 and mushroom4Y - 77 < playerY < mushroom4Y + 77:
        playerX = mushroom4X - 50
    if mushroom4X + 50 < playerX < mushroom4X + 55 and mushroom4Y - 77 < playerY < mushroom4Y + 77:
        playerX = mushroom4X + 55
    if mushroom4Y - 77 < playerY < mushroom4Y - 72 and mushroom4X - 50 < playerX < mushroom4X + 55:
        playerY = mushroom4Y - 77
    if mushroom4Y + 72 < playerY < mushroom4Y + 77 and mushroom4X - 50 < playerX < mushroom4X + 55:
        playerY = mushroom4Y + 77

    if mushroom5X - 50 < playerX < mushroom5X - 45 and mushroom5Y - 77 < playerY < mushroom5Y + 77:
        playerX = mushroom5X - 50
    if mushroom5X + 50 < playerX < mushroom5X + 55 and mushroom5Y - 77 < playerY < mushroom5Y + 77:
        playerX = mushroom5X + 55
    if mushroom5Y - 77 < playerY < mushroom5Y - 72 and mushroom5X - 50 < playerX < mushroom5X + 55:
        playerY = mushroom5Y - 77
    if mushroom5Y + 72 < playerY < mushroom5Y + 77 and mushroom5X - 50 < playerX < mushroom5X + 55:
        playerY = mushroom5Y + 77

    if mushroom6X - 50 < playerX < mushroom6X - 45 and mushroom6Y - 77 < playerY < mushroom6Y + 77:
        playerX = mushroom6X - 50
    if mushroom6X + 50 < playerX < mushroom6X + 55 and mushroom6Y - 77 < playerY < mushroom6Y + 77:
        playerX = mushroom6X + 55
    if mushroom6Y - 77 < playerY < mushroom6Y - 72 and mushroom6X - 50 < playerX < mushroom6X + 55:
        playerY = mushroom6Y - 77
    if mushroom6Y + 72 < playerY < mushroom6Y + 77 and mushroom6X - 50 < playerX < mushroom6X + 55:
        playerY = mushroom6Y + 77

    if mushroom7X - 50 < playerX < mushroom7X - 45 and mushroom7Y - 77 < playerY < mushroom7Y + 77:
        playerX = mushroom7X - 50
    if mushroom7X + 50 < playerX < mushroom7X + 55 and mushroom7Y - 77 < playerY < mushroom7Y + 77:
        playerX = mushroom7X + 55
    if mushroom7Y - 77 < playerY < mushroom7Y - 72 and mushroom7X - 50 < playerX < mushroom7X + 55:
        playerY = mushroom7Y - 77
    if mushroom7Y + 72 < playerY < mushroom7Y + 77 and mushroom7X - 50 < playerX < mushroom7X + 55:
        playerY = mushroom7Y + 77

    if mushroom8X - 50 < playerX < mushroom8X - 45 and mushroom8Y - 77 < playerY < mushroom8Y + 77:
        playerX = mushroom8X - 50
    if mushroom8X + 50 < playerX < mushroom8X + 55 and mushroom8Y - 77 < playerY < mushroom8Y + 77:
        playerX = mushroom8X + 55
    if mushroom8Y - 77 < playerY < mushroom8Y - 72 and mushroom8X - 50 < playerX < mushroom8X + 55:
        playerY = mushroom8Y - 77
    if mushroom8Y + 72 < playerY < mushroom8Y + 77 and mushroom8X - 50 < playerX < mushroom8X + 55:
        playerY = mushroom8Y + 77

    if mushroom9X - 50 < playerX < mushroom9X - 45 and mushroom9Y - 77 < playerY < mushroom9Y + 77:
        playerX = mushroom9X - 50
    if mushroom9X + 50 < playerX < mushroom9X + 55 and mushroom9Y - 77 < playerY < mushroom9Y + 77:
        playerX = mushroom9X + 55
    if mushroom9Y - 77 < playerY < mushroom9Y - 72 and mushroom9X - 50 < playerX < mushroom9X + 55:
        playerY = mushroom9Y - 77
    if mushroom9Y + 72 < playerY < mushroom9Y + 77 and mushroom9X - 50 < playerX < mushroom9X + 55:
        playerY = mushroom9Y + 77

    if mushroom10X - 50 < playerX < mushroom10X - 45 and mushroom10Y - 77 < playerY < mushroom10Y + 77:
        playerX = mushroom10X - 50
    if mushroom10X + 50 < playerX < mushroom10X + 55 and mushroom10Y - 77 < playerY < mushroom10Y + 77:
        playerX = mushroom10X + 55
    if mushroom10Y - 77 < playerY < mushroom10Y - 72 and mushroom10X - 50 < playerX < mushroom10X + 55:
        playerY = mushroom10Y - 77
    if mushroom10Y + 72 < playerY < mushroom10Y + 77 and mushroom10X - 50 < playerX < mushroom10X + 55:
        playerY = mushroom10Y + 77

    if mushroom11X - 50 < playerX < mushroom11X - 45 and mushroom11Y - 77 < playerY < mushroom11Y + 77:
        playerX = mushroom11X - 50
    if mushroom11X + 50 < playerX < mushroom11X + 55 and mushroom11Y - 77 < playerY < mushroom11Y + 77:
        playerX = mushroom11X + 55
    if mushroom11Y - 77 < playerY < mushroom11Y - 72 and mushroom11X - 50 < playerX < mushroom11X + 55:
        playerY = mushroom11Y - 77
    if mushroom11Y + 72 < playerY < mushroom11Y + 77 and mushroom11X - 50 < playerX < mushroom11X + 55:
        playerY = mushroom11Y + 77

    if mushroom12X - 50 < playerX < mushroom12X - 45 and mushroom12Y - 77 < playerY < mushroom12Y + 77:
        playerX = mushroom12X - 50
    if mushroom12X + 50 < playerX < mushroom12X + 55 and mushroom12Y - 77 < playerY < mushroom12Y + 77:
        playerX = mushroom12X + 55
    if mushroom12Y - 77 < playerY < mushroom12Y - 72 and mushroom12X - 50 < playerX < mushroom12X + 55:
        playerY = mushroom12Y - 77
    if mushroom12Y + 72 < playerY < mushroom12Y + 77 and mushroom12X - 50 < playerX < mushroom12X + 55:
        playerY = mushroom12Y + 77

    if mushroom1X - 50 < enemy1X < mushroom1X - 45 and mushroom1Y - 77 < enemy1Y < mushroom1Y + 77:
        enemy1X = mushroom1X - 50
    if mushroom1X + 50 < enemy1X < mushroom1X + 55 and mushroom1Y - 77 < enemy1Y < mushroom1Y + 77:
        enemy1X = mushroom1X + 55
    if mushroom1Y - 77 < enemy1Y < mushroom1Y - 72 and mushroom1X - 50 < enemy1X < mushroom1X + 55:
        enemy1Y = mushroom1Y - 77
    if mushroom1Y + 72 < enemy1Y < mushroom1Y + 77 and mushroom1X - 50 < enemy1X < mushroom1X + 55:
        enemy1Y = mushroom1Y + 77

    if mushroom2X - 50 < enemy1X < mushroom2X - 45 and mushroom2Y - 77 < enemy1Y < mushroom2Y + 77:
        enemy1X = mushroom2X - 50
    if mushroom2X + 50 < enemy1X < mushroom2X + 55 and mushroom2Y - 77 < enemy1Y < mushroom2Y + 77:
        enemy1X = mushroom2X + 55
    if mushroom2Y - 77 < enemy1Y < mushroom2Y - 72 and mushroom2X - 50 < enemy1X < mushroom2X + 55:
        enemy1Y = mushroom2Y - 77
    if mushroom2Y + 72 < enemy1Y < mushroom2Y + 77 and mushroom2X - 50 < enemy1X < mushroom2X + 55:
        enemy1Y = mushroom2Y + 77

    if mushroom3X - 50 < enemy1X < mushroom3X - 45 and mushroom3Y - 77 < enemy1Y < mushroom3Y + 77:
        enemy1X = mushroom3X - 50
    if mushroom3X + 50 < enemy1X < mushroom3X + 55 and mushroom3Y - 77 < enemy1Y < mushroom3Y + 77:
        enemy1X = mushroom3X + 55
    if mushroom3Y - 77 < enemy1Y < mushroom3Y - 72 and mushroom3X - 50 < enemy1X < mushroom3X + 55:
        enemy1Y = mushroom3Y - 77
    if mushroom3Y + 72 < enemy1Y < mushroom3Y + 77 and mushroom3X - 50 < enemy1X < mushroom3X + 55:
        enemy1Y = mushroom3Y + 77

    if mushroom4X - 50 < enemy1X < mushroom4X - 45 and mushroom4Y - 77 < enemy1Y < mushroom4Y + 77:
        enemy1X = mushroom4X - 50
    if mushroom4X + 50 < enemy1X < mushroom4X + 55 and mushroom4Y - 77 < enemy1Y < mushroom4Y + 77:
        enemy1X = mushroom4X + 55
    if mushroom4Y - 77 < enemy1Y < mushroom4Y - 72 and mushroom4X - 50 < enemy1X < mushroom4X + 55:
        enemy1Y = mushroom4Y - 77
    if mushroom4Y + 72 < enemy1Y < mushroom4Y + 77 and mushroom4X - 50 < enemy1X < mushroom4X + 55:
        enemy1Y = mushroom4Y + 77

    if mushroom5X - 50 < enemy1X < mushroom5X - 45 and mushroom5Y - 77 < enemy1Y < mushroom5Y + 77:
        enemy1X = mushroom5X - 50
    if mushroom5X + 50 < enemy1X < mushroom5X + 55 and mushroom5Y - 77 < enemy1Y < mushroom5Y + 77:
        enemy1X = mushroom5X + 55
    if mushroom5Y - 77 < enemy1Y < mushroom5Y - 72 and mushroom5X - 50 < enemy1X < mushroom5X + 55:
        enemy1Y = mushroom5Y - 77
    if mushroom5Y + 72 < enemy1Y < mushroom5Y + 77 and mushroom5X - 50 < enemy1X < mushroom5X + 55:
        enemy1Y = mushroom5Y + 77

    if mushroom6X - 50 < enemy1X < mushroom6X - 45 and mushroom6Y - 77 < enemy1Y < mushroom6Y + 77:
        enemy1X = mushroom6X - 50
    if mushroom6X + 50 < enemy1X < mushroom6X + 55 and mushroom6Y - 77 < enemy1Y < mushroom6Y + 77:
        enemy1X = mushroom6X + 55
    if mushroom6Y - 77 < enemy1Y < mushroom6Y - 72 and mushroom6X - 50 < enemy1X < mushroom6X + 55:
        enemy1Y = mushroom6Y - 77
    if mushroom6Y + 72 < enemy1Y < mushroom6Y + 77 and mushroom6X - 50 < enemy1X < mushroom6X + 55:
        enemy1Y = mushroom6Y + 77

    if mushroom7X - 50 < enemy1X < mushroom7X - 45 and mushroom7Y - 77 < enemy1Y < mushroom7Y + 77:
        enemy1X = mushroom7X - 50
    if mushroom7X + 50 < enemy1X < mushroom7X + 55 and mushroom7Y - 77 < enemy1Y < mushroom7Y + 77:
        enemy1X = mushroom7X + 55
    if mushroom7Y - 77 < enemy1Y < mushroom7Y - 72 and mushroom7X - 50 < enemy1X < mushroom7X + 55:
        enemy1Y = mushroom7Y - 77
    if mushroom7Y + 72 < enemy1Y < mushroom7Y + 77 and mushroom7X - 50 < enemy1X < mushroom7X + 55:
        enemy1Y = mushroom7Y + 77

    if mushroom8X - 50 < enemy1X < mushroom8X - 45 and mushroom8Y - 77 < enemy1Y < mushroom8Y + 77:
        enemy1X = mushroom8X - 50
    if mushroom8X + 50 < enemy1X < mushroom8X + 55 and mushroom8Y - 77 < enemy1Y < mushroom8Y + 77:
        enemy1X = mushroom8X + 55
    if mushroom8Y - 77 < enemy1Y < mushroom8Y - 72 and mushroom8X - 50 < enemy1X < mushroom8X + 55:
        enemy1Y = mushroom8Y - 77
    if mushroom8Y + 72 < enemy1Y < mushroom8Y + 77 and mushroom8X - 50 < enemy1X < mushroom8X + 55:
        enemy1Y = mushroom8Y + 77

    if mushroom9X - 50 < enemy1X < mushroom9X - 45 and mushroom9Y - 77 < enemy1Y < mushroom9Y + 77:
        enemy1X = mushroom9X - 50
    if mushroom9X + 50 < enemy1X < mushroom9X + 55 and mushroom9Y - 77 < enemy1Y < mushroom9Y + 77:
        enemy1X = mushroom9X + 55
    if mushroom9Y - 77 < enemy1Y < mushroom9Y - 72 and mushroom9X - 50 < enemy1X < mushroom9X + 55:
        enemy1Y = mushroom9Y - 77
    if mushroom9Y + 72 < enemy1Y < mushroom9Y + 77 and mushroom9X - 50 < enemy1X < mushroom9X + 55:
        enemy1Y = mushroom9Y + 77

    if mushroom10X - 50 < enemy1X < mushroom10X - 45 and mushroom10Y - 77 < enemy1Y < mushroom10Y + 77:
        enemy1X = mushroom10X - 50
    if mushroom10X + 50 < enemy1X < mushroom10X + 55 and mushroom10Y - 77 < enemy1Y < mushroom10Y + 77:
        enemy1X = mushroom10X + 55
    if mushroom10Y - 77 < enemy1Y < mushroom10Y - 72 and mushroom10X - 50 < enemy1X < mushroom10X + 55:
        enemy1Y = mushroom10Y - 77
    if mushroom10Y + 72 < enemy1Y < mushroom10Y + 77 and mushroom10X - 50 < enemy1X < mushroom10X + 55:
        enemy1Y = mushroom10Y + 77

    if mushroom11X - 50 < enemy1X < mushroom11X - 45 and mushroom11Y - 77 < enemy1Y < mushroom11Y + 77:
        enemy1X = mushroom11X - 50
    if mushroom11X + 50 < enemy1X < mushroom11X + 55 and mushroom11Y - 77 < enemy1Y < mushroom11Y + 77:
        enemy1X = mushroom11X + 55
    if mushroom11Y - 77 < enemy1Y < mushroom11Y - 72 and mushroom11X - 50 < enemy1X < mushroom11X + 55:
        enemy1Y = mushroom11Y - 77
    if mushroom11Y + 72 < enemy1Y < mushroom11Y + 77 and mushroom11X - 50 < enemy1X < mushroom11X + 55:
        enemy1Y = mushroom11Y + 77

    if mushroom12X - 50 < enemy1X < mushroom12X - 45 and mushroom12Y - 77 < enemy1Y < mushroom12Y + 77:
        enemy1X = mushroom12X - 50
    if mushroom12X + 50 < enemy1X < mushroom12X + 55 and mushroom12Y - 77 < enemy1Y < mushroom12Y + 77:
        enemy1X = mushroom12X + 55
    if mushroom12Y - 77 < enemy1Y < mushroom12Y - 72 and mushroom12X - 50 < enemy1X < mushroom12X + 55:
        enemy1Y = mushroom12Y - 77
    if mushroom12Y + 72 < enemy1Y < mushroom12Y + 77 and mushroom12X - 50 < enemy1X < mushroom12X + 55:
        enemy1Y = mushroom12Y + 77

    if mushroom1X - 50 < enemy2X < mushroom1X - 45 and mushroom1Y - 77 < enemy2Y < mushroom1Y + 77:
        enemy2X = mushroom1X - 50
    if mushroom1X + 50 < enemy2X < mushroom1X + 55 and mushroom1Y - 77 < enemy2Y < mushroom1Y + 77:
        enemy2X = mushroom1X + 55
    if mushroom1Y - 77 < enemy2Y < mushroom1Y - 72 and mushroom1X - 50 < enemy2X < mushroom1X + 55:
        enemy2Y = mushroom1Y - 77
    if mushroom1Y + 72 < enemy2Y < mushroom1Y + 77 and mushroom1X - 50 < enemy2X < mushroom1X + 55:
        enemy2Y = mushroom1Y + 77

    if mushroom2X - 50 < enemy2X < mushroom2X - 45 and mushroom2Y - 77 < enemy2Y < mushroom2Y + 77:
        enemy2X = mushroom2X - 50
    if mushroom2X + 50 < enemy2X < mushroom2X + 55 and mushroom2Y - 77 < enemy2Y < mushroom2Y + 77:
        enemy2X = mushroom2X + 55
    if mushroom2Y - 77 < enemy2Y < mushroom2Y - 72 and mushroom2X - 50 < enemy2X < mushroom2X + 55:
        enemy2Y = mushroom2Y - 77
    if mushroom2Y + 72 < enemy2Y < mushroom2Y + 77 and mushroom2X - 50 < enemy2X < mushroom2X + 55:
        enemy2Y = mushroom2Y + 77

    if mushroom3X - 50 < enemy2X < mushroom3X - 45 and mushroom3Y - 77 < enemy2Y < mushroom3Y + 77:
        enemy2X = mushroom3X - 50
    if mushroom3X + 50 < enemy2X < mushroom3X + 55 and mushroom3Y - 77 < enemy2Y < mushroom3Y + 77:
        enemy2X = mushroom3X + 55
    if mushroom3Y - 77 < enemy2Y < mushroom3Y - 72 and mushroom3X - 50 < enemy2X < mushroom3X + 55:
        enemy2Y = mushroom3Y - 77
    if mushroom3Y + 72 < enemy2Y < mushroom3Y + 77 and mushroom3X - 50 < enemy2X < mushroom3X + 55:
        enemy2Y = mushroom3Y + 77

    if mushroom4X - 50 < enemy2X < mushroom4X - 45 and mushroom4Y - 77 < enemy2Y < mushroom4Y + 77:
        enemy2X = mushroom4X - 50
    if mushroom4X + 50 < enemy2X < mushroom4X + 55 and mushroom4Y - 77 < enemy2Y < mushroom4Y + 77:
        enemy2X = mushroom4X + 55
    if mushroom4Y - 77 < enemy2Y < mushroom4Y - 72 and mushroom4X - 50 < enemy2X < mushroom4X + 55:
        enemy2Y = mushroom4Y - 77
    if mushroom4Y + 72 < enemy2Y < mushroom4Y + 77 and mushroom4X - 50 < enemy2X < mushroom4X + 55:
        enemy2Y = mushroom4Y + 77

    if mushroom5X - 50 < enemy2X < mushroom5X - 45 and mushroom5Y - 77 < enemy2Y < mushroom5Y + 77:
        enemy2X = mushroom5X - 50
    if mushroom5X + 50 < enemy2X < mushroom5X + 55 and mushroom5Y - 77 < enemy2Y < mushroom5Y + 77:
        enemy2X = mushroom5X + 55
    if mushroom5Y - 77 < enemy2Y < mushroom5Y - 72 and mushroom5X - 50 < enemy2X < mushroom5X + 55:
        enemy2Y = mushroom5Y - 77
    if mushroom5Y + 72 < enemy2Y < mushroom5Y + 77 and mushroom5X - 50 < enemy2X < mushroom5X + 55:
        enemy2Y = mushroom5Y + 77

    if mushroom6X - 50 < enemy2X < mushroom6X - 45 and mushroom6Y - 77 < enemy2Y < mushroom6Y + 77:
        enemy2X = mushroom6X - 50
    if mushroom6X + 50 < enemy2X < mushroom6X + 55 and mushroom6Y - 77 < enemy2Y < mushroom6Y + 77:
        enemy2X = mushroom6X + 55
    if mushroom6Y - 77 < enemy2Y < mushroom6Y - 72 and mushroom6X - 50 < enemy2X < mushroom6X + 55:
        enemy2Y = mushroom6Y - 77
    if mushroom6Y + 72 < enemy2Y < mushroom6Y + 77 and mushroom6X - 50 < enemy2X < mushroom6X + 55:
        enemy2Y = mushroom6Y + 77

    if mushroom7X - 50 < enemy2X < mushroom7X - 45 and mushroom7Y - 77 < enemy2Y < mushroom7Y + 77:
        enemy2X = mushroom7X - 50
    if mushroom7X + 50 < enemy2X < mushroom7X + 55 and mushroom7Y - 77 < enemy2Y < mushroom7Y + 77:
        enemy2X = mushroom7X + 55
    if mushroom7Y - 77 < enemy2Y < mushroom7Y - 72 and mushroom7X - 50 < enemy2X < mushroom7X + 55:
        enemy2Y = mushroom7Y - 77
    if mushroom7Y + 72 < enemy2Y < mushroom7Y + 77 and mushroom7X - 50 < enemy2X < mushroom7X + 55:
        enemy2Y = mushroom7Y + 77

    if mushroom8X - 50 < enemy2X < mushroom8X - 45 and mushroom8Y - 77 < enemy2Y < mushroom8Y + 77:
        enemy2X = mushroom8X - 50
    if mushroom8X + 50 < enemy2X < mushroom8X + 55 and mushroom8Y - 77 < enemy2Y < mushroom8Y + 77:
        enemy2X = mushroom8X + 55
    if mushroom8Y - 77 < enemy2Y < mushroom8Y - 72 and mushroom8X - 50 < enemy2X < mushroom8X + 55:
        enemy2Y = mushroom8Y - 77
    if mushroom8Y + 72 < enemy2Y < mushroom8Y + 77 and mushroom8X - 50 < enemy2X < mushroom8X + 55:
        enemy2Y = mushroom8Y + 77

    if mushroom9X - 50 < enemy2X < mushroom9X - 45 and mushroom9Y - 77 < enemy2Y < mushroom9Y + 77:
        enemy2X = mushroom9X - 50
    if mushroom9X + 50 < enemy2X < mushroom9X + 55 and mushroom9Y - 77 < enemy2Y < mushroom9Y + 77:
        enemy2X = mushroom9X + 55
    if mushroom9Y - 77 < enemy2Y < mushroom9Y - 72 and mushroom9X - 50 < enemy2X < mushroom9X + 55:
        enemy2Y = mushroom9Y - 77
    if mushroom9Y + 72 < enemy2Y < mushroom9Y + 77 and mushroom9X - 50 < enemy2X < mushroom9X + 55:
        enemy2Y = mushroom9Y + 77

    if mushroom10X - 50 < enemy2X < mushroom10X - 45 and mushroom10Y - 77 < enemy2Y < mushroom10Y + 77:
        enemy2X = mushroom10X - 50
    if mushroom10X + 50 < enemy2X < mushroom10X + 55 and mushroom10Y - 77 < enemy2Y < mushroom10Y + 77:
        enemy2X = mushroom10X + 55
    if mushroom10Y - 77 < enemy2Y < mushroom10Y - 72 and mushroom10X - 50 < enemy2X < mushroom10X + 55:
        enemy2Y = mushroom10Y - 77
    if mushroom10Y + 72 < enemy2Y < mushroom10Y + 77 and mushroom10X - 50 < enemy2X < mushroom10X + 55:
        enemy2Y = mushroom10Y + 77

    if mushroom11X - 50 < enemy2X < mushroom11X - 45 and mushroom11Y - 77 < enemy2Y < mushroom11Y + 77:
        enemy2X = mushroom11X - 50
    if mushroom11X + 50 < enemy2X < mushroom11X + 55 and mushroom11Y - 77 < enemy2Y < mushroom11Y + 77:
        enemy2X = mushroom11X + 55
    if mushroom11Y - 77 < enemy2Y < mushroom11Y - 72 and mushroom11X - 50 < enemy2X < mushroom11X + 55:
        enemy2Y = mushroom11Y - 77
    if mushroom11Y + 72 < enemy2Y < mushroom11Y + 77 and mushroom11X - 50 < enemy2X < mushroom11X + 55:
        enemy2Y = mushroom11Y + 77

    if mushroom12X - 50 < enemy2X < mushroom12X - 45 and mushroom12Y - 77 < enemy2Y < mushroom12Y + 77:
        enemy2X = mushroom12X - 50
    if mushroom12X + 50 < enemy2X < mushroom12X + 55 and mushroom12Y - 77 < enemy2Y < mushroom12Y + 77:
        enemy2X = mushroom12X + 55
    if mushroom12Y - 77 < enemy2Y < mushroom12Y - 72 and mushroom12X - 50 < enemy2X < mushroom12X + 55:
        enemy2Y = mushroom12Y - 77
    if mushroom12Y + 72 < enemy2Y < mushroom12Y + 77 and mushroom12X - 50 < enemy2X < mushroom12X + 55:
        enemy2Y = mushroom12Y + 77

    player(playerX, playerY)
    mushroom1(mushroom1X, mushroom1Y)
    mushroom1(mushroom2X, mushroom2Y)
    mushroom1(mushroom3X, mushroom3Y)
    mushroom1(mushroom4X, mushroom4Y)
    mushroom1(mushroom5X, mushroom5Y)
    mushroom1(mushroom6X, mushroom6Y)
    mushroom1(mushroom7X, mushroom7Y)
    mushroom1(mushroom8X, mushroom8Y)
    mushroom1(mushroom9X, mushroom9Y)
    mushroom1(mushroom10X, mushroom10Y)
    mushroom1(mushroom11X, mushroom11Y)
    mushroom1(mushroom12X, mushroom12Y)
    pygame.display.update()