import tkinter as tk
import os
from modules.textEditor import main_loop
from modules.moduleTable import Table

window = tk.Tk()

texteditorBtn = tk.Button(
    window,
    text="Add new template",
    command=main_loop
)

filename_tuple = ()
for filename in os.listdir("data"):
    filename_tuple += ((filename), )
file_list = Table(window, headings=("File name"), rows=filename_tuple)
file_list.pack(expand=tk.YES, fill=tk.BOTH)

texteditorBtn.pack()

window.mainloop()
