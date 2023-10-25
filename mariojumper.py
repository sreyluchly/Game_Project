
# # ================== Game jump ==============


# import tkinter as tk
# from tkinter import *
# from PIL import Image, ImageTk


# WIN_WIDTH = 1400
# WIN_HEIGHT = 740
# SPEED = 7

# #  ===========Key move =================================================================
# keyPressed = []
# # Define the player's vertical velocity
# vertical_velocity = 0

# root = tk.Tk()
# root.title("Mario Jumper")
# root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
# frame = tk.Frame()
# canvas = tk.Canvas(frame)
# original_image = Image.open("imag/Background.png")

# # ================ images element game =================================================

# pic_diamond = tk.PhotoImage(file="imag/daimond.png")
# pic_giant = tk.PhotoImage(file="imag/giant.png")
# player_mario = tk.PhotoImage(file="imag/mario-jumper.png")

# image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
# background_image = ImageTk.PhotoImage(image_resize)

# # ================= Screen auto scroll ===================================================

# background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
# background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=background_image)

# #  =============== player mario ===========================================================

# player = canvas.create_image(100, 350, image=player_mario)

# # stay = canvas.create_rectangle(100, 650, 500, 700, fill="red", outline="red")
# #  =============== store daimond ==========================================================

# diamonds = []  
# diamond_count = 0  

# diamond_count_label = tk.Label(root, text="Diamonds: 0", font=("Arial", 16))
# diamond_count_label.place(x=WIN_WIDTH - 180, y=30)

# #  =============== enemy kill mario =======================================================

# enemy = canvas.create_image(1200, 510, image=pic_giant)

# #  ========================== Scroll ======================================================

# def scroll_bg_image():
#     canvas.move(background_image_label_1, -1, 0)
#     canvas.move(background_image_label_2, -1, 0)

#     if canvas.coords(background_image_label_1)[0] < -1400:
#         canvas.coords(background_image_label_1, 1400, 0)
#     elif canvas.coords(background_image_label_2)[0] < -1400:
#         canvas.coords(background_image_label_2, 1400, 0)
#     canvas.after(5, scroll_bg_image)

# #  ================ Creat daimond ===========================================================

# def create_diamond(x, y):
#     diamond = canvas.create_image(x, y, image=pic_diamond)
#     diamonds.append(diamond)
# diamond_positions = [(670, 700), (750, 570), (830, 520), (930, 470), (1000, 470), (1170, 470)]
# for position in diamond_positions:
#     create_diamond(position[0], position[1])

# #  ==================== player move =========================================================
# def move_player():
#     global vertical_velocity

#     x, y = canvas.coords(player)

#     # Jumping logic
#     if 'space' in keyPressed and y >= WIN_HEIGHT:  # Adjust the condition as needed
#         vertical_velocity = -10  # Adjust the jump strength as needed

#     # Apply gravity
#     vertical_velocity += 0.5  # Adjust the gravity strength as needed
#     canvas.move(player, 0, vertical_velocity)

#     # Rest of the movement logic
#     if 'Left' in keyPressed and x > 0:
#         canvas.move(player, -SPEED, 0)
#     if 'Right' in keyPressed and x < WIN_WIDTH:
#         canvas.move(player, SPEED, 0)
#     if 'Down' in keyPressed and y < WIN_HEIGHT:
#         canvas.move(player, 0, SPEED)
#     if 'Up' in keyPressed and y > 0:
#         canvas.move(player, 0, -SPEED)

#     canvas.after(20, move_player)

# # ==================== Check daimond for pick up ===========================================
# def check_collision():
#     global diamond_count
#     player_coords = canvas.coords(player)
#     for diamond in diamonds:
#         diamond_coords = canvas.coords(diamond)
#         if (player_coords[0] < diamond_coords[0] + 40 and player_coords[0] + 40 > diamond_coords[0] and
#                 player_coords[1] < diamond_coords[1] + 40 and player_coords[1] + 40 > diamond_coords[1]):
#             canvas.delete(diamond)
#             diamonds.remove(diamond)
#             diamond_count += 1
#             diamond_count_label.config(text="Diamonds: " + str(diamond_count))
#             print("Diamond collected!")

#     canvas.after(10, check_collision)

# #  =============== Key for move mario ========================================================

# def on_key_press(event):
#     if event.keysym == 'Left':
#         keyPressed.append('Left')
#     elif event.keysym == 'Right':
#         keyPressed.append('Right')
#     elif event.keysym == 'Down':
#         keyPressed.append('Down')
#     elif event.keysym == 'Up':
#         keyPressed.append('Up')
#     elif event.keysym == 'space':  # Add this condition for the space key
#         keyPressed.append('space')

# def on_key_release(event):
#     if event.keysym == 'Left' and 'Left' in keyPressed:
#         keyPressed.remove('Left')
#     elif event.keysym == 'Right' and 'Right' in keyPressed:
#         keyPressed.remove('Right')
#     elif event.keysym == 'Down' and 'Down' in keyPressed:
#         keyPressed.remove('Down')
#     elif event.keysym == 'Up' and 'Up' in keyPressed:
#         keyPressed.remove('Up')
#     elif event.keysym == 'space' and 'space' in keyPressed:  # Add this condition for the space key
#         keyPressed.remove('space')
# #  ========================= Daimond display ===============================================



# scroll_bg_image()
# move_player()
# check_collision()

# canvas.bind("<KeyPress>", on_key_press)
# canvas.bind("<KeyRelease>", on_key_release)
# canvas.focus_set()

# canvas.pack(expand=True, fill='both')
# frame.pack(expand=True, fill='both')

# root.mainloop()





import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


