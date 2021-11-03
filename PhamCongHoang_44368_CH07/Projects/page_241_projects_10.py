"""
Author: pham cong hoang
Date: 18/10/2021

Problem: The edge-detection function described in this chapter returns a black-and-white
image. Think of a similar way to transform color values so that the new image is still
in its original colors but the outlines within it are merely sharpened. Then, define a
function named sharpen that performs this operation. The function should expect
an image and two integers as arguments. One integer should represent the degree
to which the image should be sharpened. The other integer should represent the
threshold used to detect edges. (Hint: A pixel can be darkened by making its RGB
values smaller.)
Solution:
"""
import os
import os.path

import tkinter

tk = tkinter

_root = None


class ImageView(tk.Canvas):
    def __init__(self, image,
                 title="New Image",
                 autoflush=False):
        master = tk.Toplevel(_root)
        master.protocol("WM_DELETE_WINDOW", self.close)
        tk.Canvas.__init__(self, master,
                           width=image.getWidth(),
                           height=image.getHeight())
        self.master.title(title)
        self.pack()
        master.resizable(0, 0)
        self.image = image
        self.height = image.getHeight()
        self.width = image.getWidth()
        self.autoflush = autoflush
        self.closed = False

    def close(self):

        self.closed = True
        self.master.destroy()
        self.image.canvas = None
        _root.quit()

    def isClosed(self):
        return self.closed

    def getHeight(self):

        return self.height

    def getWidth(self):

        return self.width


class Image:

    def __init__(self, *args):
        self.canvas = None
        if len(args) == 1:
            name = args[0]
            if type(name) != str:
                raise Exception('Must be a file name')
            if name[-4:].upper() != '.GIF':
                raise Exception('File must be a GIF')
            if not os.path.exists(args[0]):
                raise Exception('File not in current directory')
            self.image = tk.PhotoImage(file=args[0], master=_root)
            self.filename = args[0]
            self.width = self.image.width()
            self.height = self.image.height()
        else:  # arguments are width and height
            self.width, self.height = args
            self.image = tk.PhotoImage(master=_root,
                                       width=self.width,
                                       height=self.height)
            self.filename = ""

    def getWidth(self):

        return self.width

    def getHeight(self):

        return self.height

    def getPixel(self, x, y):


        value = self.image.get(x, y)
        print("value:", value)
        if type(value) == int:
            return (value, value, value)
        else:
            return value

    def setPixel(self, x, y, color):

        self.image.put("{#%02x%02x%02x}" % color, (x, y))

    def draw(self):

        if not self.canvas:
            self.canvas = ImageView(self,
                                    self.filename)
        self.canvas.create_image(self.width / 2,
                                 self.height / 2,
                                 image=self.image)
        _root.mainloop()

    def save(self, filename=""):

        if filename == "":
            return
        else:
            self.filename = filename
        path, name = os.path.split(filename)
        ext = name.split(".")[-1]
        if ext != "gif":
            filename += ".gif"
            self.filename = filename
        self.image.write(self.filename, format="gif")

    def clone(self):
        new = Image(self.width, self.height)
        new.image = self.image.copy()
        return new

    def __str__(self):
        rep = ""
        if self.filename:
            rep += ("File name: " + self.filename + "\n")
        rep += ("Width:  " + str(self.width) + \
                "\nHeight: " + str(self.height))
        return rep


_root = tk.Tk()
_root.withdraw()

from images import Image


def sharpen(image, degree, threshold):


    def average(triple):

        (r, g, b) = triple
        return (r + g + b) // 3

    new = image.clone()  # Make changes to a copy
    for y in range(image.getHeight() - 1):  # Work inside the borders
        for x in range(1, image.getWidth()):
            # Obtain average values of current, left, and
            # bottom pixels
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)
            # Detect an edge at current pixel
            if abs(oldLum - leftLum) > threshold or \
                    abs(oldLum - bottomLum) > threshold:
                # Darken that edge
                new.setPixel(x, y,
                             (max(oldPixel[0] - degree, 0),
                              max(oldPixel[1] - degree, 0),
                              max(oldPixel[2] - degree, 0)))
    return new


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    print("Close the window to view the changes to the image.")
    image.draw()
    newimage = sharpen(image, 20, 15)
    newimage.draw()

main()