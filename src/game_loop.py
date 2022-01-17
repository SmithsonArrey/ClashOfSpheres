import pygame
import cos_lib
from sys import exit
#starts pygame
pygame.init()

universe = cos_lib.zone_universe.zone_universe(9,"diamond",2)     
universe.build_zones()
map = cos_lib.universe_map.map()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Clash of Spheres")
clock = pygame.time.Clock()

background = pygame.image.load(map.background).convert()

sphere_surface = pygame.image.load('src\\view\\graphics\\blacksphere.png').convert_alpha()
sphere_rect = sphere_surface.get_rect(midbottom = (80,300))

def draw_static_elements():
    screen.blit(background, (0,0))

#not finished
def draw_UI():
    screen.blit(sphere_surface, sphere_rect)

player_blobs = pygame.sprite.Group()

def draw_sprite_groups():
    player_blobs.draw(screen)
    player_blobs.update()


#init player action object here?



while True:
    player_input_active = False
    player_input_event = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        #look for touch/mouse events
            #player_input_active = True  
            #trigger playerinput script

    if player_input_active:
        #placeholder
        #read player intent
        if player_input_event[0] == "select" and player_input_event[1] == "attack":
            player_blobs.add(cos_lib.game_rules.input_response("attack", player_input_event[2], player_input_event[3]))    
    
        draw_static_elements()
        draw_sprite_groups()
        draw_UI()
    else:
        draw_static_elements()
        draw_sprite_groups()
        draw_UI()
    

    pygame.display.update() 
    clock.tick(60)
