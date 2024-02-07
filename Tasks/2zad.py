#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def on_enter(event):
    text = entry.get()
    if text:
        listbox.insert(END, text)
        entry.delete(0, END)


def on_double_click(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_text = listbox.get(selected_index)
        entry.delete(0, END)
        entry.insert(0, selected_text)


root = Tk()

entry = Entry(root)
entry.pack(pady=10, padx=10, fill=X)

entry.bind("<Return>", on_enter)

listbox = Listbox(root)
listbox.pack(pady=10, padx=10, fill=BOTH, expand=True)

listbox.bind("<Double-Button-1>", on_double_click)

root.mainloop()
