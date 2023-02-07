#!/usr/bin/env python
# almost-watch, rcampbel@purdue.edu, 2023-02-07

# import time
import math
import tkinter as tk

ACCURACY = int(60 / 5)
CANVAS_SIZE = 1024
DEG_SEP = 360 / 12
RADIUS = CANVAS_SIZE / 2
TICK_SIZE = 16
BACKGROUND_COLOR = 'black'
OUTLINE_COLOR = 'white'
FILL_COLOR = 'white'


class AlmostWatch:
    def __init__(self):
        self.positions = [deg for deg in range(360, 0, int(-360 / ACCURACY))]
        self.step = 0
        self.arc = None
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

    def update(self):

        if self.arc is not None:
            self.canvas.delete(self.arc)

        self.arc = self.canvas.create_arc(RADIUS-RADIUS/2, RADIUS-RADIUS/2, RADIUS+RADIUS/2, RADIUS+RADIUS/2,
                                          fill=FILL_COLOR, outline=OUTLINE_COLOR,
                                          start=self.positions[self.step % ACCURACY], extent=360/ACCURACY)
        self.step += 1
        self.root.update()
        self.root.after(1000, self.update)  # Ref: https://stackoverflow.com/a/66101733


if __name__ == "__main__":
    AlmostWatch()
