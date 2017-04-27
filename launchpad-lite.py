import pygame

pygame.init()

white = 255,255,255
black = 0,0,0
green = 0,255,0

scale = 6
size = screen_width, screen_height = 160 * scale, 120 * scale
background = pygame.image.load("bg_raw.png")
background = pygame.transform.scale(background, (160 * scale, 120 * scale))

screen = pygame.display.set_mode(size)


# ----- Miscellaneous -----
done = False


# ===== ===== Main Program Loop ===== =====
