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

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up the game and initialize the variables """
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
            star.draw(self.width, self.height, self.speed_change)

        arcade.finish_render()
if __name__ == '__main__':
    program = Program(800, 600, "STARFIELD")
    program.setup()
    program.run()
