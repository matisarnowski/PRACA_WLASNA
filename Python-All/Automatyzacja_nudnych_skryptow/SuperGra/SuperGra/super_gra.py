from turtle import speed
import pygame, sys

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

speed = [3, 3]

running = True

icon = pygame.image.load(
    "/home/mateuszs/Project/VSC_Project/python_code/SuperGra/assets/alien-head.png"
)
my_icon = pygame.display.set_icon(icon)
alien = pygame.image.load(
    "/home/mateuszs/Project/VSC_Project/python_code/SuperGra/assets/alien.png"
)
alien_move = alien.get_rect()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    alien_move = alien_move.move(speed)

    if alien_move.left < 0 or alien_move.right > width:
        speed[0] = -speed[0]
    if alien_move.top < 0 or alien_move.bottom > height:
        speed[1] = -speed[1]
    screen.fill((250, 128, 114))
    screen.blit(alien, alien_move)
    pygame.display.flip()
