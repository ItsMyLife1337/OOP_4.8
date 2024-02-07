#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def motion(target_x, target_y):
    current_x, current_y, _, _ = c.coords(ball)

    if current_x < target_x:
        c.move(ball, 1, 0)
    elif current_x > target_x:
        c.move(ball, -1, 0)

    if current_y < target_y:
        c.move(ball, 0, 1)
    elif current_y > target_y:
        c.move(ball, 0, -1)

    if current_x != target_x or current_y != target_y:
        root.after(10, motion, target_x, target_y)


def on_click(event):
    target_x, target_y = event.x, event.y
    motion(target_x, target_y)


root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='green')

c.bind("<Button-1>", on_click)

root.mainloop()
