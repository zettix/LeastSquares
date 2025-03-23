#!/usr/bin/python3

import math

with open('test1.txt', 'w') as f:
  for x in range(-400, 400, 25):
   theta = math.pi * float(x) / 1000.0
   y = math.sin(theta + math.pi / 3.0) * 200.0
   f.write(f"{x} {y}\n")
