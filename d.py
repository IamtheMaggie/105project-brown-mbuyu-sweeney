import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))

playerImg = pygame.image.load(r'C:\Users\Mmwwa\Downloads\Girl 0.png')
playerImg = pygame.transform.scale(playerImg, (100, 100))
playerX = 150
playerY = 150
playerY_change = 0
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))


enemy1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-200x200.png')
enemyImg = pygame.transform.scale(enemy1Img, (100, 100))
enemy1Img = pygame.transform.scale(enemy1Img, (60, 60))
enemy1X = 500
enemy1Y = 350
enemy1Y_change = 0

def enemy1(x,y):
    screen.blit(bulletImg, (x+30, y+42))
    screen.blit(enemy1Img, (x, y))

bulletImg = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-20x20.png')


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
    playerY += playerY_change
    playerX += playerX_change
    enemy1(enemy1X, enemy1Y)
    player(playerX, playerY)
    pygame.display.update()