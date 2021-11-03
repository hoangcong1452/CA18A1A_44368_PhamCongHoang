"""
Author: pham cong hoang
Date: 18/10/2021

Problem: Why does the blur function need to work with a copy of the original image?
Solution:
Occasionally, an image appears to contain rough, jagged edges. This condition, known as pixilation,
can be mitigated by blurring the image’s problem areas. Blurring makes these areas appear softer,
but at the cost of losing some definition. We now develop a simple algorithm to blur an entire image.
This algorithm resets each pixel’s color to the average of the colors of the four pixels that surround it.
The function blur expects an image as an argument and returns a copy of that image with blurring.
The function blur begins its traversal of the grid with position (1, 1) and ends with position
(width 2 2, height 2 2). This means that the algorithm does not transform the pixels on the image’s outer
edges. We would like to avoid this, because otherwise, the code would have to check for the grid’s
boundaries when it obtains information from a pixel’s neighbors (the pixels on the boundaries have only two
or three neighbors, rather than four).

"""
