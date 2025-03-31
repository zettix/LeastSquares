# LeastSquares

Find the best fitting line to pairs of input data`(x,y)`.   The PDF paper, linked below, should be
gentle enough to understand the mathematics behind the least squares line fitting algorithm.

![build status](https://github.com/zettix/LeastSquares/actions/workflows/python-app.yml/badge.svg)

## Python Render Example
![example_plot](https://github.com/zettix/LeastSquares/blob/main/plot.png)

## HTML Example

This is based on a [W3 Schools Canvas](https://www.w3schools.com/js/tryit.asp?filename=tryai_canvas_combined) interactive tutorial,
but the line didn't fit the least-squares model, so I modified the html/javascript to produce the correct result.

![example_plot](https://github.com/zettix/LeastSquares/blob/main/canvas-plot.gif)

See the [pdf](https://github.com/zettix/LeastSquares/blob/main/tex/line-fit.pdf) for the very short python code required to implement
this algorithm, or look at `LeastSquaresLine.py`.   The file
`least-plot.py` simply plots the example data to produce the above image.

To create the pdf:
```
pdflatex line-fit.tex
```
