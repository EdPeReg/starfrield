# Starfield

This is a simple program that emulates a **STARFIELD**, it is inspire from [Coding Challenge #1: Starfield in Processing](https://www.youtube.com/watch?v=17WoOqgXsRM&t=198s), basically I only transcribed it to python, all credits to him for this wonderful video :) <br>

Basically the stars will move at some speed, creating the ilusion of stars from the center. <br>

![Demostration](https://github.com/EdPeReg/starfrield/blob/main/demostration.gif)

## How to run it

Basically the only dependency that you need is _arcade_, but you can use _requirements.txt_ if you want: <br>

``` pip install -r requiremets.txt ```

Or just install _arcade_ <br>

``` pip install arcade ```

After that just only run: <br>

```python starfield.py```

## Features

- Increment the speed by pressing left arrow key <br>
- Decrement the speed by pressing right arrow key <br>
- Depth or z buffer added, given the sensation of depth <br>

## TODO

This can be enhanced significantly, but for the moment this are the things I would like to do: <br>

- Fixbug where you stop the stars, some stars will disappear <br>
- Make more stars to be draw without incrementing the stars amount from the code <br>
- Add Interstellar theme music <br>

# References

- [Coding Challenge #1: Starfield in Processing](https://www.youtube.com/watch?v=17WoOqgXsRM&t=198s)
- [Basic starfield on C using SDL](https://github.com/djdavies/c_code/blob/master/starfield.c)
- [Z-Buffer or Depth-Buffer method](https://www.geeksforgeeks.org/z-buffer-depth-buffer-method/) 
- [Map reference p5](https://p5js.org/reference/#/p5/map)
- [Map range](https://rosettacode.org/wiki/Map_range)
- [Mapping a range of values to another](https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another)
