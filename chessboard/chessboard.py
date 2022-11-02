import turtle

chessboard_width = 200

def create_small_line(length):
    turtle.forward(length)
    turtle.left(90)

def create_box(width, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    create_small_line(width)
    create_small_line(width)
    create_small_line(width)
    create_small_line(width)
    turtle.end_fill()
    turtle.forward(width)

def create_entire_line_odd(total_width):
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    turtle.left(90)
    turtle.forward(total_width / 8)
    turtle.left(90)
    turtle.forward(total_width)
    turtle.left(180)

def create_entire_line_even(total_width):
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    create_box(total_width / 8, "white")
    create_box(total_width / 8, "black")
    turtle.left(90)
    turtle.forward(total_width / 8)
    turtle.left(90)
    turtle.forward(total_width)
    turtle.left(180)

def draw_chessboard(width):
    create_entire_line_even(width)
    create_entire_line_odd(width)
    create_entire_line_even(width)
    create_entire_line_odd(width)
    create_entire_line_even(width)
    create_entire_line_odd(width)
    create_entire_line_even(width)
    create_entire_line_odd(width)


draw_chessboard(chessboard_width)

turtle.done()