#!/usr/bin/python3

def FindLine(points=[]):
    """points is a 2-D array
        [[x, y], [x, y], ...]"""
    chi = 0.0
    omega = 0.0
    nu = 0.0
    phi = 0.0

    n = len(points)
    for x, y in points:
      chi += x
      omega += x * x
      nu += y
      phi += x * y

    if chi == 0.0:  # special case.
      m = phi / omega
      b = nu / n
      return (m, b)

    d = n * omega - chi * chi
    if d == 0.0:
      raise Exception("Bad data!")
    m = (chi + phi * n - nu * chi) / d
    b = (phi - m * omega) / chi
    return (m, b)
