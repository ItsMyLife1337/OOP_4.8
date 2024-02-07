#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def draw_scene():
    canvas.create_oval(50, 50, 150, 150, fill="yellow", outline="yellow")

    canvas.create_rectangle(100, 150, 250, 300, fill="orange", outline="black")  # основание дома
    canvas.create_polygon(100, 150, 175, 50, 250, 150, fill="brown", outline="black")  # крыша
    canvas.create_rectangle(130, 200, 170, 250, fill="blue", outline="black")  # окно
    canvas.create_rectangle(200, 200, 240, 250, fill="red", outline="black")  # дверь

    for x in range(0, 300, 5):
        canvas.create_line(x, 300, x + 20, 350, fill="green")


root = Tk()

canvas = Canvas(root, width=300, height=400, bg="skyblue")
canvas.pack()

draw_scene()

root.mainloop()
