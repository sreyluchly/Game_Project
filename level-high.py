
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random 

WIN_WIDTH = 1400
WIN_HEIGHT = 700
SCROLLING_SPEED = 10
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
root.title('highLevel')
frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("imag/back-high.png")

pic_mario = tk.PhotoImage(file="imag/mario-jumper.png")
pic_diamond= tk.PhotoImage(file="imag/daimond.png")
goomba= tk.PhotoImage(file="imag/goomba.png")
giant_stick= tk.PhotoImage(file="imag/giant.png")
heart= tk.PhotoImage(file="imag/heart.png")

diamonds = [] 

image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_image)
background_image_label_2= canvas.create_image(WIN_WIDTH, 0,anchor=tk.NW, image=background_image)

def scroll_bg_image():
    
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)

    if canvas.coords(background_image_label_1)[0]< -1400:
        canvas.coords(background_image_label_1, 1400, 0)
    elif canvas.coords(background_image_label_2)[0]< -1400:
        canvas.coords(background_image_label_2, 1400, 0)
    canvas.after(5, scroll_bg_image)

player = canvas.create_image(100, 350, image=pic_mario)

def move(event):
    global diamonds
    if event.keysym == "Left" and canvas.coords(player)[0] > 0:
        canvas.move(player, -10, 0)  # Move left (-10 in the x-axis)
    elif event.keysym == "Right" and canvas.coords(player)[0] < canvas.winfo_width():
        canvas.move(player, 10, 0)  # Move right (10 in the x-axis)
    elif event.keysym == "Down" and canvas.coords(player)[1] < canvas.winfo_height():
        canvas.move(player, 0, 10)  # Move down (10 in the y-axis)
    elif event.keysym == "Up" and canvas.coords(player)[1] > 0:
        canvas.move(player, 0, -10)  # Move up (-10 in the y-axis)

    player_coords = canvas.coords(player)
    for diamond in diamonds:
        diamond_coords = canvas.coords(diamond)
        if player_coords[0] == diamond_coords[0] and player_coords[1] == diamond_coords[1]:
            canvas.delete(diamond)  # Remove the picked up diamond from the canvas
            diamonds.remove(diamond)  # Remove the picked up diamond from the list
            print("Picked up a diamond!")
            # Update the diamond count
            diamond_count = len(diamonds)
            print("Remaining diamonds:", diamond_count)

    print(canvas.coords(player))

def create_diamond():
    x = 500  # X-coordinate of the diamond
    y = 400  # Y-coordinate of the diamond
    diamond = canvas.create_image(x, y, image=pic_diamond)
    diamonds.append(diamond)

root.bind("<Key>", move)
scroll_bg_image()


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

for _ in range(5):
    create_diamond()

root.mainloop()