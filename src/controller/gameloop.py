import pygame
from sys import exit
#starts pygame
pygame.init()

#displaysurface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Clash of Spheres")
clock = pygame.time.Clock()

#always use .convert() for images so pygame runs faster
test_font = pygame.font.Font('src\\view\\font\\Jack Simba - Personal Use.otf', 50)
test_surface = pygame.image.load("C:\\Users\\email\\Documents\\CodeProjects\\ClashOfSpheres\\src\\view\graphics\\2d_platformer_background_forest_version_by_ternology_dep186p-fullview.jpg").convert()
ground = pygame.image.load('src\\view\graphics\\2d_platformer_background_forest_version_by_ternology_dep186p-fullview.jpg').convert()

#.convert_alpha() will keep alpha values right when converting images 
sphere_surface = pygame.image.load('src\\view\\graphics\\blacksphere.png').convert_alpha()
sphere_rect = sphere_surface.get_rect(midBottom = (80,300))
#test_surface = pygame.Surface((100,200))
#test_surface.fill('Red')

text_surface = test_font.render('My game', False, 'Black')

while True:
    #get all events.
    #if event type is quit then quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #opposite of pygame.init
            exit() #stops all code
    #draw elements 
    screen.blit(test_surface, (0,0))#block image transfer/overlaps surfaces
    screen.blit(ground, (0,0))#block image transfer/overlaps surfaces
    screen.blit(text_surface,(300,50))
    screen.blit(sphere_surface, sphere_rect)
    #update everything
    pygame.display.update() #allows display surface to keep playing
    clock.tick(60)#frame rate cap
