from tkinter import *
from tkinter import ttk

def hello(event):
    print("Hello, world!")

window = Tk()

st = ttk.Style()
st.configure("TButton", background="#345", foreground="red", font=("Arial", 14))

btn = ttk.Button(
    window,
    text="Hello, world!",
    style="TButton"
)

print(btn.configure().keys())

btn.bind("<Button-1>", hello)
btn.pack()

window.mainloop()
