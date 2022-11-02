import turtle as t

t.speed("fast")

def small_line(x):
    t.forward(x)
    t.left(90)


def small_square(x, color):
    t.color(color)
    t.begin_fill()
    small_line(x)
    small_line(x)
    small_line(x)
    small_line(x)
    t.end_fill()
    t.color("black")
    t.forward(x)

def single_row(x, turn):
    small_square(x, "black")
    small_square(x, "white")
    small_square(x, "black")
    small_square(x, "white")
    small_square(x, "black")
    small_square(x, "white")
    small_square(x, "black")
    small_square(x, "white")
    if turn == "left":
        t.left(90)
        t.forward(x*2)
        t.left(90)
    else:
        t.left(90)
        t.forward(x)
        t.left(180)
        t.forward(x)
        t.right(90)

def make_chessboard(x=20):
    single_row(x, "left")
    single_row(x, "right")
    single_row(x, "left")
    single_row(x, "right")
    single_row(x, "left")
    single_row(x, "right")
    single_row(x, "left")
    single_row(x, "right")


make_chessboard()
t.done()