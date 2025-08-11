from tkinter import *
import random
colors = ['green', 'blue', 'red', 'aliceblue', 'yellow', 'pink', 'grey', 'purple', 'white',
          'aqua', 'blueviolet', 'blue4', 'brown4', 'burlywood4', 'cadetblue3',
          'chartreuse', 'darkgoldenrod1', 'darkorchid',
          'darkseagreen3', 'darkturquoise', 'deeppink2', 'dodgerblue1'
          ]


class Blocks:
    def __init__(self, window, x_velocity, y_velocity):
        self.window = window
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.block = Label(window, bg='white', width=10, height=5)
        self.block.pack()

    def animation(self):
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        global colors
        if self.block.winfo_x() + self.block.winfo_width() >= width or self.block.winfo_x() < 0:
            self.x_velocity = -self.x_velocity
            self.block.config(bg=colors[random.randint(0, len(colors) - 1)])
        if self.block.winfo_y() + self.block.winfo_height() >= height or self.block.winfo_y() < 0:
            self.y_velocity = -self.y_velocity
            self.block.config(bg=colors[random.randint(0, len(colors) - 1)])

        self.block.place(x=self.block.winfo_x()+self.x_velocity, y=self.block.winfo_y()+self.y_velocity)
        print(f"Block Cordinates:({self.block.winfo_x()},{self.block.winfo_y()})")
        self.window.update()
        self.window.after(10, self.animation)