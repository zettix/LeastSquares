#!/usr/bin/python3


import random
from PIL import Image, ImageDraw, ImageFont
import math

from LeastSquaresLine import FindLine

class FitLine:
  def __init__(self):
    self.points= []
    # Image dimensions
    self.dx = 800
    self.dy = 500

  def seedXsum0(self):
    """This spefically tests when chi is zero."""
    self.points = []
    count = 60
    start = -10
    off = random.random() * self.dx / count
    while count >= 0:
      x = start * 20 + count * 20
      y = int(math.sin(2.0 + math.pi * count * off / self.dx) * self.dy / -6.0 * random.random() + count * 13)
      self.points.append( (x, y))
      count -=1

  def seedfile(self, filename):
    self.points = []
    with open(filename, 'r') as f:
      for s in f:
        x, y = [float(x) for x in s.strip().split(' ')]
        self.points.append( (x, y))

  def render(self):
    img =  Image.new("RGB", (self.dx, self.dy), 0)
    draw = ImageDraw.Draw(img)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    centerx = self.dx // 2
    centery = self.dy // 2
    # frame and axes
    draw.rectangle( ((0, 0), (self.dx -1, self.dy - 1)), fill=None, outline=yellow, width=1)
    draw.line(((0, centery), (self.dx, centery)), yellow, 1 )
    draw.line(((centerx, 0), (centerx, self.dy)), yellow, 1 )
    # end frame and axes

    boxrad = 2
    for g in self.points:
      j = [x for x in g]
      j[0] += centerx
      j[1] = centery - j[1]
      draw.point(j, (255, 255, 255))
      pm = [x - boxrad for x in j]
      pm.extend([x + boxrad  for x in j])
      pp = tuple(pm)
      
      draw.rectangle( pp, fill=None, outline=yellow, width=1)

    m, b = FindLine(self.points)
    # plot line remapping 0,0 to centerx, centery:
    x0 = 0 
    y0 =  centerx * m - b + centery
    x1 = self.dx
    y1 =  -m * centerx - b + centery
    draw.line(((x0 , y0), (x1, y1)), red, 2)
    info = f"M {m}  B {b}"
    print(info)
    font = ImageFont.truetype("arial.ttf", 15)
    draw.text( (10, 10), info, fill=yellow, font=font)
    img.save("plot.png", "PNG")

if __name__ == "__main__":
  f = FitLine()
  #f.seedXsum0()
  f.seedfile("test1.txt")
  f.render()
