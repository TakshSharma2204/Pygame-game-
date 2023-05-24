#Importing Packages
import pygame,sys
import random

#Initializing Pygame
pygame.init()

#Game Specific Variables
FPS = pygame.time.Clock()
screen_Width = 1165
screen_Height = 1860
snakeX = 300
snakeY = 300
snakeHeight = 30
snakeWidth = 30
black =(0, 0, 0)
velocityX = 0
velocityY = 0
red = (255, 0, 0)
gray=(255,255,255)
foodX = random.randint(50, 850)
foodY = random.randint(50,  1050)
score = 0
default_velocity  = 0

#Initializing Screen
screen = pygame.display.set_mode((screen_Width, screen_Height))

#Increasing speed according to score
if score >= 5:
    default_velocity += 2
elif score >= 10:
    default_velocity += 2
#Game Loop
playing = True
while playing:
    screen.fill(gray)    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.quit()
        velocityX += default_velocity
        velocityY += default_velocity
        if event.type == pygame.KEYDOWN:           
            if event.key == pygame.K_l: 
                velocityX = 6
                velocityY = 0
            if event.key == pygame.K_a: 
                velocityX = -6
                velocityY = 0
            if event.key == pygame.K_BACKSPACE: 
                velocityX = 0
                velocityY = -6
            if event.key == pygame.K_RETURN: 
                velocityX = 0
                velocityY = 6
    if snakeX <= 0 or snakeX >= screen_Width:
        mess = pygame.font.Font(None, 100)
        text = mess.render(f'Game Over !' , True, (0, 0, 0))
        screen.blit(text, (400, 650))
        
    elif snakeY <= 0 or snakeY >= screen_Height:
        mess = pygame.font.Font(None, 100)
        text = mess.render('Game Over' , True, (0, 0, 0))
        screen.blit(text, (400, 650))
    elif snakeY == screen_Height:
        mess = pygame.font.Font(None, 100)
        text = mess.render('Game Over' , True, (0, 0, 0))
        screen.blit(text, (400, 650))
    if abs(snakeX - foodX)<15 and abs(snakeY - foodY)<15:
        score +=1
        foodX = random.randint(20, screen_Width)
        foodY = random.randint(80, screen_Height / 2)
    

    snakeY += velocityY
    snakeX += velocityX
    mess = pygame.font.Font(None, 62)
    text = mess.render(f'score: {score}' , True, (0, 0, 0))
    screen.blit(text, (30, 30))
    pygame.draw.rect(screen, 'red', (foodX, foodY, snakeWidth,  snakeHeight))
    pygame.draw.rect(screen, 'black', (snakeX, snakeY, snakeWidth,  snakeHeight))
    FPS.tick(60)
    pygame.display.update()