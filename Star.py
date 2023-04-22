#!/usr/bin/env python
import random

class Star:
    """
    This class represent a start with some given attributes
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
