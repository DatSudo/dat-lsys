# `dat-lsys`

[L-System](https://jsantell.com/l-systems/) generator implemented in `Python3`.

## Usage

- Clone the repo and go to `src` directory

    ```bash
    git clone https://github.com/DatSudo/dat-lsys.git
    cd dat-lsys/src
    ```

- Run `dat-lsys.py`

    ```bash
    # Show usage
    python dat-lsys.py -h

    # Generate l-system
    python dat-lsys.py -l kc -n 6
    ```

- Args:
    * `-l, --lsystem [l-system name initials]`
        * `kc`: Koch curve
        * `dc`: Dragon curve
        * `st`: Sierpinski triangle
        * `fp`: Fractal plant
    * `-n --numgen [number of generations]`: Must be between 0 and 7 only. You might want to change that if you have a beefy PC.

## How L-system works

You need to have these three:
- **Alphabet/symbols.** Each symbol corresponds to some graphics movement such as "forward", "turn right", etc.
- **Axiom.** The initial state.
- **Rules.** Rules on how symbols will transform in each generation.

Example (Koch curve):
* **Symbols:** $F$, $+$, $-$
* **Axiom:** $F$
* **Rules:** $F \rightarrow F+F-F-F+F$

$$\begin{align*}
G=0 \rightarrow & F \\
G=1 \rightarrow & F+F−F−F+F \\
G=2 \rightarrow & F+F−F−F+\dots −F+F \\
\end{align*}$$

If we try to draw this with $F$ means "draw forward", $+$ means "turn left 90°", and $-$ means "turn right 90°":

![Koch curve at g = 2](assets/koch_at_2.png)

At $G=4$:

![Koch curve at g = 4](assets/koch_at_4.png)

### More examples:

Dragon Curve | Sierpinski Triangle | Fractal Plant
:-----------:|:-------------------:|:-------------:
![](assets/dragon_curve.png) | ![](assets/sier_tri.png) | ![](assets/fractal_plant.png)


## TODO
- [X] README
- [ ] GUI
- [ ] Documentation
- [ ] LICENSE
