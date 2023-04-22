#!/usr/bin/env python3

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
        self.speed_change = 10
        self.TOTAL_STARS = 200
        self.WIDTH = width
        self.HEIGHT = height

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.stars = [Star(self.WIDTH, self.HEIGHT) for _ in range(self.TOTAL_STARS)]

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed """
        
        # TODO: Increase/decrease the speed when you left the key pushed
        # Update the speed when left and right are pressed, 
        if key == arcade.key.LEFT:
            # Decrease speed to the left
            self.speed_change -= 10
        elif key == arcade.key.RIGHT:
            # Increase speed to the right
            self.speed_change += 10

    def on_draw(self):
        """Called once per frame to render everything"""

        arcade.start_render()

        for star in self.stars:
            # We don't want to divide by zero, there is a point where depth reach 0
            star.reset_values(self.width, self.height)

            # The value is divided by z and map into a new value from 0 to the edge, given
            # a new position according to the depth 
            starx = map_range(star.x / star.depth, 0, 1, 0, self.WIDTH)
            stary = map_range(star.y / star.depth, 0, 1, 0, self.HEIGHT)

            # Make the star bigger with is closer and smaller with it's away
            # We use z because z controls the speed, so we are interested in that
            # this fix the illusion when the stars pop up
            width_height = map_range(star.depth, 0, self.width, 10, 0)

            # To start the stars from the center, I need to apply a transform translation
            # if I don't start from the center, it will star from the bottom left corner (0,0)?
            # that is why I am doing the little formula for (x,y) position for drawing the ellipse
            # for more information: https://www.geeksforgeeks.org/translation-of-objects-in-computer-graphics/
            arcade.draw_ellipse_filled(starx + (self.width / 2), stary + (self.height / 2),
                                       width_height, width_height, arcade.color.WHITE)


            # arcade.draw_ellipse_filled(star.x + (self.width / 2), star.y + (self.height / 2),
            #                            width_height, width_height, arcade.color.WHITE)

            # Map the previous (x,y) to a new value from 0 to width and height of the window 
            prevx = map_range(star.x / star.prevz, 0, 1, 0, self.width)
            prevy = map_range(star.y / star.prevz, 0, 1, 0, self.height)

            # Update the previous depth of the star
            # The new position of the star can be calculated based on its current and previous depth. 
            # This is done so that the star moves smoothly through the star field and so that 
            # the sensation of depth is generated against the background of moving stars.
            star.prevz = star.depth

            # When we decrement the stars move
            star.depth -= star.speed + self.speed_change

            # Draw a line where it was previously to where it is now
            arcade.draw_line(prevx + (self.width / 2), prevy + (self.height / 2), 
                             starx + (self.width / 2), stary + (self.height / 2), arcade.color.WHITE)

        arcade.finish_render()

if __name__ == '__main__':
    program = Program(800, 600, "STARFIELD")
    program.setup()
    program.run()
