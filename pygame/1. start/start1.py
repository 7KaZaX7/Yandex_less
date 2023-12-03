import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 360))  # flags=pygame.NOFRAME
pygame.display.set_caption("My Games")

icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)

background = pygame.image.load("img/background.jpg")

background_sound = pygame.mixer.Sound("sounds/default_sound.mp3")

walk_right = [pygame.image.load("img/hero_walk/1.png"),
              pygame.image.load("img/hero_walk/2.png"),
              pygame.image.load("img/hero_walk/3.png"),
              pygame.image.load("img/hero_walk/4.png")]

walk_left = [pygame.image.load("img/hero_walk/8.png"),
             pygame.image.load("img/hero_walk/7.png"),
             pygame.image.load("img/hero_walk/6.png"),
             pygame.image.load("img/hero_walk/5.png")]

player_anim_count = 0

player_speed = 7
player_x = 20
player_y = 216

is_jump = False
jump_count = 6

background_x = 0

background_sound.play()

while True:

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + 600, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_RIGHT] and player_x < 250:
        player_x += player_speed
    elif keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -6:
            if jump_count < 0:
                player_y += (jump_count ** 2) / 2
            else:
                player_y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 6

    background_x -= 4
    if background_x < -600:
        background_x = 0

    if player_anim_count >= 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(8)
