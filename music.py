import os
from tkinter import *
import pygame
from tkinter import messagebox
from tkinter import filedialog

root =Tk()
root.geometry('400x350')
root.title('Music Player')
root.resizable(False,False)


#==============color codes for theme TuneFlow
BG_COLOR = "#121212"
FG_COLOR = "#FFFFFF"
ACCENT_BLUE = "#00C3FF"
ACCENT_GREEN = "#00FFAB"  
LISTBOX_BG = "#1E1E1E"

root.configure(bg=BG_COLOR)


pygame.mixer.init()

menu_bar = Menu(root, bg=BG_COLOR, fg=FG_COLOR, tearoff=False)
root.config(menu=menu_bar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name , ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)
    
    if not songs:
        messagebox.showinfo("No Songs", "No MP3 files found in the selected directory.")
        return

    
    for song in songs:
        song_list.insert('end' ,song)
        
    song_list.selection_set(0)
    current_song = songs[song_list.curselection()[0]]

def play_music():
    global current_song,paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory , current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False    
    
    
def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True
    
def  next_music():
    global current_song,paused
    
    try:
        song_list.selection_clear(0,END)
        song_list.selection_set(songs.index(current_song) + 1)
        current_song =songs[song_list.curselection()[0]]
        play_music()
    except:
        pass
    
def prev_music():
    global current_song,paused
    
    try:
        song_list.selection_clear(0,END)
        song_list.selection_set(songs.index(current_song) - 1)
        current_song =songs[song_list.curselection()[0]]
        play_music()
    except:
        pass
    

# =========== Graphical User Interface ===========

organise_menu = Menu(menu_bar,tearoff=False, bg=BG_COLOR, fg=FG_COLOR)
organise_menu.add_command(label='Select Folder',command=load_music)
menu_bar.add_cascade(label='Organise',menu=organise_menu)

song_list = Listbox(root,width=100,height=15, bg=LISTBOX_BG, fg=ACCENT_GREEN, selectbackground=ACCENT_BLUE,)
song_list.pack()

play_btn_image = PhotoImage(file="play.png")
pause_btn_image = PhotoImage(file="pause.png")
next_btn_image = PhotoImage(file="nextt.png")
prev_btn_image = PhotoImage(file="prev.png")

control_panel = Frame(root,bg=BG_COLOR)
control_panel.pack()

btn_style = {"borderwidth": 0, "height": 32, "width": 32, "bg": BG_COLOR, "activebackground": BG_COLOR}

play_btn = Button(control_panel, image=play_btn_image, command=play_music, **btn_style)
pause_btn = Button(control_panel, image=pause_btn_image, command=pause_music, **btn_style)
next_btn = Button(control_panel, image=next_btn_image, command=next_music, **btn_style)
prev_btn = Button(control_panel, image=prev_btn_image, command=prev_music, **btn_style)


play_btn.grid(row= 0,column=1,padx=7,pady=10)
pause_btn.grid(row= 0,column=2,padx=7,pady=10)
next_btn.grid(row= 0,column=3,padx=7,pady=10)
prev_btn.grid(row= 0,column=0,padx=7,pady=10)

root.mainloop()
