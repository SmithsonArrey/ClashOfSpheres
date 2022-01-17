#this script will process the input events from the player to determine the player's intentions

#hovering over zone

#mouse_pos = pygame.mouse.get_pos()
#for zone in universe.zones:
#   if zone.rect.collidepoint(mouse_pos):
    #triggerhover(zone)

#attack command

#selcting a zone

# return player intent

class player_action():
    def __init__(self, context, input_event):
        self.context = context
        self.input_event = input_event
        self.intent = None

    def return_intent(self): return self.intent