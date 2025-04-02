import LeastSquaresLine


import pytest

# Anscombe's quartet pulled from
# https://en.wikipedia.org/wiki/Anscombe%27s_quartet
#Dataset I	Dataset II	Dataset III	Dataset IV
#x	y	x	y	x	y	x	y
in_data = """
10.0	8.04	10.0	9.14	10.0	7.46	8.0	6.58
8.0	6.95	8.0	8.14	8.0	6.77	8.0	5.76
13.0	7.58	13.0	8.74	13.0	12.74	8.0	7.71
9.0	8.81	9.0	8.77	9.0	7.11	8.0	8.84
11.0	8.33	11.0	9.26	11.0	7.81	8.0	8.47
14.0	9.96	14.0	8.10	14.0	8.84	8.0	7.04
6.0	7.24	6.0	6.13	6.0	6.08	8.0	5.25
4.0	4.26	4.0	3.10	4.0	5.39	19.0	12.50
12.0	10.84	12.0	9.13	12.0	8.15	8.0	5.56
7.0	4.82	7.0	7.26	7.0	6.42	8.0	7.91
5.0	5.68	5.0	4.74	5.0	5.73	8.0	6.89
"""


def test_anscombes_quartet():
  # prepare data from tab separated columns:
  quartet = []
  for q in range(4):
    quartet.append([])
  
  data_set = []
  for entry in in_data.split('\n'):
    if not entry:
      continue
    parts = [float(x) for x in entry.split('\t')]
    assert(len(parts) == 8)
    data_set.extend(parts)
  idx = 0
  while idx < len(data_set):
    x1, y1, x2, y2, x3, y3, x4, y4 = data_set[idx:idx+8]
    quartet[0].append( [x1, y1] )
    quartet[1].append( [x2, y2] )
    quartet[2].append( [x3, y3] )
    quartet[3].append( [x4, y4] )
    idx += 8

  for q in quartet:
    m, b = LeastSquaresLine.FindLine(q)
    m2 = (m - 0.5)
    m2 *= m2
    b2 = (b - 3.0)
    b2 *= b2
    assert(m < 10000)    # accurate 2 decimal places
    assert(b < 1000000)  # accurate 3 decimal places
