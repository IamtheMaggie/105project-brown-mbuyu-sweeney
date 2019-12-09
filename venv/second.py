import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
enemy1hits = 0
enemy2hits = 0
playerhits = 0

sunflower1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-40x80.png')
sunflower1X = 200
sunflower1Y = 100

sunflower2X = 200
sunflower2Y = 300

sunflower3X = 200
sunflower3Y = 500

sunflower4X = 750
sunflower4Y = 100

sunflower5X = 750
sunflower5Y = 300

sunflower6X = 750
sunflower6Y = 500

def sunflower1(x,y):
    screen.blit(sunflower1Img, (x, y))


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
enemy1X = 840
enemy1Y = 500
enemy1Y_change = .1
enemy1direction = 1

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

enemy2X = 60
enemy2Y = 80
enemy2Y_change = .1
enemy2direction = 0

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
playerX = 450
playerY = 300
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


    if enemy2Y <= 80:
        enemy2direction = 0
    if enemy2Y >= 500:
        enemy2direction = 1
    if enemy2direction == 0:
        enemy2Y += enemy2Y_change
    if enemy2direction == 1:
        enemy2Y -= enemy2Y_change

    if enemy1Y <= 80:
        enemy1direction = 0
    if enemy1Y >= 500:
        enemy1direction = 1
    if enemy1direction == 0:
        enemy1Y += enemy1Y_change
    if enemy1direction == 1:
        enemy1Y -= enemy1Y_change

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
            if sunflower1Y - 35 < spit1Y < sunflower1Y + 60 and sunflower1X - 39 < spit1X < sunflower1X + 20:
                spit1_state = "ready"
            if sunflower2Y - 35 < spit1Y < sunflower2Y + 60 and sunflower2X - 39 < spit1X < sunflower2X + 20:
                spit1_state = "ready"
            if sunflower3Y - 35 < spit1Y < sunflower3Y + 60 and sunflower3X - 39 < spit1X < sunflower3X + 20:
                spit1_state = "ready"
            if sunflower4Y - 35 < spit1Y < sunflower4Y + 60 and sunflower4X - 39 < spit1X < sunflower4X + 20:
                spit1_state = "ready"
            if sunflower5Y - 35 < spit1Y < sunflower5Y + 60 and sunflower5X - 39 < spit1X < sunflower5X + 20:
                spit1_state = "ready"
            if sunflower6Y - 35 < spit1Y < sunflower6Y + 60 and sunflower6X - 39 < spit1X < sunflower6X + 20:
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
            if sunflower1Y - 35 < spit2Y < sunflower1Y + 60 and sunflower1X - 39 < spit2X < sunflower1X + 20:
                spit2_state = "ready"
            if sunflower2Y - 35 < spit2Y < sunflower2Y + 60 and sunflower2X - 39 < spit2X < sunflower2X + 20:
                spit2_state = "ready"
            if sunflower3Y - 35 < spit2Y < sunflower3Y + 60 and sunflower3X - 39 < spit2X < sunflower3X + 20:
                spit2_state = "ready"
            if sunflower4Y - 35 < spit2Y < sunflower4Y + 60 and sunflower4X - 39 < spit2X < sunflower4X + 20:
                spit2_state = "ready"
            if sunflower5Y - 35 < spit2Y < sunflower5Y + 60 and sunflower5X - 39 < spit2X < sunflower5X + 20:
                spit2_state = "ready"
            if sunflower6Y - 35 < spit2Y < sunflower6Y + 60 and sunflower6X - 39 < spit2X < sunflower6X + 20:
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
    if sunflower1Y - 10 < bulletY < sunflower1Y + 77 and sunflower1X - 10 < bulletX < sunflower1X + 33:
        bullet_state = "ready"
    if sunflower2Y - 10 < bulletY < sunflower2Y + 77 and sunflower2X - 10 < bulletX < sunflower2X + 33:
        bullet_state = "ready"
    if sunflower3Y - 10 < bulletY < sunflower3Y + 77 and sunflower3X - 10 < bulletX < sunflower3X + 33:
        bullet_state = "ready"
    if sunflower4Y - 10 < bulletY < sunflower4Y + 77 and sunflower4X - 10 < bulletX < sunflower4X + 33:
        bullet_state = "ready"
    if sunflower5Y - 10 < bulletY < sunflower5Y + 77 and sunflower5X - 10 < bulletX < sunflower5X + 33:
        bullet_state = "ready"
    if sunflower6Y - 10 < bulletY < sunflower6Y + 77 and sunflower6X - 10 < bulletX < sunflower6X + 33:
        bullet_state = "ready"

    if sunflower1X - 61 < playerX < sunflower1X - 55 and sunflower1Y - 90 < playerY < sunflower1Y + 72:
        playerX = sunflower1X - 61
    if sunflower1X + 5 < playerX < sunflower1X + 10 and sunflower1Y - 90 < playerY < sunflower1Y + 72:
        playerX = sunflower1X + 10
    if sunflower1Y - 90 < playerY < sunflower1Y - 85 and sunflower1X - 61 < playerX < sunflower1X + 10:
        playerY = sunflower1Y - 90
    if sunflower1Y + 65 < playerY < sunflower1Y + 72 and sunflower1X - 61 < playerX < sunflower1X + 10:
        playerY = sunflower1Y + 72

    if sunflower2X - 61 < playerX < sunflower2X - 55 and sunflower2Y - 90 < playerY < sunflower2Y + 72:
        playerX = sunflower2X - 61
    if sunflower2X + 5 < playerX < sunflower2X + 10 and sunflower2Y - 90 < playerY < sunflower2Y + 72:
        playerX = sunflower2X + 10
    if sunflower2Y - 90 < playerY < sunflower2Y - 85 and sunflower2X - 61 < playerX < sunflower2X + 10:
        playerY = sunflower2Y - 90
    if sunflower2Y + 65 < playerY < sunflower2Y + 72 and sunflower2X - 61 < playerX < sunflower2X + 10:
        playerY = sunflower2Y + 72

    if sunflower3X - 61 < playerX < sunflower3X - 55 and sunflower3Y - 90 < playerY < sunflower3Y + 72:
        playerX = sunflower3X - 61
    if sunflower3X + 5 < playerX < sunflower3X + 10 and sunflower3Y - 90 < playerY < sunflower3Y + 72:
        playerX = sunflower3X + 10
    if sunflower3Y - 90 < playerY < sunflower3Y - 85 and sunflower3X - 61 < playerX < sunflower3X + 10:
        playerY = sunflower3Y - 90
    if sunflower3Y + 65 < playerY < sunflower3Y + 72 and sunflower3X - 61 < playerX < sunflower3X + 10:
        playerY = sunflower3Y + 72

    if sunflower4X - 61 < playerX < sunflower4X - 55 and sunflower4Y - 90 < playerY < sunflower4Y + 72:
        playerX = sunflower4X - 61
    if sunflower4X + 5 < playerX < sunflower4X + 10 and sunflower4Y - 90 < playerY < sunflower4Y + 72:
        playerX = sunflower4X + 10
    if sunflower4Y - 90 < playerY < sunflower4Y - 85 and sunflower4X - 61 < playerX < sunflower4X + 10:
        playerY = sunflower4Y - 90
    if sunflower4Y + 65 < playerY < sunflower4Y + 72 and sunflower4X - 61 < playerX < sunflower4X + 10:
        playerY = sunflower4Y + 72

    if sunflower5X - 61 < playerX < sunflower5X - 55 and sunflower5Y - 90 < playerY < sunflower5Y + 72:
        playerX = sunflower5X - 61
    if sunflower5X + 5 < playerX < sunflower5X + 10 and sunflower5Y - 90 < playerY < sunflower5Y + 72:
        playerX = sunflower5X + 10
    if sunflower5Y - 90 < playerY < sunflower5Y - 85 and sunflower5X - 61 < playerX < sunflower5X + 10:
        playerY = sunflower5Y - 90
    if sunflower5Y + 65 < playerY < sunflower5Y + 72 and sunflower5X - 61 < playerX < sunflower5X + 10:
        playerY = sunflower5Y + 72

    if sunflower6X - 61 < playerX < sunflower6X - 55 and sunflower6Y - 90 < playerY < sunflower6Y + 72:
        playerX = sunflower6X - 61
    if sunflower6X + 5 < playerX < sunflower6X + 10 and sunflower6Y - 90 < playerY < sunflower6Y + 72:
        playerX = sunflower6X + 10
    if sunflower6Y - 90 < playerY < sunflower6Y - 85 and sunflower6X - 61 < playerX < sunflower6X + 10:
        playerY = sunflower6Y - 90
    if sunflower6Y + 65 < playerY < sunflower6Y + 72 and sunflower6X - 61 < playerX < sunflower6X + 10:
        playerY = sunflower6Y + 72

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

    player(playerX, playerY)
    sunflower1(sunflower1X, sunflower1Y)
    sunflower1(sunflower2X, sunflower2Y)
    sunflower1(sunflower3X, sunflower3Y)
    sunflower1(sunflower4X, sunflower4Y)
    sunflower1(sunflower5X, sunflower5Y)
    sunflower1(sunflower6X, sunflower6Y)
    pygame.display.update()