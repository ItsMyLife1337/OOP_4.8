#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def resize_text():
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text.config(width=width, height=height)
    except ValueError:
        pass


def on_focus_in(event):
    text.config(bg="white")


def on_focus_out(event):
    text.config(bg="lightgrey")


root = Tk()

width_label = Label(root, text="Ширина:")
width_label.pack(side=LEFT, padx=5)
width_entry = Entry(root)
width_entry.pack(side=LEFT, padx=5)
width_entry.insert(0, "20")

height_label = Label(root, text="Высота:")
height_label.pack(side=LEFT, padx=5)
height_entry = Entry(root)
height_entry.pack(side=LEFT, padx=5)
height_entry.insert(0, "10")

text = Text(root, bg="lightgrey", wrap=WORD)
text.pack(pady=10, padx=10, fill=BOTH, expand=True)

resize_button = Button(root, text="Изменить", command=resize_text)
resize_button.pack(pady=5)

text.bind("<FocusIn>", on_focus_in)
text.bind("<FocusOut>", on_focus_out)

root.mainloop()
