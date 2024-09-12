import turtle
import random

def draw_filled_square(turtle_obj, size, fill_color):
    turtle_obj.fillcolor(fill_color)
    turtle_obj.begin_fill()
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)
    turtle_obj.end_fill()

def draw_square_border(turtle_obj, size, border_color, border_thickness):
    # Draws the border of a square with the specified color and thickness.
    turtle_obj.color(border_color)
    turtle_obj.pensize(border_thickness)
    turtle_obj.penup()
    turtle_obj.goto(-size / 2, size / 2)  # Moves to the starting position.
    turtle_obj.pendown()
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)
    turtle_obj.pensize(1)  # Resets pen size to default size.

def draw_squares_with_borders(turtle_obj, num_squares, base_size, step):
    # Draws a series of squares with varying sizes, filled colors, and borders.
    size = base_size + (num_squares - 1) * step
    fill_colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "brown"]
    border_colors = ["black", "grey", "white", "darkblue", "darkgreen", "darkred", "darkorange", "darkviolet", "darkcyan", "darkbrown"]

    turtle_obj.penup()
    turtle_obj.goto(-size / 2, size / 2)
    turtle_obj.pendown()
    random_fill_color = (random.random(), random.random(), random.random())  # Randomized color for fills of each concentric square.
    draw_filled_square(turtle_obj, size, random_fill_color)
    draw_square_border(turtle_obj, size + step, border_colors[0], 3)

    # Draws concentric squares with specified fill and border colors
    for i in range(num_squares):
        fill_color = fill_colors[i % len(fill_colors)]  # Cycles through different fill colors
        border_color = border_colors[(i + 1) % len(border_colors)]  # Cycles through different border colors.
        turtle_obj.penup()
        turtle_obj.goto(-size / 2, size / 2)
        turtle_obj.pendown()
        draw_filled_square(turtle_obj, size, fill_color)
        draw_square_border(turtle_obj, size + step, border_color, 3)
        size -= step  # Decrease the size for the next square

def main():
    # Sets up the screen, and then draws the squares.
    screen = turtle.Screen()
    screen.bgcolor("white")

    drawer = turtle.Turtle()
    drawer.speed(0)  # Sets the drawing speed to the fastest possible speed.

    # Get user input for the number of squares
    while True:
        try:
            num_squares = int(input("Enter the number of squares to draw (between 1 and 15): "))
            if num_squares <= 0:
                print("Please enter a positive integer between 1 and 15.")
            elif num_squares > 15:
                print("Please enter a positive integer between 1 and 15.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    draw_squares_with_borders(drawer, num_squares, 20, 30)  # Draw the squares based on user input of how many to draw.

    drawer.hideturtle()  # Hides the turtle after drawing.
    turtle.done()

if __name__ == "__main__":
    main()