WIN_WIDTH = 1400
WIN_HEIGHT = 740
SPEED = 7


#  ===========Key move =================================================================
keyPressed = []
# Define the player's vertical velocity
vertical_velocity = 0

root = tk.Tk()
root.title("Mario Jumper")
root.geometry(str(WIN_WIDTH) + "x" + str(WIN_HEIGHT))
frame = tk.Frame()
canvas = tk.Canvas(frame)
original_image = Image.open("imag/Background.png")

# ================ images element game =================================================

game_over = tk.PhotoImage(file="imag/over-game.png")

pic_diamond = tk.PhotoImage(file="imag/daimond.png")
pic_life = tk.PhotoImage(file="imag/heart.png")
pic_giant = tk.PhotoImage(file="imag/giant.png")
player_mario = tk.PhotoImage(file="imag/mario-jumper.png")

image_resize = original_image.resize((WIN_WIDTH, WIN_HEIGHT))
background_image = ImageTk.PhotoImage(image_resize)

# ================= Screen auto scroll ===================================================

background_image_label_1 = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
background_image_label_2 = canvas.create_image(WIN_WIDTH, 0, anchor=tk.NW, image=background_image)

#  =============== player mario ===========================================================

player = canvas.create_image(100, 350, image=player_mario)

#  =============== store daimond ==========================================================
isStart = True
diamonds = []  

diamond_count = 0  


diamond_count_label = tk.Label(root, text="Diamonds: 0", font=("Arial", 16))
diamond_count_label.place(x=WIN_WIDTH - 180, y=20)


#  =============== enemy kill mario =======================================================

enemy = canvas.create_image(1200, 510, image=pic_giant)

#  ========================== Scroll ======================================================

def scroll_bg_image():
    canvas.move(background_image_label_1, -1, 0)
    canvas.move(background_image_label_2, -1, 0)

    if canvas.coords(background_image_label_1)[0] < -1400:
        canvas.coords(background_image_label_1, 1400, 0)
    elif canvas.coords(background_image_label_2)[0] < -1400:
        canvas.coords(background_image_label_2, 1400, 0)
    canvas.after(5, scroll_bg_image)

#  ================ Creat daimond ===========================================================
def create_diamond(x, y):
    diamond = canvas.create_image(x, y, image=pic_diamond)
    diamonds.append(diamond)
diamond_positions = [(670, 700), (750, 570), (830, 520), (930, 470), (1000, 470), (1170, 470)]
for position in diamond_positions:
    create_diamond(position[0], position[1])

#  ==================== player move =========================================================

enemy = canvas.create_image(1200, 600, image=pic_giant)
def move_player():
    global vertical_velocity

    x, y = canvas.coords(player)

    # Jumping logic==========================================================

    if 'space' in keyPressed and y >= WIN_HEIGHT:  
        vertical_velocity = -10  

    # Apply gravity==========================================================

    vertical_velocity += 0.5 
    canvas.move(player, 0, vertical_velocity)

    # step move =============================================================

    if 'Left' in keyPressed and x > 0:
        canvas.move(player, -SPEED, 0)
    if 'Right' in keyPressed and x < WIN_WIDTH:
        canvas.move(player, SPEED, 0)
    if 'Down' in keyPressed and y < WIN_HEIGHT:
        canvas.move(player, 0, SPEED)
    if 'Up' in keyPressed and y > 0:
        canvas.move(player, 0, -SPEED)

    giant_coords = canvas.coords(enemy)
    if (x < giant_coords[0] + 40 and x + 40 > giant_coords[0] and
            y + vertical_velocity < giant_coords[1] + 40 and y + vertical_velocity + 40 > giant_coords[1]):
        gameOver()

    canvas.after(20, move_player)

def check_collision():
    global diamond_count
    player_coords = canvas.coords(player)
    for diamond in diamonds:
        diamond_coords = canvas.coords(diamond)
        if (player_coords[0] < diamond_coords[0] + 40 and player_coords[0] + 40 > diamond_coords[0] and
                player_coords[1] < diamond_coords[1] + 40 and player_coords[1] + 40 > diamond_coords[1]):
            canvas.delete(diamond)
            diamonds.remove(diamond)
            diamond_count += 1
            diamond_count_label.config(text="Diamonds: " + str(diamond_count))
            print("Diamond collected!")
  
    canvas.after(10, check_collision)

#  ============== Key for move mario ========================================================

def gameOver():
    global isStart
    isStart = False
    canvas.delete("all")
    canvas.create_image(WIN_WIDTH // 2, WIN_HEIGHT // 2, anchor="center", image=game_over)
  
def on_key_press(event):
    if event.keysym == 'Left':
        keyPressed.append('Left')
    elif event.keysym == 'Right':
        keyPressed.append('Right')
    elif event.keysym == 'Down':
        keyPressed.append('Down')
    elif event.keysym == 'Up':
        keyPressed.append('Up')
    elif event.keysym == 'space':  
        keyPressed.append('space')

def on_key_release(event):
    if event.keysym == 'Left' and 'Left' in keyPressed:
        keyPressed.remove('Left')
    elif event.keysym == 'Right' and 'Right' in keyPressed:
        keyPressed.remove('Right')
    elif event.keysym == 'Down' and 'Down' in keyPressed:
        keyPressed.remove('Down')
    elif event.keysym == 'Up' and 'Up' in keyPressed:
        keyPressed.remove('Up')
    elif event.keysym == 'space' and 'space' in keyPressed:   
        keyPressed.remove('space')

scroll_bg_image()
move_player()
check_collision()


canvas.bind("<KeyPress>", on_key_press)
canvas.bind("<KeyRelease>", on_key_release)
canvas.focus_set()

canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')

root.mainloop()





