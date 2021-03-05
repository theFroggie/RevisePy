import tkinter as tk
from tkinter import filedialog, Text
import os


def Application():
    root = tk.Tk()

    # Defines what is the first layer
    canvas = tk.Canvas(root, width=1280, height=720, bg="#363949")
    canvas.pack()

    # Defines the second frame and where it's placed
    sideBar = tk.Canvas(root, bg="#2f314a")
    sideBar.place(relwidth=0.2, relheight=1)

    # Defines the title box and where it's placed
    titleBox = tk.Canvas(sideBar, bg="#20222f")
    titleBox.place(relwidth=1, relheight=0.1)

    # Defines a label in the title box
    titleLabel = tk.Label(titleBox, text="RevisePy", font=50, fg="white", bg="#20222f")
    titleLabel.place(relwidth=0.75, relheight=0.75, x=30, y=7.5)

    # Defines buttons on the side bar
    openFileButton = tk.Button(sideBar, text="Open revision file", pady=15, padx=50, fg="white", bg="#292b39")
    openFileButton.place(x=25, y=100)

    root.mainloop()
