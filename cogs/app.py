import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk(className="RevisePy Dev 1.0")
root.resizable(0, 0)
debugText = "owo owo owo owo"


def OptionCommand():
    print("Opening option tab")


def OpenFileCommand():
    print("Opening open file tab")


def CreateFileCommand():
    print("Opening create file tab")


def Application():
    # Defines what is the first layer
    canvas = tk.Canvas(root, width=1280, height=720, bg="#363949", highlightthickness=0)
    canvas.pack()

    # Change text on the GUI
    debugLabel = tk.Label(canvas, text=debugText, font=("Roboto", 25), fg="white", bg="#363949")
    debugLabel.place(x=750, y=250)

    # Defines the second frame and where it's placed
    sideBar = tk.Canvas(root, bg="#2f314a", highlightthickness=0)
    sideBar.place(relwidth=0.2, relheight=1)

    # Defines the title box and where it's placed
    titleBox = tk.Canvas(sideBar, bg="#20222f", highlightthickness=0)
    titleBox.place(relwidth=1, relheight=0.1)

    # Defines a label in the title box
    titleLabel = tk.Label(titleBox, text="RevisePy", font=("Roboto", 25), fg="white", bg="#20222f")
    titleLabel.place(relwidth=1, relheight=1)

    # Defines open file buttons on the side bar
    openFileButton = tk.Button(sideBar, text="Open revision file", font=("Roboto", 12), pady=15, padx=35, fg="white",
                               bg="#292b39", command=OpenFileCommand)
    openFileButton.place(anchor="center", x=125, y=125)

    # Defines create file buttons on the side bar
    createFileButton = tk.Button(sideBar, text="Create revision file", font=("Roboto", 12), pady=15, padx=35, fg="white"
                                 , bg="#292b39", command=CreateFileCommand)
    createFileButton.place(anchor="center", x=125, y=200)

    # Defines create options on the side bar
    optionButton = tk.Button(sideBar, text="Options", pady=15, font=("Roboto", 8), padx=35, fg="white",
                             bg="#292b39", command=OptionCommand)
    optionButton.place(anchor="center", x=125, y=675)

    root.mainloop()


Application()
