#!/usr/bin/env python
import random

# TODO: When self.z = width you can see more stars but they don't increment the speed
# TODO: Analize why pz

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
        # negative values
        self.x = random.randint(-width, width)
        self.y = random.randint(-height, height)
        self.speed = 20

        # This z value is use to disperse the stars, each star will have
        # a different value
        self.z = random.randint(0, width)
        self.pz = self.z
    
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

        if self.z < 1:
            self.z = width
            self.x = random.randint(-width, width)
            self.y = random.randint(-height, height)
            self.pz = self.z
