# /usr/bin/env python3

# Created by: Marwan Mashaly
# Created on: September 2019
# This programs draws

import ugame
import stage

# an image bank for circuitpython
image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
# a list of sprites that will be updated every frame
sprites = []


def main():
    # this function sets the background

    # sets the background to image 0 in the bank
    # backgrounds do not have magents as a transparent color
    background = stage.Grid(image_bank_1, 10, 8)
    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    alien = stage.Sprite(image_bank_1, 8, 64, 56)
    sprites.append(alien)
    ship = stage.Sprite(image_bank_1, 4, 75, 56)
    sprites.insert(0, ship)  # insert at top of sprite list

    # create a stage for the background to show up on
    #  and set the frame rate to 60
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input

        # update_game_logic

        # redraw sprite list

        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    main()
