import tkinter as tk
from tkinter import messagebox

def click_me():
    data = entry.get()
    print(f"{data} ,Button Clicked")
    messagebox.showinfo("Welcome", 
    f"Welcome to my application {data}")
    # messagebox.showinfo("Welcome","Welcome to my application")

window = tk.Tk()
window.configure(background = "gray")
window.title("My First GUI Program")

entry = tk.Entry(window, width= 40,font=("Arial", 25))
entry.pack(pady = 50)

btn = tk.Button(window, text='submit', command=click_me)
btn.pack()

# label = tk.Label(window, text="Hello World", 
# font=("Arial", 40),
# fg="blue")
# btn = tk.Button(window,
# text="Click Me",
# font=("Arial", 40),
# command = click_me)

# entry = tk.Entry(window, width= 40,
# font=("Arial", 25))
# entry.pack(pady = 50)
# label.pack(pady = 50)
# btn.pack()
window.mainloop()