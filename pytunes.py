# Pytunes music player


# imports
import json
import pygame
import tkinter

# initialize mixer
pygame.mixer.init()

# global config
file = 'music.json'

def load():
    with open(file, 'r') as f:
        txt = f.read()

    return json.loads(txt)


def play(song):
    path = song['path']
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    
def pause():
    pygame.mixer.music.stop()

    
# main
if __name__ == '__main__':
    library = load()
