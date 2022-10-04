import tkinter as tk
from tkinter import filedialog
def Quit():
    global root
    root.destroy()

def LoadFile(ev):
    fn = filedialog.Open(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open(fn, 'rt').read())


def SaveFile(ev):
    global textbox
    fn = filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))

def main_loop():
    global root
    root.mainloop()

if __name__ == "__main__":
    global textbox
    root = tk.Tk()

    panelFrame = tk.Frame(root, height=60, bg='gray')
    textFrame = tk.Frame(root, height=340, width=600)

    panelFrame.pack(side='top', fill='x')
    textFrame.pack(side='bottom', fill='both', expand=1)

    textbox = tk.Text(textFrame, font='Arial 14', wrap='word')
    scrollbar = tk.Scrollbar(textFrame)

    scrollbar['command'] = textbox.yview
    textbox['yscrollcommand'] = scrollbar.set

    textbox.pack(side='left', fill='both', expand=1)
    scrollbar.pack(side='right', fill='y')

    loadBtn = tk.Button(panelFrame, text='Load')
    saveBtn = tk.Button(panelFrame, text='Save')
    quitBtn = tk.Button(panelFrame, text='Quit')

    loadBtn.bind("<Button-1>", LoadFile)
    saveBtn.bind("<Button-1>", SaveFile)
    quitBtn.bind("<Button-1>", Quit)

    loadBtn.place(x=10, y=10, width=40, height=40)
    saveBtn.place(x=60, y=10, width=40, height=40)
    quitBtn.place(x=110, y=10, width=40, height=40)
