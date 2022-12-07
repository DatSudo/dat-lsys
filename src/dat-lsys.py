import tkinter as tk
import turtle
import argparse

from samples import *


DESCRIPTION = """
    L-system generator implemented in Python3
"""

USAGE = """
    python dat-lsys.py [-h] [-l {L-system}] [-n {0,...,7}]
"""

GEN_LIMIT = 7

SCREEN_BG = "#1D2021"
PEN_COLOR = "#EBDBB2"


def draw_lsystem(lsys: str, numgen: int, pen) -> None:
    lsystems = {
        "kc": lambda pen, numgen: koch_curve(pen, numgen),
        "dc": lambda pen, numgen: dragon_curve(pen, numgen),
        "st": lambda pen, numgen: sierpinski_triangle(pen, numgen),
        "fp": lambda pen, numgen: fractal_plant(pen,numgen)
    }

    lsystems[lsys](pen, numgen)


def main() -> None:
    # Get input
    parser = argparse.ArgumentParser(
        prog="dat-lsys",
        description=DESCRIPTION,
        usage=USAGE)

    parser.add_argument(
        "-l", "--lsystem", help="L-system name",
        choices={"kc", "dc", "st", "fp"})
    parser.add_argument(
        "-n", "--numgen",
        help="Number of generations",
        type=int,
        choices={n for n in range(0,GEN_LIMIT + 1)})

    args = parser.parse_args()

    # Interface
    root = tk.Tk()
    root.geometry("600x600")

    fr = tk.Frame(root)
    fr.pack(fill="both", expand=True)

    tcanvas = turtle.ScrolledCanvas(root, width=1000, height=1000)
    tcanvas.pack(fill="both", expand=True)

    screen = turtle.TurtleScreen(tcanvas)
    screen.bgcolor(SCREEN_BG)
    screen.screensize(10000, 10000)

    pen = turtle.RawTurtle(screen)
    pen.color(PEN_COLOR)
    pen.hideturtle()

    screen.tracer(0)

    draw_lsystem(args.lsystem, args.numgen, pen)

    screen.update()

    root.mainloop()


if __name__ == "__main__":
    main()