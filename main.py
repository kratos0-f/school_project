import tkinter as tk
from tkinter import ttk
import textEditorStarter

window = tk.Tk()

texteditorBtn = tk.Button(
    window,
    text="Add new template",
    #command=lambda: textEditorStarter.startEditor()
)

texteditorBtn.pack()

window.mainloop()
