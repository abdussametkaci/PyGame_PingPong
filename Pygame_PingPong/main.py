# Reference: 
# https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/

# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball
from random import randint

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the car to the list of objects
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates - FPS
clock = pygame.time.Clock()

# Initialise player scores and combos
scoreA = 0
scoreB = 0
comboA = 0
comboB = 0

# Player Combo active or inactive
comboActiveA = False
comboActiveB = False

# Lock key of playerA or playerB
lockB = False
lockA = False

timer = 1

# -------- Main Program Loop -----------
while carryOn:

    # Quit Condition
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    # Combo Bar. If combo score greater than 200, combo activated.
    if comboA > 200:
        comboA = 0
        comboActiveA = True
        lockB = True
    if comboB > 200:
        comboB = 0
        comboActiveB = True
        lockA = True

    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and lockA == False:
        paddleA.moveUp(5)
    if keys[pygame.K_s] and lockA == False:
        paddleA.moveDown(5)
    if keys[pygame.K_UP] and lockB == False:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN] and lockB == False:
        paddleB.moveDown(5)
    
    # --- Game logic should go here
    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA = scoreA + 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB = scoreB + 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    # Collision Detection between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce() 

    # Stop combo counter for 5 seconds if any user's combo is active.
    if comboActiveA or comboActiveB:
        timer = timer + 1
        if timer > 100:
            timer = 0
            lockA = False
            lockB = False
            comboActiveA = False
            comboActiveB = False

    if comboActiveA == False:
        comboA = comboA + scoreA

    if comboActiveB == False:
        comboB = comboB + scoreB

    # --- Drawing code should go here
    # First, clear the screen to black. 
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    combo_font = pygame.font.Font(None, 28)
    text = combo_font.render(str(f"Combo: {comboA / 10}"), 1, WHITE)
    screen.blit(text, (230, 60))
    text = combo_font.render(str(f"Combo: {comboB / 10}"), 1, WHITE)
    screen.blit(text, (410, 60))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()