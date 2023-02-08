#!/usr/bin/env python
# almost-watch, rcampbel@purdue.edu, 2023-02-07

# import time
import math
import tkinter as tk
from tkinter import font

ACCURACY = int(60 / 10)
CANVAS_SIZE = 1024
DEG_SEP = 360 / 12
RADIUS = CANVAS_SIZE / 2
TICK_SIZE = 16
BACKGROUND_COLOR = 'black'
OUTLINE_COLOR = 'white'
FILL_COLOR = 'white'
FONT_FAMILY = 'bitstream charter'


class AlmostWatch:
    def __init__(self):
        self.positions = [deg for deg in range(360, 0, int(-360 / ACCURACY))]
        self.step = 1
        self.min_hand = None
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, bg=BACKGROUND_COLOR, height=CANVAS_SIZE, width=CANVAS_SIZE)

        # Draw face outline
        self.canvas.create_oval(RADIUS-RADIUS/2, RADIUS-RADIUS/2, RADIUS+RADIUS/2, RADIUS+RADIUS/2,
                                outline=OUTLINE_COLOR)

        # Draw indices - ref: https://stackoverflow.com/a/36732748
        for i in range(12):
            x = RADIUS/2 * math.cos(i * DEG_SEP * math.pi / 180) + RADIUS
            y = RADIUS/2 * math.sin(i * DEG_SEP * math.pi / 180) + RADIUS
            self.canvas.create_rectangle(x-TICK_SIZE/2, y-TICK_SIZE/2, x+TICK_SIZE/2, y+TICK_SIZE/2, fill=FILL_COLOR,
                                         outline=OUTLINE_COLOR)

        self.canvas.pack()
        self.update()
        self.root.mainloop()

    def calc_min_text_pos(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.min_hand)
        x = x1 + (x2 - x1) / 2
        y = y1 + (y2 - y1) / 2
        print(x1, y1, x2, y2, ':', x, y)
        return x, y

    def update(self):

        # Erase old minutes hand & text
        if self.min_hand is not None:
            self.canvas.delete(self.min_hand)
            self.canvas.delete(self.min_text)

        # Draw minutes
        self.min_hand = self.canvas.create_arc(RADIUS-RADIUS/2, RADIUS-RADIUS/2, RADIUS+RADIUS/2, RADIUS+RADIUS/2,
                                               fill=FILL_COLOR, outline=OUTLINE_COLOR,
                                               start=self.positions[(self.step-1) % ACCURACY], extent=360/ACCURACY)
        x, y = self.calc_min_text_pos()
        self.min_text = self.canvas.create_text(x, y, text=str(self.step),
                                                font=font.Font(family=FONT_FAMILY, size=32, weight="bold"),
                                                fill=BACKGROUND_COLOR)

        # Draw hour
        self.canvas.create_oval(RADIUS-RADIUS/4.5, RADIUS-RADIUS/4.5, RADIUS+RADIUS/4.5, RADIUS+RADIUS/4.5,
                                outline=OUTLINE_COLOR, fill=BACKGROUND_COLOR)
        self.canvas.create_text(RADIUS, RADIUS, text=str(self.step),
                                font=font.Font(family=FONT_FAMILY, size=128, weight="bold", underline=False),
                                fill=OUTLINE_COLOR)

        self.step = self.step + 1 if self.step < 12 else 1
        self.root.update()
        self.root.after(2000, self.update)  # Ref: https://stackoverflow.com/a/66101733


if __name__ == "__main__":
    AlmostWatch()
