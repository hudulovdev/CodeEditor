import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
    if filepath:
        with open(filepath, "r") as file:
            editor.delete("1.0", tk.END)
            editor.insert(tk.END, file.read())

def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("Python files", "*.py")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(editor.get("1.0", tk.END))
        messagebox.showinfo("Save", "File saved successfully.")

def exit_editor():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        window.destroy()

window = tk.Tk()
window.title("Simple Code Editor")

menu = tk.Menu(window)
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

window.config(menu=menu)

editor = tk.Text(window)
editor.pack(expand=True, fill="both")

window.mainloop()
