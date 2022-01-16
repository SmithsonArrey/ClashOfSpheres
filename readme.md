### CLASH OF SPHERES
----------------
## Strategy Game created in pygame

a diamond network of towers are being fought over by two opposing armies. securing a subdiamond network of towers will form a portal that will allow reinforcements to come through. Reinforcements will spawn at each tower contributing to a portal. Towers contributing to more than one Portal will recieve bonus reinforcements. However. The Home node is necessary for any reinforcements to be produced at all.

----------------
## Installation Guide
1. Use the executable file and follow directions

----------------
## Outline of functions

StartGame - launched by executable
Attack - selects attack mode based on relative strength 
EvenAttack - evenly divides forces to assault adjacent enemy tiles -started by Attack function
Occupy - Sends 50% of forces to claim adjacent empty tiles
Reinforce - sends 25% to buff adjacent tile
EndGame - process end code and reset

## Outline of Classes
zone - Control Points connected in a diamond pattern
zone_universe - Game world

--
## To - do
squares - zones
* automatically place zones evenly spaced on the screen
dotted_lines - paths between zones
* algorithm will draw a line between each zone. DFS. if line was drawn before don't redraw.
UI - troop movement, distance counter
spinning hexagon - reps portals, gap between zones and paths


