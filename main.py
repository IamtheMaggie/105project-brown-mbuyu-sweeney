import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 800))

enemy1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-200x200.png')
enemy1Img = pygame.transform.scale(enemy1Img, (100, 100))
enemy1X = 100
enemy1Y = 100

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

playerImg = pygame.image.load(r'C:\Users\Mmwwa\Pictures\tank-2.png')
playerX = 500
playerY = 500
playerY_change = 0
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

bulletImg = pygame.image.load(r'C:\Users\Mmwwa\Pictures\bullet.png')
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
    screen.fill((255, 255, 255))
    slopeX = 0
    slopeY = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            slopeX, slopeY = pygame.mouse.get_pos()
            fire_bullet(playerX, bulletY)

    playerY += playerY_change
    playerX += playerX_change

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
        if spit1X > 1000 or spit1X < 0 or spit1Y > 800 or spit1X < 0:
            spit1_state = "ready"

    if bullet_state is "ready":
        bulletX = playerX
        bulletY = playerY
        anglebullet = math.atan2((slopeY - playerY), (slopeX - playerX))
        bullet.angle = math.degrees(anglebullet)
        SPEEDbullet = .3
    if bullet_state is "fire":
        fire_bullet(playerX, playerY)
        bulletY += math.sin(anglebullet) * SPEEDbullet
        bulletX += math.cos(anglebullet) * SPEEDbullet
        if bulletX > 1000 or bulletX < 0 or bulletY > 800 or bulletX < 0:
            bullet_state = "ready"

    enemy1(enemy1X, enemy1Y)
    player(playerX, playerY)
    pygame.display.update()