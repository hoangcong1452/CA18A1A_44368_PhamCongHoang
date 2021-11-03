"""
Author: pham cong hoang
Date: 18/10/2021

Problem: Explain why one would use the clone method with a given object.
Solution:
The next few algorithms do not modify an existing image, but instead use that image to generate a brand
new image with the desired properties. One could create a new, blank image of the same height and
width as the original, but it is often useful to start with an exact copy of the original image
that retains the pixel information as well. The Image class includes a clone method for this purpose.
The method clone builds and returns a new image with the same attributes as the original one, but with
an empty string as the filename. The two images are thus structurally equivalent but not identical,
as discussed in Chapter 5. This means that changes to the pixels in one image will have no impact
on the pixels in the same positions in the other image.

"""