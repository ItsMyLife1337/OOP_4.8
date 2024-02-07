#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def move_items(source_listbox, destination_listbox):
    selected_items = source_listbox.curselection()

    for index in selected_items[::-1]:
        item = source_listbox.get(index)
        destination_listbox.insert(END, item)
        source_listbox.delete(index)


def on_add_button_click():
    move_items(products_listbox, shopping_listbox)


def on_remove_button_click():
    move_items(shopping_listbox, products_listbox)


root = Tk()
root.title("Magazine")

products_listbox = Listbox(root, selectmode=MULTIPLE)
products_listbox.pack(side=LEFT, padx=10)
products = ["Apple", "Banana", "Orange", "Milk", "Bread", "Eggs"]

for product in products:
    products_listbox.insert(END, product)

shopping_listbox = Listbox(root, selectmode=MULTIPLE)
shopping_listbox.pack(side=RIGHT, padx=10)

add_button = Button(root, text=">>>>", command=on_add_button_click)
add_button.pack(pady=5)

remove_button = Button(root, text="<<<<", command=on_remove_button_click)
remove_button.pack(pady=5)

root.mainloop()
