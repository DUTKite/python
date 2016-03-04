import pygame
import Tkinter as tk

window=tk.Tk()
pygame.init()
pygame.mixer.music.load("music.mp3")
started=False
playing=False

def buttonclick():
    global playing, started
    if not playing:
        if not started:
            pygame.mixer.music.play(-1)
            started=True
        else:
            pygame.mixer.music.unpause()
            button.config(text="pause")

    else:
        pygame.mixer.music.pause()
        button.config(text="play")
    playing=not playing

def setvolume(val):
    volume=float(slider.get())
    pygame.mixer.music.set_volume(volume/100)



slider=tk.Scale(window,from_=0,to=100,command=setvolume)
button=tk.Button(window,text="play",command=buttonclick)

slider.pack()
slider.set(100)
button.pack()
window.mainloop()



