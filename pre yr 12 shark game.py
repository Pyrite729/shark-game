import pygame
import time
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()


running = True
angle = 0

left_button = pygame.image.load("left button.png").convert_alpha()
right_button = pygame.image.load("right button.png").convert_alpha()
light_left_button = pygame.image.load("light left button.png").convert_alpha()
light_right_button = pygame.image.load("light right button.png").convert_alpha()
big_left_button = pygame.image.load("big left button.png").convert_alpha()
big_right_button = pygame.image.load("big right button.png").convert_alpha()

## circle = pygame.image.load("circle.png").convert_alpha()

sign = pygame.image.load("sighn.png").convert_alpha()
sighn_eyes = pygame.image.load("sighn eyes.png").convert_alpha()

epp_shark = pygame.image.load("epp shark.png").convert_alpha()

empty_card = pygame.image.load("card.png").convert_alpha()

epp_shark_card = pygame.image.load("epp shark card.png").convert_alpha()
big_epp_shark_card = pygame.image.load("big epp shark card.png").convert_alpha()
big_light_epp_shark_card = pygame.image.load("big light epp shark card.png").convert_alpha()


left_button_rect = left_button.get_rect(topleft=(80, 360))
right_button_rect = right_button.get_rect(topleft=(910, 360))
sign_rect = sign.get_rect(topleft=(273, 20))
## epp_shark_rect = epp_shark.get_rect(topleft=(425, 280))
## empty_card_rect = empty_card.get_rect(topleft=(420, 260))
epp_shark_card_rect = epp_shark_card.get_rect(topleft=(430, 260))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((87, 132, 191))

    screen.blit(epp_shark_card, (430, 260))
    screen.blit(left_button, (80, 360))
    screen.blit(right_button, (910, 360))
    ##screen.blit(circle, (278, 200))
    screen.blit(sign, (268, 20))
    ## screen.blit(epp_shark, (425, 280))

    if left_button_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(light_left_button, (80, 360))
    if right_button_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(light_right_button, (910, 360))
    if epp_shark_card_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(big_light_epp_shark_card, (430, 260))

##    spinning_shark = pygame.transform.rotate(epp_shark, angle)

    if angle >= 360:
        angle = 0
    else:
        angle += 1


    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
        if left_button_rect.collidepoint(mouse_position):
            screen.blit(big_left_button, (62, 340))
        if right_button_rect.collidepoint(mouse_position):
            screen.blit(big_right_button, (910, 340))
        if sign_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(sighn_eyes, (268, 20))
        if epp_shark_card_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(big_epp_shark_card, (425, 255))            


##            screen.blit(spinning_shark, (350, 210))

 ##   pygame.draw.rect(screen, (255, 255, 255), left_button_rect, 2)
 ##   pygame.draw.rect(screen, (255, 255, 255), right_button_rect, 2)
 ##   pygame.draw.rect(screen, (255, 255, 255), sign_rect, 2)  
 ##   pygame.draw.rect(screen, (255, 255, 255), epp_shark_rect, 2)

    pygame.display.flip()
    angle += 1

    clock.tick(60)

pygame.quit()
