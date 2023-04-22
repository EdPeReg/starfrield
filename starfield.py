#!/usr/bin/env python3

# TODO: Make that more stars appear in the screen, don't increment the amount of stars
# for that dont map_range the stars, use te oriinal (x,y) values, more stars will appear
# but it won't move because it won't have the new position (I guess)

# TODO: Control de speed using the mouse or keys
# TODO: Check why the pz

import arcade

from Star import Star

def map_range(value: float, min_val: float, max_val: 
              float, min_targ: float, max_targ: float) -> float:
    """
    Re-maps a number from one range to another, for more information check
    https://p5js.org/reference/#/p5/map
    https://rosettacode.org/wiki/Map_range
    https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another

    Parameters
    ----------
        value : float
            Value to be converted
        min_val : float
            lower bound of the value's current range
        max_val : float
            upper bound of the value's current range
        min_tar : float
            lower bound of value's target
        max_tar : float
            upper bound of the value's target
    Returns
    -------
        Remapped number
    """
    return min_targ + (((value - min_val) * (max_targ - min_targ)) / (max_val - min_val))

class Program(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        self.stars = []
        self.TOTAL_STARS = 800
        self.WIDTH = width
        self.HEIGHT = height

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.stars = [Star(self.WIDTH, self.HEIGHT) for _ in range(self.TOTAL_STARS)]

    # def on_key_press(self, key, modifiers):
    #     """Called whenever a key is pressed """
    #     for star in self.stars:
    #         if key == arcade.key.LEFT:
    #             print("inside left")
    #             star.speed -= 1
    #         if key == arcade.key.RIGHT:
    #             print("inside right")
    #             star.speed += 1

    def on_draw(self):
        """Called once per frame to render everything"""

        arcade.start_render()

        for star in self.stars:
            # We don't want to divide by zero, there is a point where z reach 0
            star.reset_values(self.width, self.height)

            # The value is divided by z and map into a new value from 0 to the edge, given
            # a new position
            starx = map_range(star.x / star.z, 0, 1, 0, self.WIDTH)
            stary = map_range(star.y / star.z, 0, 1, 0, self.HEIGHT)

            # Make the star bigger with is closer and smaller with it's away
            # We use z because z controls the speed, so we are interested in that
            # this fix the illusion when the stars pop up
            width_height = map_range(star.z, 0, self.width, 10, 0)

            # To start the stars from the center, I need to apply a transform translation
            # if I don't start from the center, it will star from the bottom left corner (0,0)?
            # that is why I am doing the little formula for (x,y) position for drawing the ellipse
            # for more information: https://www.geeksforgeeks.org/translation-of-objects-in-computer-graphics/
            arcade.draw_ellipse_filled(starx + (self.width / 2), stary + (self.height / 2),
                                       width_height, width_height, arcade.color.WHITE)

            px = map_range(star.x / star.pz, 0, 1, 0, self.width)
            py = map_range(star.y / star.pz, 0, 1, 0, self.height)

            star.pz = star.z

            # When we decrement the stars move
            star.z -= star.speed

            arcade.draw_line(px + (self.width / 2), py + (self.height / 2), 
                             starx + (self.width / 2), stary + (self.height / 2), arcade.color.WHITE)

        arcade.finish_render()

if __name__ == '__main__':
    program = Program(800, 600, "STARFIELD")
    program.setup()
    program.run()
