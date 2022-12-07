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
