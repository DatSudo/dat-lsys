from lsystem import LSystem

import math


def koch_curve(pen, num_gen: int) -> None:
    rules = {"F": "F+F-F-F+F"}
    axiom = "F"

    lsys = LSystem(axiom, rules, num_gen)
    sentence = lsys.generate()

    for s in sentence:
        if s == "F": pen.forward(10)
        elif s == "+": pen.left(90)
        else: pen.right(90)

def sierpinski_triangle(pen, num_gen: int) -> None:
    rules = {
        "F": "F-G+F+G-F",
        "G": "GG"
    }
    axiom = "F-G-G"

    lsys = LSystem(axiom, rules, num_gen)
    sentence = lsys.generate()

    for s in sentence:
        if s in {"F", "G"}: pen.forward(10)
        elif s == "+": pen.left(120)
        else: pen.right(120)

def dragon_curve(pen, num_gen: int) -> None:
    rules = {
        "F": "F+G",
        "G": "F-G"
    }
    axiom = "F"

    lsys = LSystem(axiom, rules, num_gen)
    sentence = lsys.generate()

    for s in sentence:
        if s in {"F", "G"}: pen.forward(10)
        elif s == "+": pen.left(90)
        else: pen.right(90)

def fractal_plant(pen, num_gen: int) -> None:
    rules = {
        "F": "FF",
        "X": "F+[[X]-X]-F[-FX]+X"
    }
    axiom = "X"

    lsys = LSystem(axiom, rules, num_gen)
    sentence = lsys.generate()


    xpos, ypos = pen.pos()
    theta = math.pi / 2 - 0.4
    dtheta = math.radians(25)
    positions = []
    for s in sentence:
        if s in {"F", "G"}:
            curr_x = xpos + 5 * math.cos(theta)
            curr_y = ypos + 5 * math.sin(theta)
            pen.goto(curr_x, curr_y)
            pen.down()
            xpos, ypos = curr_x, curr_y
        elif s == "+":
            theta += dtheta
            pen.setheading(theta)
        elif s == "-":
            theta -= dtheta
            pen.setheading(theta)
        elif s == "[":
            positions.append({"x":xpos, "y":ypos, "theta": theta})
        elif s == "]":
            position = positions.pop()
            xpos, ypos, theta = position['x'], position['y'], position['theta']
            pen.up()
