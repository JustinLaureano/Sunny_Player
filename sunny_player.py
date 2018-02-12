import subprocess
from tkinter import *
import functions
import os


window = Tk()  # create window
window.title("Sunny Player")
window.geometry("620x370")

# Create Menu Bar
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)

ep_lbl = Label(window, text="Episode List:", fg='black', font=("Helvetica", 16,
    "bold"))
pl_btn = Radiobutton(window, text="Create Playlist")

ep_lbl.grid(row=1, column=0, padx=15, sticky=W)
pl_btn.grid(row=1, column=1, padx=15, sticky=W)

# Create the frame object.
frm = Frame(window)
frm.grid(row=2, column=0, sticky=N+S)

# Window layout configurations.
window.rowconfigure(0, weight=1, pad=10)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, pad=30)
window.columnconfigure(1, weight=1)

functions.create_episode_list(frm)

# Create playlist listbox.
playlist = Listbox(frm, height=8, width=45, font=("Helvetica", 12))
playlist.grid(row=2, column=1, padx=15, sticky=W+N)


def run_program():
    """Run the program and play episodes on the tv."""
    subprocess.call(['castnow --address 192.168.2.178 '
                     '/Users/justinlaureano/Movies/Its\ Always\ Sunny\ '
                     'In\ Philadelphia/All --shuffle'], shell=True)


# Create Run Button
run_btn = Button(window, text="Play", command=run_program)
run_btn.grid(row=3, column=1)

window.mainloop()
