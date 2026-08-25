import pygame
import spritesheet
import Buttons
from Buttons import Button

pygame.init()
screen = pygame.display.set_mode((1080, 720))

running = True
animation_plays = False


sprite_sheet_image = pygame.image.load("sprite walk.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
start_button = pygame.image.load("start button.png")

start_button_interact = Button(0, 0, start_button, 1)


black = (0, 0, 0)

animation_list = []
animation_steps = 8
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 128, 128, black))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((87, 132, 191))

    if start_button_interact.draw(screen) == True:
        animation_plays = True

    if animation_plays:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0

    screen.blit(animation_list[frame], (476, 592))

    pygame.display.update()


pygame.quit()