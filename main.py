import tkinter as tk
from tkinter import ttk
from textEditor import main_loop

window = tk.Tk()

texteditorBtn = tk.Button(
    window,
    text="Add new template",
    command=main_loop
)

texteditorBtn.pack()

window.mainloop()
