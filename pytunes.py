# Pytunes music player

import tkinter
import json

file = 'music.json'

def load():
    with open(file, 'r') as f:
        txt = f.read()

    return json.loads(txt)


def play(song_number):
    pass

if __name__ == '__main__':
    library = load()
