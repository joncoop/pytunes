# Pytunes music player
# Tkinter tutorial - http://www.python-course.eu/python_tkinter.php 

# imports
import json
import pygame
from tkinter import *


# initialize mixer
pygame.mixer.init()


# global config
music_data = 'music.json'


class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.play = Button(frame, 
                             text="Play",
                             fg="green",
                             command=self.play)

        self.pause = Button(frame,
                             text="Pause",
                             fg="red",
                             command=self.pause)

        self.play.pack(side=LEFT)    
        self.pause.pack(side=LEFT)

        self.library = self.load(music_data)

    def load(self, path):
        with open(path, 'r') as f:
            txt = f.read()

        return json.loads(txt)
                      
    def play(self, song=None):
        #path = song['path']
        path = self.library[0]['path'] # for testin
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
    def pause(self):
        pygame.mixer.music.stop()

        
# main
if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
