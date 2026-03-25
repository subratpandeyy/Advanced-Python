import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Components Demo")
root.geometry("600x600")

label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 16))
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

def show_text():
    messagebox.showinfo("Input", f"You entered: {entry.get()}")

btn = tk.Button(root, text="Submit", command=show_text)
btn.pack(pady=5)

check_var = tk.IntVar()
check = tk.Checkbutton(root, text="Accept Terms", variable=check_var)
check.pack(pady=5)

radio_var = tk.StringVar(value="None")

tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1").pack()
tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2").pack()

options = ["Python", "Java", "C++"]
selected_option = tk.StringVar(value=options[0])

dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=5)

listbox = tk.Listbox(root)
for item in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, item)
listbox.pack(pady=5)

text = tk.Text(root, height=5, width=40)
text.pack(pady=5)

frame = tk.Frame(root, bd=2, relief="sunken")
frame.pack(pady=10)

tk.Label(frame, text="Inside Frame").pack()
tk.Button(frame, text="Click Me").pack()

tk.Button(root, text="Exit", command=root.quit).pack(pady=20)

root.mainloop()

