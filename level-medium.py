
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

WIN_WIDTH = 1400
WIN_HEIGHT = 700
SCROLLING_SPEED = 10
root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
root.title('meduimLewel')
frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("imag/back-medium.png")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

pic_mario = tk.PhotoImage(file="imag/mario-jumper.png")
diamond= tk.PhotoImage(file="imag/daimond.png")
goomba= tk.PhotoImage(file="imag/goomba.png")
giant_stick= tk.PhotoImage(file="imag/giant.png")
heart= tk.PhotoImage(file="imag/heart.png")



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

diamond_count = 0

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
    


    print(canvas.coords(player))

scroll_bg_image()
player = canvas.create_image(100,550,image=pic_mario )
canvas.create_image(200,550,image=diamond )

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')



root.mainloop()