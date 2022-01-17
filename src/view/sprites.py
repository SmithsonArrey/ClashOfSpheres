import pygame
class blob_sprite(pygame.sprite.Sprite):
    def __init__(self, zone, attack_path, team):
        super().__init__
        self.spawn_zone = zone
        self.team = team
        self.image = None
        self.animation_set = None
        self.sprite_group = None
        self.unitcount = None
        #currentlocationx = 0?

#movement logic

    def update():
        super().update
        # blob size increases with unit count
        # appears from one zone disappears into the next
        # draw unit counts

class portal_sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__
        self.image = None
        self.animation_set = None

    def update():
        super().update

#    def destroy(self):
#		if self.rect.x <= -100: 
#			self.kill()


    #portal has 3 states
    #Team 1
    #Team 2
    #Neutral

    #therefore it could swap between 3 sprites/animation sets
