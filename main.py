from tkinter import *
from random import randint
from Objects import *

obj_list = []
total_blocks = 0


def animate(event):
    print(1)
    global total_blocks
    temp_x_velocity = randint(5, 10)
    temp_y_velocity = randint(5, 10)
    temp_obj = Blocks(window, temp_x_velocity, temp_y_velocity)
    temp_obj.animation()
    total_blocks += 1


def escape(event):
    window.destroy()


window = Tk()
window.title("Dynamic Animation")
window.attributes('-fullscreen', True)
window.config(bg='black')
window.bind('<space>', animate)
window.bind("q", escape)
window.mainloop()
