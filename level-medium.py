

# # ===================================================================

# import tkinter as tk
# from tkinter import *
# from PIL import Image, ImageTk
# import random

# WIN_WIDTH = 1400
# WIN_HEIGHT = 700
# SCROLLING_SPEED = 10
# ENEMY_SPEED = 5

# root = tk.Tk()
# root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
# root.title('lowerLevel')
# frame = tk.Frame()
# canvas = tk.Canvas(frame)
# pic_mario = tk.PhotoImage(file="imag/mario-jumper.png")
# pic_goomba = tk.PhotoImage(file="imag/goomba.png")
# pic_giant_stick = tk.PhotoImage(file="imag/giant.png")
# pic_game_over = tk.PhotoImage(file="imag/over-game.png")

# original_image = Image.open("imag/back-medium.png")
# image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
# background_image = ImageTk.PhotoImage(image_resize)
# background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
# background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=background_image)

# player = canvas.create_image(100, 500, image=pic_mario)

# enemies = []

# def create_enemy():
#     x = WIN_WIDTH + 100
#     y = random.randint(100, WIN_HEIGHT - 100)
#     enemy_type = random.choice(["goomba", "giant_stick"])
#     if enemy_type == "goomba":
#         enemy_image = pic_goomba
#         enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
#     elif enemy_type == "giant_stick":
#         enemy_image = pic_giant_stick
#         enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
#     enemies.append((enemy, enemy_type))
#     canvas.after(random.randint(2000, 5000), create_enemy)

# def move_enemies():
#     for enemy, enemy_type in enemies:
#         if enemy_type == "goomba":
#             canvas.move(enemy, -ENEMY_SPEED, 0)
#         elif enemy_type == "giant_stick":
#             canvas.move(enemy, -ENEMY_SPEED - 2, 0)
#         enemy_coords = canvas.coords(enemy)
#         player_coords = canvas.coords(player)
#         if collision_check(enemy_coords, player_coords):
#             game_over()
#             return
#         if enemy_coords[0] < -100:
#             canvas.delete(enemy)
#             enemies.remove((enemy, enemy_type))
#     canvas.after(30, move_enemies)

# def collision_check(coords1, coords2):
#     x1, y1 = coords1
#     x2, y2 = coords2
#     if abs(x1 - x2) < 50 and abs(y1 - y2) < 50:
#         return True
#     return False

# def scroll_bg_image():
#     canvas.move(background_image_label_1, -1, 0)
#     canvas.move(background_image_label_2, -1, 0)
    
#     if canvas.coords(background_image_label_1)[0] < -1400:
#         canvas.coords(background_image_label_1, 1400, 0)
#     elif canvas.coords(background_image_label_2)[0] < -1400:
#         canvas.coords(background_image_label_2, 1400, 0)

#     canvas.after(5, scroll_bg_image)

# def move(event):
#     player_coords = canvas.coords(player)
#     if event.keysym == "Left" and player_coords[0] > 0:
#         canvas.move(player, -10, 0)  # Move left (-10 in the x-axis)
#     elif event.keysym == "Right" and player_coords[0] < canvas.winfo_width():
#         canvas.move(player, 10, 0)  # Move right (10 in the x-axis)
#     elif event.keysym == "Down" and player_coords[1] < canvas.winfo_height():
#         canvas.move(player, 0, 10)  # Move down (10 in the y-axis)
#     elif event.keysym == "Up" and player_coords[1] > 0:
#         canvas.move(player, 0, -10)  # Move up (-10 in the y-axis)

# root.bind("<Key>", move)
# scroll_bg_image()
# create_enemy()
# move_enemies()

# def game_over():
#     canvas.delete(player)
#     canvas.unbind("<Key>")
#     canvas.itemconfig(background_image_label_1, image=pic_game_over)
#     canvas.itemconfig(background_image_label_2, image=pic_game_over)

# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')
# root.mainloop()


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import random

WIN_WIDTH = 1400
WIN_HEIGHT = 700
SCROLLING_SPEED = 10
ENEMY_SPEED = 5


root = tk.Tk()
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
root.title('lowerLevel')
frame = tk.Frame()
canvas = tk.Canvas(frame)

#  ==================== Images Enemy ============================

