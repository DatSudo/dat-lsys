import tkinter as tk
import tkinter.ttk as ttk
import turtle

from samples import *


def main() -> None:
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

    koch_curve(pen, 4)

    screen.update()

    root.mainloop()


if __name__ == "__main__":
    main()