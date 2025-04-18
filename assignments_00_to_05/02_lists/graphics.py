import tkinter
from tkinter import *

class Canvas:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title('Canvas Window')
        self.canvas = tkinter.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self._click_var = IntVar()
        self.last_click = (0, 0)
        self.canvas.bind("<Button-1>", self._on_click)

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def set_color(self, item, color):
        self.canvas.itemconfig(item, fill=color)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def get_mouse_x(self):
        return self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()

    def get_mouse_y(self):
        return self.canvas.winfo_pointery() - self.canvas.winfo_rooty()

    def moveto(self, item, x, y):
        # Move rectangle to (x, y)
        x0, y0, x1, y1 = self.canvas.coords(item)
        width = x1 - x0
        height = y1 - y0
        self.canvas.coords(item, x, y, x + width, y + height)

    def wait_for_click(self):
        self.root.wait_variable(self._click_var)

    def get_last_click(self):
        return self.last_click

    def _on_click(self, event):
        self.last_click = (event.x, event.y)
        self._click_var.set(1)

    def run(self):
        self.root.mainloop()

# Tumhara pehla wala GraphWin, Point, Circle bhi reh sakte hain, agar doosri file use kar rahi hai
class GraphWin:
    def __init__(self, title, width, height):
        self.win = Tk()
        self.win.title(title)
        self.canvas = tkinter.Canvas(self.win, width=width, height=height)
        self.canvas.pack()
        self.win.update()

    def getMouse(self):
        self.win.mainloop()

    def close(self):
        self.win.destroy()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, win):
        x, y = self.center.x, self.center.y
        r = self.radius
        win.canvas.create_oval(x - r, y - r, x + r, y + r)
