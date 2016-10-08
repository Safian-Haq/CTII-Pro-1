from ConsoleBasedImplementation import *
import pyglet
from pyglet.window import key


# My pyglet functions
#########################################################################################################


def loadSprite(num, pos_x, pos_y):
    """Returns a sprite corresponding to the provided arguments."""
    global im_t2, im_t4, im_t8, im_t16, im_t32, im_t64, im_t128
    global im_t256, im_t512, im_t1024, im_t2048, im_t4096, im_t8192
    if num == 2:
        temp_sp = pyglet.sprite.Sprite(im_t2, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 4:
        temp_sp = pyglet.sprite.Sprite(im_t4, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 8:
        temp_sp = pyglet.sprite.Sprite(im_t8, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 16:
        temp_sp = pyglet.sprite.Sprite(im_t16, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 32:
        temp_sp = pyglet.sprite.Sprite(im_t32, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 64:
        temp_sp = pyglet.sprite.Sprite(im_t64, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 128:
        temp_sp = pyglet.sprite.Sprite(im_t128, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 256:
        temp_sp = pyglet.sprite.Sprite(im_t256, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 512:
        temp_sp = pyglet.sprite.Sprite(im_t512, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 1024:
        temp_sp = pyglet.sprite.Sprite(im_t1024, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 2048:
        temp_sp = pyglet.sprite.Sprite(im_t2048, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 4096:
        temp_sp = pyglet.sprite.Sprite(im_t4096, pos_x, pos_y)
        temp_sp.visible = True
    elif num == 8192:
        temp_sp = pyglet.sprite.Sprite(im_t8192, pos_x, pos_y)
        temp_sp.visible = True
    else:
        return None
    return temp_sp


def deleteSprites():
    """Deletes all sprites in sprite_list."""
    global sprite_list
    for sprite in sprite_list:
        if sprite is None:
            continue
        sprite.delete()
    sprite_list = []


def loadAllsprites():
    """Loads all sprites in sprite_list."""
    global Grid
    global sprite_list
    for i in range(4):
        sprite_list.append(loadSprite(Grid[i], 10 + i * 31 + i * 172, 619))
    for i in range(4, 8):
        sprite_list.append(loadSprite(Grid[i], 10 + (i - 4) * 31 + (i - 4) * 172, 416))
    for i in range(8, 12):
        sprite_list.append(loadSprite(Grid[i], 10 + (i - 8) * 31 + (i - 8) * 172, 212))
    for i in range(12, 16):
        sprite_list.append(loadSprite(Grid[i], 10 + (i - 12) * 31 + (i - 12) * 172, 10))


#########################################################################################################

# Initializing all variables
#########################################################################################################
# Grid that holds the
Grid = [0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0,
        0, 0, 0, 0]

sprite_list = []  # List of Sprites
state = None  # For checking the state of the game
firstRun = False  # For printing initial Grid
Grid = initBoard(Grid)  # Initialize the board

# Instantiate Window
window = pyglet.window.Window(800, 800, resizable=False,
                              caption="2048", vsync=False,
                              config=pyglet.gl.Config(double_buffer=True))

# Image Loading
#########################################################################################################
BOARD = pyglet.resource.image('Resources/Board_Main.png')
im_t2 = pyglet.resource.image('Resources/t2.png')
im_t4 = pyglet.resource.image('Resources/t4.png')
im_t8 = pyglet.resource.image('Resources/t8.png')
im_t16 = pyglet.resource.image('Resources/t16.png')
im_t32 = pyglet.resource.image('Resources/t32.png')
im_t64 = pyglet.resource.image('Resources/t64.png')
im_t128 = pyglet.resource.image('Resources/t128.png')
im_t256 = pyglet.resource.image('Resources/t256.png')
im_t512 = pyglet.resource.image('Resources/t512.png')
im_t1024 = pyglet.resource.image('Resources/t1024.png')
im_t2048 = pyglet.resource.image('Resources/t2048.png')
im_t4096 = pyglet.resource.image('Resources/t4096.png')
im_t8192 = pyglet.resource.image('Resources/t8192.png')
im_lose = pyglet.resource.image('Resources/lose label.png')


#########################################################################################################

# Pyglet functions
#########################################################################################################

@window.event
# Handles key press events
def on_key_press(symbol, modifiers):
    global state, Grid, sprite_list
    deleteSprites()  # Delete's all the sprites in list & empties the list
    # Handles left, right, up & down key presses respectively
    if symbol == key.LEFT:
        Grid = move("l", Grid)
        loadAllsprites()
    elif symbol == key.RIGHT:
        Grid = move("r", Grid)
        loadAllsprites()
    elif symbol == key.UP:
        Grid = move("u", Grid)
        loadAllsprites()
    elif symbol == key.DOWN:
        Grid = move("d", Grid)
        loadAllsprites()
    else:  # If any other key is pressed on keyboard
        loadAllsprites()
        return
    state = checkWin(Grid)
    Grid = addRandtwo(Grid)


@window.event
def on_draw():
    global firstRun, Grid
    window.clear()
    BOARD.blit(0, 0)  # Draws the background board images
    # For ensuring board appears with numbers at the start
    if firstRun is False:
        firstRun = True
        loadAllsprites()
        Grid = addRandtwo(Grid)
    # Traverse over the sprite_list & draw each sprite in list
    for sprite in sprite_list:
        if sprite is None:
            continue
        sprite.draw()
    # Draw logo if no moves are left
    if state == "lose":
        sprite_lose = pyglet.sprite.Sprite(im_lose)
        sprite_lose.draw()


def update(dt):
    window.clear()


pyglet.app.run()
