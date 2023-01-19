import math

# Game settings
RESOLUTION = WIDTH, HEIGHT = 1280, 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60

PLAYER_POS = 1.5, 5         # POSIÇÃO NO MINIMAPA
PLAYER_ANGLE = 0            # ANGULO DO PAYER
PLAYER_SPEED = 0.004        # VELOCIDADE DO PLAYER
PLAYER_ROT_SPEED = 0.002    # VELOCIDADE DE ROTAÇÃO

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DISTANCE = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
