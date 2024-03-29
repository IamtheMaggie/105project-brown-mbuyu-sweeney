import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
enemy1hits = 0
enemy2hits = 0
playerhits = 0

#pump1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-100x100.png')
#pump1X = 0
#pump1Y = 0

#def pump1(x,y):
   # screen.blit(pump1Img,(x, y))

fence1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-100x100(1).png')
fence1X = 130
fence1Y = 340

fence2X = 540
fence2Y = 340

fence3X = 640
fence3Y = 340

def fence1(x,y):
    screen.blit(fence1Img,(x, y))

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
          #  if pump1X - 35 < spit1X < pump1X + 65 and pump1Y - 10 < spit1Y < pump1Y + 55:
             #   spit1_state = "ready"
            if fence1X - 43 < spit1X < fence1X + 75 and fence1Y < spit1Y < fence1Y + 80:
                spit1_state = "ready"
            if fence2X - 43 < spit1X < fence2X + 75 and fence2Y < spit1Y < fence2Y + 80:
                spit1_state = "ready"
            if fence3X - 43 < spit1X < fence3X + 75 and fence3Y < spit1Y < fence3Y + 80:
                spit1_state = "ready"
    if enemy1hits == 0:
        enemy1healthbar1(enemy1X + 23, enemy1Y + 100)
        enemy1(enemy1X, enemy1Y)
    if enemy1hits == 1:
        enemy1healthbar2(enemy1X + 23, enemy1Y + 100)
        enemy1(enemy1X, enemy1Y)

    if enemy2hits < 2:
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
        #    if pump1X - 35 < spit2X < pump1X + 65 and pump1Y - 10 < spit2Y < pump1Y + 55:
             #   spit2_state = "ready"
            if fence1X - 43 < spit2X < fence1X + 75 and fence1Y < spit2Y < fence1Y + 80:
                spit2_state = "ready"
            if fence2X - 43 < spit2X < fence2X + 75 and fence2Y < spit2Y < fence2Y + 80:
                spit2_state = "ready"
            if fence3X - 43 < spit2X < fence3X + 75 and fence3Y < spit2Y < fence3Y + 80:
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
   # if pump1X - 13 < bulletX < pump1X + 84 and pump1Y + 20 < bulletY < pump1Y + 75:
      #  bullet_state = "ready"
    if fence1X - 17 < bulletX < fence1X + 97 and fence1Y + 28 < bulletY < fence1Y + 98:
        bullet_state = "ready"
    if fence2X - 17 < bulletX < fence2X + 97 and fence2Y + 28 < bulletY < fence2Y + 98:
        bullet_state = "ready"
    if fence3X - 17 < bulletX < fence3X + 97 and fence3Y + 28 < bulletY < fence3Y + 98:
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

 #   if pump1X - 60 < playerX < pump1X - 55 and pump1Y - 65 < playerY < pump1Y + 65:
     #   playerX = pump1X - 60
  #  if pump1X + 55 < playerX < pump1X + 60 and pump1Y - 65 < playerY < pump1Y + 65:
       # playerX = pump1X + 60
   # if pump1Y - 65 < playerY < pump1Y - 60 and pump1X - 60 < playerX < pump1X + 60:
       # playerY = pump1Y - 65
  #  if pump1Y + 60 < playerY < pump1Y + 65 and pump1X - 60 < playerX < pump1X + 60:
       # playerY = pump1Y + 65

    if fence1X - 65 < playerX < fence1X - 60 and fence1Y -55 < playerY < fence1Y + 90:
        playerX = fence1X - 65
    if fence1X + 63 < playerX < fence1X + 68 and fence1Y -55 < playerY < fence1Y + 90:
        playerX = fence1X + 68
    if fence1Y - 55 < playerY < fence1Y - 50 and fence1X - 65 < playerX < fence1X + 68:
        playerY = fence1Y - 55
    if fence1Y + 85 < playerY < fence1Y + 90 and fence1X - 65 < playerX < fence1X + 68:
        playerY = fence1Y + 90

    if fence2X - 65 < playerX < fence2X - 60 and fence2Y -55 < playerY < fence2Y + 90:
        playerX = fence2X - 65
    if fence2X + 63 < playerX < fence2X + 68 and fence2Y -55 < playerY < fence2Y + 90:
        playerX = fence2X + 68
    if fence2Y - 55 < playerY < fence2Y - 50 and fence2X - 65 < playerX < fence2X + 68:
        playerY = fence2Y - 55
    if fence2Y + 85 < playerY < fence2Y + 90 and fence2X - 65 < playerX < fence2X + 68:
        playerY = fence2Y + 90

    if fence3X - 65 < playerX < fence3X - 60 and fence3Y -55 < playerY < fence3Y + 90:
        playerX = fence3X - 65
    if fence3X + 63 < playerX < fence3X + 68 and fence3Y -55 < playerY < fence3Y + 90:
        playerX = fence3X + 68
    if fence3Y - 55 < playerY < fence3Y - 50 and fence3X - 65 < playerX < fence3X + 68:
        playerY = fence3Y - 55
    if fence3Y + 85 < playerY < fence3Y + 90 and fence3X - 65 < playerX < fence3X + 68:
        playerY = fence3Y + 90


    player(playerX, playerY)
    fence1(fence1X, fence1Y)
    fence1(fence2X, fence2Y)
    fence1(fence3X, fence3Y)
    pygame.display.update()