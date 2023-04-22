#!/usr/bin/env python
import random
import arcade

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

def translation(x: float, y: float, width: int, height: int) -> tuple[float, float]:
    """
    Translate the position to the center of the window

    Parameters
    ----------
        x : float
            x axis to translate
        y : float
            y axis to translate
        width : int
            width of the window
        height : int
            height of the window
    """
    return x + (width / 2), y + (height / 2)

class Star:
    """
    This class represent a start that will be draw on the screen
    """
    def __init__(self, width: int, height: int):
        """
        Initialize a start with basic information

        Parameters
        ----------
            width : int
                Width of the start
            height : int
                Height of the start
        """

        # The reason why we use -width and -height it is because the translation
        # if we start from 0, it will start from the center, so no stars will be drawn
        # beyond the center, we want the stars all over the place, for that we give
        # negative values. In this manner there is a random distribution and we get a better
        # visual effect in the stars
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.speed = 20

        # This depth value is use to disperse the stars, each star will have
        # a different value, so it works like in a 3D space, where the stars that
        # are far away have bigger depth value and stars that are closer have smaller depth value
        # The depth is used to controll the speed and star size
        self.depth = random.randint(0, width)
        self.prevz = self.depth

    def reset_values(self, width: int, height: int):
        """
        Reset star values in case there is a division by zero because "z" value
        This will make the stars to pop up, but it will fix when the stars come back

        Parameters
        ----------
            width : int
                Width of the start
            height : int
                Height of the start
        """

        if self.depth < 1:
            self.depth = width
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.prevz = self.depth
    
    def draw(self, width: int, height: int, speed_change: int):
        """
        Draw each star in the screen

        Parameters
        ----------
            width : int
                Width of window
            height : int
                Height of window
            speed_change : int
                Amount of value that change the star speed 
        """

        # We don't want to divide by zero, there is a point where depth reach 0
        self.reset_values(width, height)

        # The value is divided by z and map into a new value from 0 to the edge, given
        # a new position according to the depth
        screen_x = map_range(self.x / self.depth, 0, 1, 0, width)
        screen_y = map_range(self.y / self.depth, 0, 1, 0, height)

        # Make the star bigger when is closer and smaller with it's away
        # We use z because z controls the speed, so we are interested in that
        # this fix the illusion when the stars pop up
        width_height = map_range(self.depth, 0, width, 10, 0)

        screen_x, screen_y = translation(screen_x, screen_y, width, height)

        # To start the stars from the center, I need to apply a transform translation
        # if I don't start from the center, it will star from the bottom left corner (0,0)?
        # that is why I am doing the little formula for (x,y) position for drawing the ellipse
        # for more information: https://www.geeksforgeeks.org/translation-of-objects-in-computer-graphics/
        arcade.draw_ellipse_filled(screen_x, screen_y, width_height,
                                   width_height, arcade.color.WHITE)

        # Map the previous (x,y) to a new value from 0 to width and height of the window
        prevx = map_range(self.x / self.prevz, 0, 1, 0, width)
        prevy = map_range(self.y / self.prevz, 0, 1, 0, height)

        # Update the previous depth of the star
        # The new position of the star can be calculated based on its current and previous depth. 
        # This is done so that the star moves smoothly through the star field and so that
        # the sensation of depth is generated against the background of moving stars.
        self.prevz = self.depth

        # we have some negative speed, stop the stars
        if speed_change < 1:
            self.speed = 0
            speed_change = 0

        # When we decrement the star, it will move
        self.depth -= self.speed + speed_change
        prevx, prevy = translation(prevx, prevy, width, height)

        # Draw a line where it was previously to where it is now
        arcade.draw_line(prevx, prevy, screen_x, screen_y, arcade.color.WHITE)
