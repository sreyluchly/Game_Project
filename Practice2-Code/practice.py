
import tkinter as tk

def jump_animation():
    global y_position, y_velocity

    # Update the position based on the velocity
    y_position -= y_velocity
    y_velocity -= gravity

    # Check if the object has reached the ground
    if y_position >= ground_level:
        y_position = ground_level
        y_velocity = initial_velocity

    # Update the object's position on the canvas
    canvas.coords(object_id, x_position, y_position)

    # Schedule the next animation frame
    root.after(animation_speed, jump_animation)

# Create the Tkinter window
root = tk.Tk()
root.title("Jump Animation")

# Create the canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Set up the initial variables
x_position = 200
y_position = 200
y_velocity = 10
gravity = 1
ground_level = 200
initial_velocity = 10
animation_speed = 50

# Create the object on the canvas
object_id = canvas.create_oval(x_position - 10, y_position - 10, x_position + 10, y_position + 10, fill="blue")

# Start the animation loop
jump_animation()

# Run the Tkinter event loop
root.mainloop()