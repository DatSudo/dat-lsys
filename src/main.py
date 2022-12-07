import tkinter as tk
import tkinter.ttk as ttk
import turtle
import argparse

from samples import *


DESCRIPTION = """
    L-system generator implemented in Python3
"""

USAGE = """
    python dat-lsys.py [-h] [-l {L-system}] [-n {0,...,7}]
"""



def main() -> None:
    # Get input
    parser = argparse.ArgumentParser(
        prog="dat-lsys",
        description=DESCRIPTION,
        usage=USAGE)

    parser.add_argument(
        "-l", "--lsystem", help="L-System name",
        choices={"kc", "dc", "st", "fp"})
    parser.add_argument(
        "-n", "--numgen",
        help="Number of generations",
        type=int,
        choices={n for n in range(0,8)})

    args = parser.parse_args()

    # Interface
    root = tk.Tk()
    root.geometry("600x600")

    fr = tk.Frame(root)
    fr.pack(fill="both", expand=True)

    tcanvas = turtle.ScrolledCanvas(root, width=1000, height=1000)
    tcanvas.pack(fill="both", expand=True)

    screen = turtle.TurtleScreen(tcanvas)
    screen.bgcolor("black")
    screen.screensize(10000, 10000)

    pen = turtle.RawTurtle(screen)
    pen.color("yellow")
    pen.hideturtle()

    screen.tracer(0)


    screen.update()

    root.mainloop()


if __name__ == "__main__":
    main()