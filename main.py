import tkinter as tk
import os
from modules.textEditor import main_loop

def openFile():
    print("Hello, world!")

window = tk.Tk()
frame = tk.Frame(window)
frame.pack()

texteditorBtn = tk.Button(
    frame,
    text="Add new template",
    command=main_loop
)


# создает кортеж из всех файлов директории data
filename_tuple = ()
for filename in os.listdir("data"):
    filename_tuple += ((filename), )

# выводим все файлы в список
for i in filename_tuple:
    fileBtn = tk.Button(
        frame,
        text=i,
        command=openFile
    )
    fileBtn.pack(side=tk.BOTTOM)

texteditorBtn.pack(side=tk.TOP)

window.mainloop()
