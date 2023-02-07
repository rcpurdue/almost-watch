#!/usr/bin/env python
# almost-watch, rcampbel@purdue.edu, 2023-02-07

import time
import math
import tkinter as tk

CANVAS_SIZE = 1024
DEG_SEP = 360 / 12
RADIUS = CANVAS_SIZE / 2
TICK_SIZE = 16
BACKGROUND_COLOR = 'black'
OUTLINE_COLOR = 'white'
FILL_COLOR = 'white'


def draw_clock_face(canvas):
    # Outline
    canvas.create_oval(RADIUS-RADIUS/2, RADIUS-RADIUS/2, RADIUS+RADIUS/2, RADIUS+RADIUS/2, outline=OUTLINE_COLOR)

    # Indices - based on https://stackoverflow.com/a/36732748
    for i in range(12):
        x = RADIUS/2 * math.cos(i * DEG_SEP * math.pi / 180) + RADIUS
        y = RADIUS/2 * math.sin(i * DEG_SEP * math.pi / 180) + RADIUS
        canvas.create_rectangle(x-TICK_SIZE/2, y-TICK_SIZE/2, x+TICK_SIZE/2, y+TICK_SIZE/2, fill=FILL_COLOR,
                                outline=OUTLINE_COLOR)


def run(canvas):

    i = 0
    positions = [90, 0, 270, 180]

    while True:
        arc = canvas.create_arc(RADIUS-RADIUS/2, RADIUS-RADIUS/2, RADIUS+RADIUS/2, RADIUS+RADIUS/2,
                                fill=FILL_COLOR, outline=OUTLINE_COLOR,
                                start=positions[i % 4], extent=90)
        i += 1
        root.update()
        time.sleep(1)
        canvas.delete(arc)
        root.update()


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, height=CANVAS_SIZE, width=CANVAS_SIZE)
    draw_clock_face(canvas)
    canvas.pack()
    run(canvas)  # root.mainloop()
