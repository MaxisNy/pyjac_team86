SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1800
SEA_LEVEL = SCREEN_HEIGHT - 75

BACKGROUND_IMG = "./sprites/bg2.png"
ENEMY_SHIP_IMG = "./sprites/enemy_ship.png"
PLAYER_SHIP_IMG = "./sprites/new_flatship.png"
PLAYER_SHIP_BG_IMG = "./sprites/ship_background.png"
HEART_IMG = "./sprites/heart.png"

# projectiles
NUM_OF_PROJECTILES = 30
PROJECTILE_ACCELERATION = 50
PROJECTILE_ANGLE = 70
INITIAL_PROJECTILE_HEIGHT = 550
PROJECTILE_IMG = "./sprites/projectile.png"
EXPLOSION_IMG = "./sprites/explosion.png"

# player
PLAYER_BLOCK_DOWN_SPEED = 4
PLAYER_BLOCK_UP_SPEED = 1
PLAYER_JUMP_SPEED = 450
PLAYER_ACCELERATION = 600
PLAYER_INITIAL_COORDINATES = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.6)
PLAYER_IMG = "./sprites/player_left.png"
PLAYER_BLOCK_IMG = "./sprites/player_block.png"
PLAYER_JUMP_IMG = "./sprites/player_jump.png"

intro_text1 = "Yo ho ho! Ahoy heartie! " \
              "The scallywags are trying " \
              "t' scuttle the wit' thar chase guns. " \
              "Protect the ship as long as ye can, arr."
intro_text2 = "How to play:"
intro_text3 = "Press the [W] key to jump"
intro_text4 = "Press the [A] key to move left and [D] to move right."
intro_text5 = "Press the [Shift] key to use your shield."
intro_text6 = "Block the cannons using your shield, good luck!"
intro_text8 = "Press E for Easy, N for Normal, and H for Hard"
intro_texts = [intro_text1, intro_text2, intro_text3,
               intro_text4, intro_text5, intro_text6, intro_text8]
win_screen_text1 = "You win!"
win_screen_text2 = "Captain LackBeard of The Booty Hauler requests your " \
                   "humble presence at the bottom of the ocean."
win_screen_text3 = "RSVP not required. Guests will have to pose " \
                   "on the plank for pictures."
win_screen_text4 = "Sharks may escort you in the downward travel."
win_screen_text5 = "Press [ESC] to quit!"
win_screen_text6 = "Press any other key to restart!"
win_texts = [win_screen_text1, win_screen_text2, win_screen_text3,
             win_screen_text4, win_screen_text5, win_screen_text6]
lose_screen_text1 = "You lost."
lose_screen_text2 = "Captain LackBeard of the Booty Hauler " \
                    "sank to the bottom of the ocean."
lose_screen_text3 = "Press [ESC] to give up and quit."
lose_screen_text4 = "Press any other key to restart!"
lose_texts = [lose_screen_text1, lose_screen_text2, lose_screen_text3,
              lose_screen_text4]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (100, 100, 100)
ORANGE = (255, 165, 0)
GREEN = (0, 128, 0)
RED = (100, 0, 0)
BLUE = (30, 144, 255)
DARK_BLUE = (0, 0, 205)
PURPLE = (102, 0, 204)
YELLOW = (255, 255, 0)
