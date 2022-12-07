from lsystem import LSystem

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
