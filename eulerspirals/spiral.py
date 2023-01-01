#!/usr/bin/env python

import math
import pickle

class Spiral:
  def __init__(self, da):
    self.da = da

  def __str__(self):
    return f"Spiral: da = ${self.da}"


  def calculate(self, steps): 
    self.steps = steps

    points = [(0, 0)]
    x_coords = [0]
    y_coords = [0]
    angle = 0

    for step in range(0, self.steps):

      angle = angle + step*self.da

      x = points[-1][0] + math.cos(math.radians(angle))
      y = points[-1][1] + math.sin(math.radians(angle))
      x_coords.append(x)
      y_coords.append(y)
      points.append((x, y))

    self.points = points
    self.x = x_coords
    self.y = y_coords

  def save(self, path = "."):

    if hasattr(self, 'steps'): 
      steps = self.steps
    else: 
      steps = 0

    pickle_out = open(f"{path}/eulerspiral-{self.da}-{steps}.pickle","wb")
    pickle.dump(self, pickle_out)
    pickle_out.close()


if __name__ == "__main__": 

  spiral = Spiral(1)
  spiral.calculate(1000)
  print(spiral.points)
