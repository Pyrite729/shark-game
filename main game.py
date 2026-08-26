import pygame
import spritesheet
import Buttons
from Buttons import Button
import math

pygame.init()
screen_w = (1080)
screen_h = (720)
screen = pygame.display.set_mode((screen_w, screen_h))

running = True
animation_plays = False
clock = pygame.time.Clock()
FPS = 30
black = (0, 0, 0)
# end of init stuff ------------------------------------------------


# image load -----------------------------------------------------------
sprite_sheet_image = pygame.image.load("sprite walk.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
start_button = pygame.image.load("start button.png").convert_alpha()
background = pygame.image.load("racing lanes.png").convert_alpha()
background_w = background.get_width()
background_h = background.get_height()
start_button_interact = Button(0, 0, start_button, 1)
# image load end -------------------------------------------------------

# scroll ---------------------------------------------------------------
scroll = 0
tiles = math.ceil(screen_h / background_h) +1
print (tiles)
# scroll end -----------------------------------------------------------

# animation ------------------------------------------------------------
animation_list = []
animation_steps = 8
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0
for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 128, 128, black))
# animation end ---------------------------------------------------------


# obsticles -------------------------------------------------------------
rock_group = pygame.sprite.Group()
# obsticles end ---------------------------------------------------------


# game loop -------------------------------------------------------------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    clock.tick(FPS)
    
    if start_button_interact.draw(screen) == True:
        animation_plays = True

    if animation_plays:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0
        
        for i in range (-1, tiles):
            screen.blit(background, (0,i * background_h + scroll))

        scroll = scroll + 5

        if scroll >= background_h:
            scroll = 0

        screen.blit(animation_list[frame], (476, 592))

    pygame.display.update()


pygame.quit()