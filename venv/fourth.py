import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 700))
enemy1hits = 0
enemy2hits = 0
enemy3hits = 0
enemy4hits = 0
playerhits = 0

enemy1healthbar1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-30x7.png')
enemy1healthbar1Img = pygame.transform.scale(enemy1healthbar1Img, (50, 10))
enemy1healthbar2Img = pygame.transform.scale(enemy1healthbar1Img, (25, 0))

def enemy1healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def enemy2healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def enemy3healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def enemy4healthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x,y))

def enemy4healthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x,y))

def playerhealthbar1(x,y):
    screen.blit(enemy1healthbar1Img, (x, y))

def playerhealthbar2(x,y):
    screen.blit(enemy1healthbar2Img, (x, y))

enemy1Img = pygame.image.load(r'C:\Users\Mmwwa\Downloads\pixel-200x200.png')
enemyImg = pygame.transform.scale(enemy1Img, (100, 100))
enemy1Img = pygame.transform.scale(enemy1Img, (60, 60))
enemy1X = -20
enemy1Y = 350
enemy1Y_change = 0

def enemy1(x,y):
    screen.blit(enemy1Img, (x, y))

enemy2X = 350
enemy2Y = 700

def enemy2(x,y):
    screen.blit(enemy1Img, (x, y))

enemy3X = 350
enemy3Y = -20

def enemy3(x,y):
    screen.blit(enemy1Img, (x, y))

enemy4X = 840
enemy4Y = 350
enemy4direction = 0

def enemy4(x,y):
    screen.blit(enemyImg, (x, y))

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
    screen.blit(bulletImg, (x,y))

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

    if enemy4Y <= 80:
        enemy4direction = 0
    if enemy4Y >= 500:
        enemy4direction = 1
    if enemy4direction == 0:
        enemy4Y += .1
    if enemy4direction == 1:
        enemy4Y -= .1

    if enemy1hits == 0:
        angle3 = math.atan2((playerY - enemy1Y), (playerX - enemy1X))
        enemy1.angle3 = math.degrees(angle3)
        if playerY - 33 > enemy1Y or enemy1Y > playerY + 71 or playerX - 30 > enemy1X or enemy1X > playerX + 58:
            enemy1Y += math.sin(angle3) * .05
            enemy1X += math.cos(angle3) * .05
        if playerY - 36 <= enemy1Y <= playerY + 74 and playerX - 33 <= enemy1X <= playerX + 61:
            if playerX_change > 0:
                playerX_change = .025
            if playerX_change < 0:
                playerX_change = -.025
            if playerY_change > 0:
                playerY_change = .025
            if playerY_change < 0:
                playerY_change = -.025
            enemy1Y += playerY_change
            enemy1X += playerX_change
        enemy1(enemy1X, enemy1Y)
        enemy1healthbar1(enemy1X + 23, enemy1Y + 100)
    if enemy1hits > 0:
        enemy1Y = 350
        enemy1X = -20
        enemy1hits = 0

    if enemy2hits == 0:
        angle4 = math.atan2((playerY - enemy2Y), (playerX - enemy2X))
        enemy2.angle4 = math.degrees(angle4)
        if playerY - 33 > enemy2Y or enemy2Y > playerY + 71 or playerX - 30 > enemy2X or enemy2X > playerX + 58:
            enemy2Y += math.sin(angle4) * .05
            enemy2X += math.cos(angle4) * .05
        if playerY - 36 <= enemy2Y <= playerY + 74 and playerX - 33 <= enemy2X <= playerX + 61:
            if playerX_change > 0:
                playerX_change = .025
            if playerX_change < 0:
                playerX_change = -.025
            if playerY_change > 0:
                playerY_change = .025
            if playerY_change < 0:
                playerY_change = -.025
            enemy2Y += playerY_change
            enemy2X += playerX_change
        enemy1(enemy2X, enemy2Y)
        enemy2healthbar1(enemy2X + 23, enemy2Y + 100)
    if enemy2hits > 0:
        enemy2Y = 700
        enemy2X = 350
        enemy2hits = 0


    if enemy3hits == 0:
        angle5 = math.atan2((playerY - enemy3Y), (playerX - enemy3X))
        enemy3.angle4 = math.degrees(angle5)
        if playerY - 33 > enemy3Y or enemy3Y > playerY + 71 or playerX - 30 > enemy3X or enemy3X > playerX + 58:
            enemy3Y += math.sin(angle5) * .05
            enemy3X += math.cos(angle5) * .05
        if playerY - 36 <= enemy3Y <= playerY + 74 and playerX - 33 <= enemy3X <= playerX + 61:
            if playerX_change > 0:
                playerX_change = .025
            if playerX_change < 0:
                playerX_change = -.025
            if playerY_change > 0:
                playerY_change = .025
            if playerY_change < 0:
                playerY_change = -.025
            enemy3Y += playerY_change
            enemy3X += playerX_change
        enemy1(enemy3X, enemy3Y)
        enemy3healthbar1(enemy3X + 23, enemy3Y + 100)
    if enemy3hits > 0:
        enemy3Y = -20
        enemy3X = 350
        enemy3hits = 0

    if enemy4hits < 2:
        if spit1_state is "ready":
            spit1X = enemy4X
            spit1Y = enemy4Y
            angle = math.atan2((playerY - enemy4Y), (playerX - enemy4X))
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
    if enemy4hits == 0:
        enemy4healthbar1(enemy4X + 23, enemy4Y + 100)
        enemy4(enemy4X, enemy4Y)
    if enemy4hits == 1:
        enemy4healthbar2(enemy4X + 23, enemy4Y + 100)
        enemy4(enemy4X, enemy4Y)

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
    if enemy1X - 10 < bulletX < enemy1X + 54 and enemy1Y + 5 < bulletY < enemy1Y + 42:
        enemy1hits = enemy1hits + 1
        bullet_state = "ready"
    if enemy2X - 10 < bulletX < enemy2X + 54 and enemy2Y + 5 < bulletY < enemy2Y + 42:
        enemy2hits = enemy2hits + 1
        bullet_state = "ready"
    if enemy3X - 10 < bulletX < enemy3X + 54 and enemy3Y + 5 < bulletY < enemy3Y + 42:
        enemy3hits = enemy3hits + 1
        bullet_state = "ready"
    if enemy4X - 5 < bulletX < enemy4X + 85 and enemy4Y + 16 < bulletY < enemy4Y + 71:
        enemy4hits = enemy4hits + 1
        bullet_state = "ready"

    if enemy4X - 45 < playerX < enemy4X - 40 and enemy4Y - 75 < playerY < enemy4Y + 60:
        playerX = enemy4X - 45
    if enemy4X + 60 < playerX < enemy4X + 65 and enemy4Y - 75 < playerY < enemy4Y + 60:
        playerX = enemy4X + 65
    if enemy4Y - 75 < playerY < enemy4Y - 70 and enemy4X - 45 < playerX < enemy4X + 65:
        playerY = enemy4Y - 75
    if enemy4Y - 55 < playerY < enemy4Y + 60 and enemy4X - 45 < playerX < enemy4X + 65:
        playerY = enemy4Y + 60

    player(playerX, playerY)
    pygame.display.update()