pic_mario = tk.PhotoImage(file="imag/mario-jumper.png")
pic_goomba = tk.PhotoImage(file="imag/goomba.png")
pic_giant_stick = tk.PhotoImage(file="imag/giant.png")
pic_game_over = tk.PhotoImage(file="imag/over-game.png")
pic_diamond = tk.PhotoImage(file="imag/daimond.png")

# =================== Back Ground ==========================

original_image = Image.open("imag/back-medium.png")
image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)
background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=background_image)

# ================== Play Game =============================

player = canvas.create_image(100, 500, image=pic_mario)

enemies = []
game_over_flag = False  

diamond_count = tk.IntVar()
diamond_count_label = tk.Label(root, textvariable=diamond_count)
diamond_count_label.place(x=10, y=10)


# ============= Create Enemy ================================

def create_enemy():
    if not game_over_flag: 
        x = WIN_WIDTH + 100
        y = random.randint(100, WIN_HEIGHT - 100)
        enemy_type = random.choice(["goomba", "giant_stick", "diamond"])  
        if enemy_type == "goomba":
            enemy_image = pic_goomba
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        elif enemy_type == "giant_stick":
            enemy_image = pic_giant_stick
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        elif enemy_type == "diamond": 
            enemy_image = pic_diamond
            enemy = canvas.create_image(x, y, image=enemy_image, tags="enemy")
        enemies.append((enemy, enemy_type))
        canvas.after(random.randint(2000, 5000), create_enemy)

#  ============ Move Enemy ================================

def move_enemies():
    if not game_over_flag:  
        for enemy, enemy_type in enemies:
            if enemy_type == "goomba":
                canvas.move(enemy, -ENEMY_SPEED, 0)
            elif enemy_type == "giant_stick":
                canvas.move(enemy, -ENEMY_SPEED - 2, 0)
            elif enemy_type == "diamond":  
                canvas.move(enemy, -ENEMY_SPEED, 0)
            enemy_coords = canvas.coords(enemy)
            player_coords = canvas.coords(player)
            if collision_check(enemy_coords, player_coords):
                if enemy_type == "diamond": 
                    canvas.delete(enemy)
                    enemies.remove((enemy, enemy_type))
                    
                    diamond_count.set(diamond_count.get() + 1)
                else:
                    game_over()
                    return
            if enemy_coords[0] < -100:
                canvas.delete(enemy)
                enemies.remove((enemy, enemy_type))
        canvas.after(30, move_enemies)

# ============= Check position Enemy ==============================

def collision_check(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    if abs(x1 - x2) < 50 and abs(y1 - y2) < 50:
        return True
    return False

# ============= Sroll Screen ======================================

def scroll_bg_image():
    if not game_over_flag:  
        canvas.move(background_image_label_1, -1, 0)
        canvas.move(background_image_label_2, -1, 0)

        if canvas.coords(background_image_label_1)[0] < -1400:
            canvas.coords(background_image_label_1, 1400, 0)
        elif canvas.coords(background_image_label_2)[0] < -1400:
            canvas.coords(background_image_label_2, 1400, 0)

        canvas.after(5, scroll_bg_image)

# ====================== Key Player move ============================

def move(event):
    if not game_over_flag: 
        player_coords = canvas.coords(player)
        if event.keysym == "Left" and player_coords[0] > 0:
            canvas.move(player, -10, 0) 
        elif event.keysym == "Right" and player_coords[0] < canvas.winfo_width():
            canvas.move(player, 10, 0) 
        elif event.keysym == "Down" and player_coords[1] < canvas.winfo_height():
            canvas.move(player, 0, 10) 
        elif event.keysym == "Up" and player_coords[1] > 0:
            canvas.move(player, 0, -10) 

# ============ Game Over ====================================

def game_over():
    global game_over_flag
    game_over_flag = True
    canvas.delete(player)
    canvas.unbind("<Key>")
    canvas.itemconfig(background_image_label_1, image=pic_game_over)
    canvas.itemconfig(background_image_label_2, image=pic_game_over)

root.bind("<Key>", move)
scroll_bg_image()
create_enemy()
move_enemies()

# ============= Key Move ======================

root.bind("<Key>", move)
scroll_bg_image()


canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
root.mainloop()