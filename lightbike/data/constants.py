"""
The constants module holds global variables for the lightbike game
"""
from arcade import color
from arcade import key
from arcade import Sound

SCREEN_TITLE = "Lightbike"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING = 1
AI_SPRITE = "assets/orange_player.png"
AI_WALL_SPRITE = "assets/orange_wall.png"
PLAYER_SPRITE = "assets/blue_player.png"
PLAYER_WALL_SPRITE = "assets/blue_wall.png"

MOVEMENT_SPEED = 100
DEFAULT_KEYS = {
    key.A: (-1, 0), # a
    key.D: (1, 0),  # d
    key.W: (0, 1),  # w
    key.S: (0, -1)  # s
}

NUM_PLAYERS = 1
NUM_AI = 1

AI_RANGE = 5
AI_BLINDSPOT_RANGE = 3
AI_TURN_COOLDOWN = 0.5

SOUND_BACKGROUND = Sound("assets/Sci-Fi-Dramatic-Theme.wav")
SOUND_COLLISION = Sound("assets/mi_explosion_03_hpx.wav")

# --- Explosion Particles Related

# How fast the particle will accelerate down. Make 0 if not desired
PARTICLE_GRAVITY = 0.05

# How fast to fade the particle
PARTICLE_FADE_RATE = 8

# How fast the particle moves. Range is from 2.5 <--> 5 with 2.5 and 2.5 set.
PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5

# How many particles per explosion
PARTICLE_COUNT = 20

# How big the particle
PARTICLE_RADIUS = 3

# Possible particle colors
PARTICLE_COLORS = [color.ALIZARIN_CRIMSON,
                   color.COQUELICOT,
                   color.LAVA,
                   color.KU_CRIMSON,
                   color.DARK_TANGERINE]

# Chance we'll flip the texture to white and make it 'sparkle'
PARTICLE_SPARKLE_CHANCE = 0.02

# --- Smoke
# Note: Adding smoke trails makes for a lot of sprites and can slow things
# down. If you want a lot, it will be necessary to move processing to GPU
# using transform feedback. If to slow, just get rid of smoke.

# Start scale of smoke, and how fast is scales up
SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03

# Rate smoke fades, and rises
SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5

# Chance we leave smoke trail
SMOKE_CHANCE = 0.25

BACKGROUND_COLOR = color.BLACK

__corner = "assets/wall_3.png"
__parallel = "assets/wall_4.png"
__one = "assets/wall_5.png"
__three = "assets/wall_2.png"
__wall = "assets/wall_6.png"

DEFAULT_WALL = "assets/wall_1.png"
MAPX = 20
MAPY = 15



# Default map
MAP0 = [

]

MAP1 = [
    [(4, 3), __three, 270],
    [(4, 4), __parallel, 90],
    [(4, 5), __parallel, 90],
    [(4, 6), __parallel, 90],
    [(4, 7), __parallel, 90],
    [(4, 8), __parallel, 90],
    [(4, 9), __parallel, 90],
    [(4, 10), __parallel, 90],
    [(4, 11), __three, 90],
    [(15, 3), __three, 270],
    [(15, 4), __parallel, 90],
    [(15, 4), __parallel, 90],
    [(15, 5), __parallel, 90],
    [(15, 6), __parallel, 90],
    [(15, 7), __parallel, 90],
    [(15, 8), __parallel, 90],
    [(15, 9), __parallel, 90],
    [(15, 10), __parallel, 90],
    [(15, 11), __three, 90],
]

# MAP2
MAP2 = [
    [(4, 3), __corner, 180], # Bottom Left Square
    [(4, 4), __one, 90],
    [(4, 5), __corner, 90],
    [(5, 3), __one, 180],
    [(5, 4), __wall, 90],
    [(5, 5), __one, 0],
    [(6, 3), __corner, 270],
    [(6, 4), __one, 270],
    [(6, 5), __corner, 0],
    [(4, 9), __corner, 180], # Top Left Square
    [(4, 10), __one, 90],
    [(4, 11), __corner, 90],
    [(5, 9), __one, 180],
    [(5, 10), __wall, 90],
    [(5, 11), __one, 0],
    [(6, 9), __corner, 270],
    [(6, 10), __one, 270],
    [(6, 11), __corner, 0],
    [(14, 3), __corner, 180], # Bottom Right Square
    [(14, 4), __one, 90],
    [(14, 5), __corner, 90],
    [(15, 3), __one, 180],
    [(15, 4), __wall, 90],
    [(15, 5), __one, 0],
    [(16, 3), __corner, 270],
    [(16, 4), __one, 270],
    [(16, 5), __corner, 0],
    [(14, 9), __corner, 180], # Top Right Square
    [(14, 10), __one, 90],
    [(14, 11), __corner, 90],
    [(15, 9), __one, 180],
    [(15, 10), __wall, 90],
    [(15, 11), __one, 0],
    [(16, 9), __corner, 270],
    [(16, 10), __one, 270],
    [(16, 11), __corner, 0],

]
# MAP3
MAP3 = [
    [(2, 2), __corner, 180], # Bottom Left Square
    [(2, 3), __one, 90],
    [(2, 4), __corner, 90],
    [(3, 2), __one, 180],
    [(3, 3), __wall, 90],
    [(3, 4), __one, 0],
    [(4, 2), __corner, 270],
    [(4, 3), __one, 270],
    [(4, 4), __corner, 0],
    [(2, 10), __corner, 180], # Top Left Square
    [(2, 11), __one, 90],
    [(2, 12), __corner, 90],
    [(3, 10), __one, 180],
    [(3, 11), __wall, 90],
    [(3, 12), __one, 0],
    [(4, 10), __corner, 270],
    [(4, 11), __one, 270],
    [(4, 12), __corner, 0],
    [(15, 2), __corner, 180], # Bottom Right Square
    [(15, 3), __one, 90],
    [(15, 4), __corner, 90],
    [(16, 2), __one, 180],
    [(16, 3), __wall, 90],
    [(16, 4), __one, 0],
    [(17, 2), __corner, 270],
    [(17, 3), __one, 270],
    [(17, 4), __corner, 0],
    [(15, 10), __corner, 180], # Top Right Square
    [(15, 11), __one, 90],
    [(15, 12), __corner, 90],
    [(16, 10), __one, 180],
    [(16, 11), __wall, 90],
    [(16, 12), __one, 0],
    [(17, 10), __corner, 270],
    [(17, 11), __one, 270],
    [(17, 12), __corner, 0],
    [(6, 7), __three, 180], # Left Cross Arm
    [(7, 7), __parallel, 0],
    [(8, 7), __parallel, 0],
    [(9, 7), __wall, 180], # Center Cross
    [(10, 7), __wall, 180],
    [(11, 7), __parallel, 0], # Right Cross Arm
    [(12, 7), __parallel, 0], 
    [(13, 7), __three, 0],
    [(9, 8), __one, 90], #Left Side of Top Cross Arm
    [(9, 9), __corner, 90],
    [(10, 8), __one, 270], #Right Side of Top Cross Arm
    [(10, 9), __corner, 0],
    [(9, 6), __one, 90], #Left Side of Bottom Cross Arm
    [(9, 5), __corner, 180],
    [(10, 6), __one, 270], #Right Side of Bottom Cross Arm
    [(10, 5), __corner, 270],    
]