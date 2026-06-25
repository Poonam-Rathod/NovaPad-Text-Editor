import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Poonam Text Editor")
root.geometry("800x600+100+100")

text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Consolas", 12),
    undo=True,
    bg="#1E1E1E",
    fg="white",
    insertbackground="white"
)
text.pack(expand=True, fill=tk.BOTH)

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

        messagebox.showinfo("Success", "File Saved Successfully")

def undo_text():
    text.edit_undo()

def redo_text():
    text.edit_redo()

def cut_text():
    text.event_generate("<<Cut>>")  
    
def copy_text():
    text.event_generate("<<Copy>>")   
    
def paste_text():
    text.event_generate("<<Paste>>")          
                

# Menu Bar
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
edit_menu=tk.Menu(menu,tearoff=0)

menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Edit",menu=edit_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
edit_menu.add_command(label="Undo",command=undo_text)
edit_menu.add_command(label="Redo",command="redo_text")

file_menu.add_separator()

edit_menu.add_command(label="Cut",command=cut_text)
edit_menu.add_command(label="Copy",command=copy_text)
edit_menu.add_command(label="Paste",command=paste_text)

file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()