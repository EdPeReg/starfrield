#!/usr/bin/env python3

import arcade

from Star import Star

class Program(arcade.Window):
    """Main program"""
    def __init__(self, width: int, height: int, title: str):
        self.stars = []
        self.speed_change = 10
        self.TOTAL_STARS = 200
        self.WIDTH = width
        self.HEIGHT = height
        self.is_key_left = False
        self.is_key_right = False

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables """

        self.stars = [Star(self.WIDTH, self.HEIGHT) for _ in range(self.TOTAL_STARS)]

    def on_update(self, delta_time):
        """ Update objects and game logic """

        if self.is_key_right:
            # Increase speed to the right
            self.speed_change += 10 * delta_time
        elif self.is_key_left:
            # Decrease speed to the left
            self.speed_change -= 10 * delta_time

            # Negative speed, we want to stop
            if self.speed_change < 1:
                self.speed_change = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed """

        if key == arcade.key.LEFT:
            self.is_key_left = True
        elif key == arcade.key.RIGHT:
            self.is_key_right = True
    
    def on_key_release(self, key, modifiers):
        """ Called whenever a key is released """

        if key == arcade.key.LEFT:
            self.is_key_left = False
        elif key == arcade.key.RIGHT:
            self.is_key_right = False

    def on_draw(self):
        """Called once per frame to render everything"""

        arcade.start_render()

        for star in self.stars:
            star.draw(self.width, self.height, self.speed_change)

        arcade.finish_render()
if __name__ == '__main__':
    program = Program(800, 600, "STARFIELD")
    program.setup()
    program.run()
