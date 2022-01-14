import numpy as np

class zone:
    def __init__(self, location, troops, team, adj_z):
        self.location = location #0
        self.troops = troops #1
        self.team = team #neutral
        self.adj_z = adj_z #1 2 3

class zone_universe:
    def __init__(self, locations, pattern, teams):
        self.locations = locations
        self.pattern = pattern
        self.teams = teams

#build team, enter team name, everything else default
#build neutral, filler

    def build_zones(self):
        if self.pattern == "diamond" and self.teams == 2:
            self.zones = [zone(0, 50, "Northern Alliance", [1,2]),
            zone(1, 1, "Neutral", [0,4,3]),
            zone(2, 1, "Neutral", [0,4,5]),
            zone(3, 1, "Neutral", [1,6,7]),
            zone(4, 1, "Neutral", [1,2,7,8]),
            zone(5, 1, "Neutral", [2,8,9]),
            zone(6, 1, "Neutral", [3,10]),
            zone(7, 1, "Neutral", [3,4,10,11]),
            zone(8, 1, "Neutral", [4,5,11,12]),
            zone(9, 1, "Neutral", [5,12]),
            zone(10, 1, "Neutral", [6,7,13]),
            zone(11, 1, "Neutral", [7,13,8,14]),
            zone(12, 1, "Neutral", [8,14,9]),
            zone(13, 1, "Neutral", [10,11,15]),
            zone(14, 1, "Neutral", [11,12,15]),
            zone(15, 50, "Southern Empire", [13,14])    
            ]

universe = zone_universe(9,"diamond",2)     
universe.build_zones()
   