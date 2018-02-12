# import subprocess
from tkinter import *
import functions
import os


# Window layout configurations.
window = Tk()  # Create window
v = IntVar()  # Create radio button options
v.set(2)
window.title("Sunny Player")
window.geometry("710x410")

window.rowconfigure(0, weight=1, pad=15)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, pad=30)
window.columnconfigure(1, weight=1)


# Episode Directory and lists.
ep_directory = '/Users/justinlaureano/Movies/Its Always Sunny In ' \
               'Philadelphia/All/'
episode_list = []
current_playlist = []


# Create episode list label.
episode_lbl = Label(
    window,
    text="Episode List:",
    fg='black',
    font=("Helvetica", 16, "bold"))

episode_lbl.grid(row=0, column=0, columnspan=3, padx=15, sticky=W)


# Create episode listbox.
ep_listbox = Listbox(
    window,
    height=18,
    width=40,
    font=("Helvetica", 14))
ep_listbox.grid(row=1, column=0, rowspan=10, sticky=N)


# Fill listbox with episodes
for filename in os.listdir(ep_directory):
    episode_list.append(filename)

for file in episode_list[1:]:
    ep_listbox.insert(END, file)

ep_listbox.select_set(0)


# Create player options label.
episode_lbl = Label(
    window,
    text="Player Options",
    fg='black',
    font=("Helvetica", 16, "bold"))
episode_lbl.grid(row=0, column=1, columnspan=4, padx=15, sticky=W)


# Create playlist radio button.
playlist_btn = Radiobutton(
    window,
    text="Create Playlist",
    variable=v,
    value=1,
    font=("Helvetica", 14))
playlist_btn.grid(row=1, column=1, columnspan=4, padx=10, sticky=W)


# Create playlist listbox.
playlist_box = Listbox(
    window,
    height=8,
    width=40,
    font=("Helvetica", 14))
playlist_box.grid(row=2, column=1, rowspan=1, columnspan=4, padx=15,
                  sticky=W+N)


# Create Add to Playlist button.
add_btn = Button(
    window,
    text="Add",
    command=lambda: functions.add_video(ep_listbox, playlist_box,
                                        current_playlist, v))
add_btn.grid(row=7, column=0, padx=15, pady=15)


# Create Up, Down, and Remove from Playlist button.
up_btn = Button(
    window,
    text="Up",
    command=lambda: functions.move_up_list(playlist_box))
up_btn.grid(row=3, column=1, padx=15, pady=10, sticky=W)

down_btn = Button(
    window,
    text="Down",
    command=lambda: functions.move_down_list(playlist_box))
down_btn.grid(row=3, column=2, columnspan=2, padx=15, pady=10, sticky=W)

remove_btn = Button(
    window,
    text="Remove",
    command=lambda: functions.remove_video(playlist_box))
remove_btn.grid(row=3, column=4, padx=15, pady=10, sticky=E)


# Shuffle radio button.
shuffle_btn = Radiobutton(
    window,
    text="Shuffle All",
    variable=v,
    value=2,
    font=("Helvetica", 14))
shuffle_btn.grid(row=4, column=1, columnspan=4, padx=15, pady=5, sticky=W)


# Create control options label.
control_lbl = Label(
    window,
    text="Controls",
    fg='black',
    font=("Helvetica", 14, "bold"))
control_lbl.grid(row=5, column=1, columnspan=4, padx=15, sticky=W)


# Pause and next buttons.
pause_btn = Button(
    window,
    text="Pause",
    command=functions.pause_video)
pause_btn.grid(row=6, column=1, padx=15, sticky=W)

skip_btn = Button(
    window,
    text="Skip",
    command=functions.skip_video)
skip_btn.grid(row=6, column=2, padx=15, sticky=W)


# Create control options label.
vol_lbl = Label(
    window,
    text="Vol",
    fg='black',
    font=("Helvetica", 14))

vol_lbl.grid(row=6, column=3, padx=(15, 0), sticky=E)


# Volume sliders.
vol = Scale(
    window,
    from_=0,
    to=10,
    orient=HORIZONTAL,
    resolution=1,
    showvalue=0,
    length=100,
    command=functions.change_volume)
vol.set(100)
vol.grid(row=6, column=4, padx=15, sticky=W)


# Run program button
play_btn = Button(window,
                  text="Play",
                  command=lambda: functions.run_program(v, current_playlist,
                                                        ep_directory))
play_btn.grid(row=7, column=4, padx=15, pady=15, sticky=E)

window.mainloop()
