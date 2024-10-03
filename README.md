[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.

Zero iteration conditions occur when the starting condition for a loop is always false, and thus the loop never executes in the first place. However, infinite loops occur when the starting condition for a loop is true and never becomes false, and thus, runs indefinitely. Zero-iteration conditions are useful for scenarios in which it is essential for initial loop conditions to not be met, and infinite loops are essential for continuous executions, which there often being internal mechanisms to break out of the loop.

Infinite loops: 
```python
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
```
Zero iteration conditions:
```python
for i in range(num_squares):
    fill_color = fill_colors[i % len(fill_colors)]
    border_color = border_colors[(i + 1) % len(border_colors)]
    # Drawing code
    size -= step
```
This loop won't run if num_squares is 0 in the draw_squares_with_borders function.

3. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.

```python
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
```

5. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.



https://github.com/user-attachments/assets/d5b848ec-ba74-4fab-a62a-37289144f923



Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)

Step 17:
```python
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

x = -200
y = 0
move_x = 1
move_y = 1

# First peak
while (x < 1):  # Moving towards the first peak
    while (y < 100):  # Going up the peak
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = -1  # Change direction to go down

    while (y > 0):  # Coming down
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = 1  # Reset to go up again

# Reset for the second peak
x = 0  # Move the starting point for the second peak
y = 0

# Second peak
while (x < 0):  # Moving towards the second peak
    while (y < 100):  # Going up the second peak
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = -1  # Change direction to go down

    while (y > 0):  # Coming down
        x = x + move_x
        y = y + move_y
        painter.goto(x, y)
    move_y = 1  # Reset for next peak (if needed)

# Keep the window open
wn = trtl.Screen()
wn.mainloop()
```
Step 18:
```python
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

def draw_rhombus(start_x, start_y):
    x = start_x
    y = start_y
    move_x = 100
    move_y = 100

    painter.goto(x + move_x, y + move_y)
    painter.goto(x + 2 * move_x, y)
    painter.goto(x + move_x, y - move_y)
    painter.goto(x, y)

draw_rhombus(-200, 0)

painter.penup()
painter.goto(0, 0)
painter.pendown()
painter.setheading(270)
draw_rhombus(0, 0)

wn = trtl.Screen()
wn.mainloop()
```
Step 19:
```python
import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

def draw_rhombus(start_x, start_y):
    x = start_x
    y = start_y
    move_x = 100
    move_y = 100

    painter.goto(x + move_x, y + move_y)
    painter.goto(x + 2 * move_x, y)
    painter.goto(x + move_x, y - move_y)
    painter.goto(x, y)

draw_rhombus(-200, 0)
painter.penup()
painter.goto(0, 0)
painter.pendown()
draw_rhombus(0, 0)

start_x = 200

while True:
    painter.penup()
    painter.goto(start_x, 0)
    painter.pendown()
    draw_rhombus(start_x, 0)
    start_x += 200

wn = trtl.Screen()
wn.mainloop()
```

6. Answer to step 21

This represents the program modified earlier in this activity to avoid a zero iteration condition and draw five circles.

8. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.

