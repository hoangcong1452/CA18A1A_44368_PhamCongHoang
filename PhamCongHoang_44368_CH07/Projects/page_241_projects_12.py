"""
Author: pham cong hoang
Date: 18/10/2021

Problem: Each image-processing function that modifies its image argument has the same
loop pattern for traversing the image. The only thing that varies is the code used
to change each pixel within the loop. Section 6.6 of this book, on higher-order
functions, suggests a simpler design pattern for such code. Design a single function, named transform, which expects an image and a function as arguments.
When this function is called, it should be passed another function that expects a
tuple of integers and returns a tuple of integers. This is the function that transforms the information for an individual pixel (such as converting it to black and
white or gray-scale). The transform function contains the loop logic for traversing its image argument. In the body of the loop, the transform function accesses
the pixel at the current position, passes it as an argument to the other function,
and resets the pixel in the image to the function’s value. Write and test a script
that defines this function and uses it to perform at least two different types of
transformation on an image.
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
