import pygame
import spritesheet
import Buttons
from Buttons import Button
import math
import random
import time

pygame.init()
screen_w = (1080)
screen_h = (720)
screen = pygame.display.set_mode((screen_w, screen_h))

running = True
animation_plays = False
clock = pygame.time.Clock()
FPS = 30
scroll_speed = 4
black = (0, 0, 0)
lane = random.randint(0,2)
obsticle_spawn_time = pygame.time.get_ticks()
obsticle_spawning_cooldown = random.randint(500, 1500)
# end of init stuff ------------------------------------------------


# image load -----------------------------------------------------------
sprite_sheet_image = pygame.image.load("sprite walk.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

background = pygame.image.load("racing lanes.png").convert_alpha()

rock_1 = pygame.image.load("stone 1.png").convert_alpha()
rock_2 = pygame.image.load("stone 2.png").convert_alpha()
rock_3 = pygame.image.load("stone 3.png").convert_alpha()

easy_button = pygame.image.load("easy button.png").convert_alpha()
light_easy_button = pygame.image.load("light easy button.png").convert_alpha()

medium_button = pygame.image.load("medium button.png").convert_alpha()
light_start_button = pygame.image.load("light start button.png").convert_alpha()

hard_button = pygame.image.load("hard button.png").convert_alpha()
light_hard_button = pygame.image.load("light hard button.png").convert_alpha()

left_button = pygame.image.load ("left button.png").convert_alpha()
right_button = pygame.image.load ("right button.png").convert_alpha()

light_left_button = pygame.image.load ("light left button.png").convert_alpha()
light_right_button = pygame.image.load ("light right button.png").convert_alpha()

big_left_button = pygame.image.load ("big left button.png").convert_alpha()
big_right_button = pygame.image.load ("big right button.png").convert_alpha()

sign = pygame.image.load("sighn.png").convert_alpha()
sighn_eyes = pygame.image.load("sighn eyes.png").convert_alpha()

epp_shark_card = pygame.image.load ("epp shark card.png").convert_alpha()

background_w = background.get_width()
background_h = background.get_height()

# image load end -------------------------------------------------------

# button interacts -----------------------------------------------------
easy_button_interact = Button(290, 580, easy_button, 1)
medium_button_interact = Button(472, 580, medium_button, 1)
hard_button_interact = Button(654, 580, hard_button, 1)
left_button_interact = Button(80, 360, left_button, 1)
right_button_interact = Button(910, 360, right_button, 1)
# button interacts end -------------------------------------------------


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
obsticles = []
rock_images = [rock_1, rock_2, rock_3]

class Obsticles:
    def __init__(self, lane):
        self.lane = lane
        self.image = random.choice(rock_images)
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.height

        if self.lane == 0:
            self.rect.x = 241
        elif self.lane == 1:
            self.rect.x = 475
        elif self.lane == 2:
            self.rect.x = 700

    def update(self):
        self.rect.y += scroll_speed
        if self.rect.y > screen_h:
            obsticles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def spawn_obsticle():
    rocks_per_lane = [0, 0, 0]
    available_lanes = []

    for lane in range(3):
        can_spawn = True

        for obsticle in obsticles:
            rocks_per_lane[obsticle.lane] += 1
            if obsticle.lane == lane:
                if obsticle.rect.y < 250:
                    can_spawn = False

        if can_spawn:
            available_lanes.append(lane)

    if len(available_lanes) > 0:
        lane = random.choice(available_lanes)
        obsticles.append(Obsticles(lane))

# obsticles end ---------------------------------------------------------


# game loop -------------------------------------------------------------
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)

    screen.fill((87, 132, 191))

    screen.blit(sign, (268, 20))
         
    if left_button_interact.draw(screen) == True:
        screen.blit(big_left_button, (62, 340))

    if right_button_interact.draw(screen) == True:
        screen.blit (big_right_button, (910, 340))

    if easy_button_interact.draw(screen) == True:
        animation_plays = True
        scroll_speed = 2

    if medium_button_interact.draw(screen) == True:
        animation_plays = True
        scroll_speed = 4

    if hard_button_interact.draw(screen) == True:
        animation_plays = True
        scroll_speed = 6

    if animation_plays:
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0
        
        for i in range (-1, tiles):
            screen.blit(background, (0,i * background_h + scroll))

        scroll = scroll + (scroll_speed)

        if scroll >= background_h:
            scroll = 0


        current_time = pygame.time.get_ticks()

        if current_time - obsticle_spawn_time >= obsticle_spawning_cooldown:
            spawn_obsticle()
            obsticle_spawn_time = current_time
            obsticle_spawning_cooldown = random.randint(500, 1500)

##        if len(obsticles) == 0:
##            obsticles.append(Obsticles())

        for obsticle in obsticles:
            obsticle.draw(screen)
            obsticle.update()
        ##  if player.shark_rect.colliderect(obsticle.rect):
        ##      pygame.draw.rect(screen, (255, 0, 0), player.shark_rect, 2)
        screen.blit(animation_list[frame], (476, 592))

##    pygame.draw.rect(screen, (255, 255, 255), easy_button_interact, 2)

    pygame.display.update()


pygame.quit()