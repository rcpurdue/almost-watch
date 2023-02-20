#!/usr/bin/env python
# almost-watch, rect.py, rcampbel@purdue.edu, 2023-02-07

import datetime
import math
import tkinter as tk
from tkinter import font
import random

CANVAS_SIZE = 200
BACKGROUND_COLOR = 'white'
OUTLINE_COLOR = 'white'
FILL_COLOR = 'black'
FONT_FAMILY = 'bitstream charter'
HOUR_FONT_SIZE = 64
MIN_FONT_SIZE = 16
FORMAT_12_HOUR = True
UPDATE_MS = 1000
BLOCK_SIZE = 50
MIN_PER_BLOCK = 5
BLOCKS = [
    [100, 0],
    [150, 0],
    [150, 50],
    [150, 100],
    [150, 150],
    [100, 150],
    [50, 150],
    [0, 150],
    [0, 100],
    [0, 50],
    [0, 0],
    [50, 0]
]


class AlmostWatch:
    def __init__(self, accuracy):
        self.accuracy = accuracy
        self.min_hand = []
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, bg=BACKGROUND_COLOR, height=CANVAS_SIZE, width=CANVAS_SIZE)
        self.canvas.pack()
        self.update()
        self.root.mainloop()

    def update(self):

        # Erase old minutes hand & text
        if self.min_hand:
            self.canvas.delete(self.min_text)

            for block in self.min_hand:
                self.canvas.delete(block)

            self.min_hand = []

        # Draw minutes
        minutes = datetime.datetime.now().minute
        minutes = random.randint(0, 59)
        print(minutes)

        for i in range(math.floor(minutes / MIN_PER_BLOCK)+1):
            r, c = BLOCKS[i][0], BLOCKS[i][1]
            block = self.canvas.create_rectangle(r, c, r+BLOCK_SIZE, c+BLOCK_SIZE, fill=FILL_COLOR,
                                                 outline=OUTLINE_COLOR)
            self.min_hand.append(block)

        self.min_text = self.canvas.create_text(int(r+BLOCK_SIZE/2), int(c+BLOCK_SIZE/2), text=str((i+1)*5),
                                                font=font.Font(family=FONT_FAMILY, size=MIN_FONT_SIZE, weight="bold"),
                                                fill=BACKGROUND_COLOR)

        # Draw hour
        hours = datetime.datetime.now().hour

        if FORMAT_12_HOUR:
            hours = hours - 12 if hours > 12 else hours

        self.canvas.create_text(100, 100, text=str(hours),
                                font=font.Font(family=FONT_FAMILY, size=HOUR_FONT_SIZE, weight="bold", underline=False),
                                fill=FILL_COLOR)
        self.root.update()
        self.root.after(UPDATE_MS, self.update)  # Ref: https://stackoverflow.com/a/66101733


if __name__ == "__main__":
    AlmostWatch(15)