```python
import subprocess
import sys
from PIL import Image, ImageFilter
import turtle
import os
import random
import concurrent.futures
import re

def install_pillow():
    """Install the Pillow library using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])

# Call the function to install Pillow if not already installed
install_pillow()

print("Pillow installed successfully!")

def flower():
    """Prompt the user to enter the number and name of a single flower type."""
    while True:
        flower_sentence = input("Enter the number and name of the flower (e.g., '3 roses'): ")
        parsed_flowers = parse_flowers(flower_sentence)
        
        # Only allow one type of flower
        if len(parsed_flowers) == 1:
            flower_name = list(parsed_flowers.keys())[0]
            return flower_name.lower(), parsed_flowers[flower_name]
        else:
            print("Please enter a valid input with one type of flower (e.g., '3 roses').")

def parse_flowers(sentence):
    """Parse the sentence to extract the flower name and number."""
    pattern = r"(\d+)\s+(\w+)"
    matches = re.findall(pattern, sentence)
    return {flower: int(number) for number, flower in matches}

def pixelate_image_chunk(image, start_x, end_x, start_y, end_y, pixel_size):
    """Pixelate a chunk of the image."""
    chunk = image.crop((start_x, start_y, end_x, end_y))
    small_size = (chunk.width // pixel_size, chunk.height // pixel_size)
    chunk = chunk.resize(small_size, resample=Image.Resampling.NEAREST)
    chunk = chunk.resize((end_x - start_x, end_y - start_y), resample=Image.Resampling.NEAREST)
    return (start_x, start_y, chunk)

def combine_image_chunks(chunks, width, height):
    """Combine image chunks back into a single image."""
    combined_image = Image.new('RGB', (width, height))
    for (start_x, start_y, chunk) in chunks:
        combined_image.paste(chunk, (start_x, start_y))
    return combined_image

def pixelate_image(image_path, output_size=(7680, 4320), pixel_size=20):
    """Pixelate the image using parallel processing."""
    try:
        img = Image.open(image_path)
        img = img.resize(output_size, resample=Image.Resampling.LANCZOS)
        img = img.filter(ImageFilter.SMOOTH_MORE)  # Apply smoothing
    except IOError:
        print(f"Error opening image file: {image_path}")
        return None

    width, height = img.size
    chunks = []
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        chunk_width = width // 4
        chunk_height = height // 4
        for i in range(0, width, chunk_width):
            for j in range(0, height, chunk_height):
                end_x = min(i + chunk_width, width)
                end_y = min(j + chunk_height, height)
                futures.append(
                    executor.submit(
                        pixelate_image_chunk,
                        img,
                        i, end_x,
                        j, end_y,
                        pixel_size
                    )
                )

        for future in concurrent.futures.as_completed(futures):
            chunks.append(future.result())
    
    pixelated_image = combine_image_chunks(chunks, width, height)
    pixelated_image = pixelated_image.filter(ImageFilter.SMOOTH_MORE)  # Apply smoothing to the final image
    return pixelated_image

def rgb_to_hex(rgb):
    """Convert an RGB tuple to a HEX color string."""
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def draw_pixelated_image(image, pixel_size=20):
    """Draw a pixelated image using Turtle graphics."""
    width, height = image.size
    screen_width = min(width, 800)  # Limit screen width
    screen_height = min(height, 600)  # Limit screen height
    
    screen = turtle.Screen()
    screen.setup(width=screen_width, height=screen_height)
    screen.title("Pixelated Image Animation")
    screen.tracer(0)  # Turn off automatic screen updates for animation effect
    turtle.speed(0)  # Set the drawing speed to maximum
    turtle.hideturtle()
    
    turtle.setworldcoordinates(-width // 2, height // 2, width // 2, -height // 2)
    
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            pixel_color = image.getpixel((x, y))
            hex_color = rgb_to_hex(pixel_color)
            
            turtle.penup()
            turtle.goto(x - width // 2, height // 2 - y)
            turtle.pendown()
            
            turtle.fillcolor(hex_color)
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(pixel_size)
                turtle.right(90)
            turtle.end_fill()
            
            screen.update()

def pixellate(flower_name):
    """Pixelate a randomly chosen image from the specified flower folder."""
    base_folder_path = 'flowers'  # Replace with your base folder path
    
    flower_folders = {
        'tulip': 'tulip',
        'daisy': 'daisy',
        'dandelion': 'dandelion',
        'sunflower': 'sunflower',
        'rose': 'rose'
    }
    
    if flower_name not in flower_folders:
        print(f"Invalid flower name: {flower_name}")
        return None
    
    flower_folder_path = os.path.join(base_folder_path, flower_folders[flower_name])
    
    if not os.path.exists(flower_folder_path):
        print(f"Folder does not exist: {flower_folder_path}")
        return None
    
    files = os.listdir(flower_folder_path)
    
    if not files:
        print(f"No files found in the folder: {flower_folder_path}")
        return None
    
    random_file = random.choice(files)
    file_path = os.path.join(flower_folder_path, random_file)
    
    return pixelate_image(file_path)

def main():
    flower_name, flower_count = flower()
    print(f"Drawing {flower_count} {flower_name}(s)...")
    
    # Pixelate and draw the image multiple times based on the count
    for _ in range(flower_count):
        pixelated_img = pixellate(flower_name)
        if pixelated_img:
            draw_pixelated_image(pixelated_img)
    
    turtle.done()

if __name__ == "__main__":
    main()
```

10. Give an example of an undecidable problem, attach code.
ChatGPT gave the idea of a Halting Problem:
```python
def halting_function(program, input_value):
    try:
        exec(program)  # Executes the given program code
    except Exception as e:
        return "Program crashed or did not halt"

# Example program code as a string
program_code = """
def example_program():
    while True:
        pass  # This will run indefinitely

example_program()
"""

# Check if the example program halts
result = halting_function(program_code, None)
print(result)
```



