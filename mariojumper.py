
#===import==============================================

import tkinter as tk
from tkinter import *
import winsound
from PIL import Image, ImageTk
import random
from random import randrange, choice

keyPressed = []

#===Constan=============================================================

vertical_velocity = 0

WIN_WIDTH =1400
WIN_HEIGHT = 740
SPEED = 10

#  ============== Name Game ===============================================

root = tk.Tk()
root.geometry(str(WIN_WIDTH)+"x"+str(WIN_HEIGHT))
root.title('Mario Jumper')
canvas = tk.Canvas(root, scrollregion= (0,0,4000,5000)) 
frame = tk.Frame()

#====Variable=======================================================

game_page1 = tk.PhotoImage(file="img/page1.png")
game_lower = tk.PhotoImage(file="img/lower.png")

btn_introductio = tk.PhotoImage(file="img/btn_introduction.png")
btn_level = tk.PhotoImage(file="img/btn_level.png")
btn_play = tk.PhotoImage(file="img/btn_play.png")
btn_choose=tk.PhotoImage(file="img/btn_choose.png")
btn_lower= tk.PhotoImage(file="img/btn_lower.png")
btn_high= tk.PhotoImage(file="img/btn_high.png")
btn_meduim= tk.PhotoImage(file="img/btn_medium.png")

# ================ Background Game ======================================

game_over_image = tk.PhotoImage(file="img/game-over.png")
pic_mario = tk.PhotoImage(file="img/mario.png")
pic_giant = tk.PhotoImage(file="img/diamond.png")
pic_goomba = tk.PhotoImage(file="img/heart.png")
pic_introduction = tk.PhotoImage(file="img/introduction.png")
pic_level= tk.PhotoImage(file="img/level.png")
background_lower= tk.PhotoImage(file="img/lower.png")
background_high= tk.PhotoImage(file="img/high.png")
background_medium= tk.PhotoImage(file="img/medium.png")

diamond= tk.PhotoImage(file="img/diamond.png")
goomba= tk.PhotoImage(file="img/goomba.png")
giant_stick= tk.PhotoImage(file="img/Giant Stick.png")
heart= tk.PhotoImage(file="img/heart.png")

btn_back = tk.PhotoImage(file="img/btn_back.png")
#  ======start game ==================================================

isStart = True
isMario= 1
marioMeetenemy = 0
isGoomba =0
isGiantstick=0
level1 = 0
level2 =0

diamonds=[]
score = 0

diamonds = [] 

count_create_dm = 0
totaldm = 0
listOfDm = []
listOfLives = []
canLive = 0
toConfig = 0
isStart = True

#===Function==================================================================
 
def gameShow(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=game_page1)
    canvas.create_image(870,280, image=btn_introductio, tags="introduction")
    canvas.create_image(870,410,image=btn_level, tags="level")
    canvas.create_image(870,520 ,image=btn_play, tags ="play")
winsound.PlaySound("sound/first-background.wav", winsound.SND_ASYNC)

#===introduction==========================================================

def gameIntroduction(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=pic_introduction)
    canvas.create_image(120, 50, image=btn_back, tags="back")

#===lavel==================================================================

def gameLevel(event):
    canvas.delete("all")
    canvas.create_image(680, 372, image=pic_level)
    canvas.create_image(700,150, image=btn_choose, tags="choose")
    canvas.create_image(300,300, image=btn_lower, tags="lower")
    canvas.create_image(700,300, image=btn_high, tags="high")
    canvas.create_image(1100,300, image=btn_meduim, tags="medium")
    canvas.create_image(120, 50, image=btn_back, tags="back")

#================================ Lower Level ================================

def lowerLevel(event):
    global player
    canvas.delete("all")
    background_image_label_1= canvas.create_image(0, 0,anchor=tk.NW, image=background_lower)
    background_image_label_2= canvas.create_image(1400, 0,anchor=tk.NW, image=background_lower)

# ======================= Scroll screen ======================================

    def scroll_bg_image():
        
        canvas.move(background_image_label_1, -1, 0)
        canvas.move(background_image_label_2, -1, 0)

        if canvas.coords(background_image_label_1)[0]<-1400:
            canvas.coords(background_image_label_1, 1400, 0)
        elif canvas.coords(background_image_label_2)[0]<-1400:
            canvas.coords(background_image_label_2, 1400, 0)
        canvas.after(10, scroll_bg_image)
   
    scroll_bg_image()
    winsound.PlaySound("sound/game-show.wav", winsound.SND_ASYNC)
    player = canvas.create_image(100, 450, image=pic_mario)

# =============== Player Images =======================================================

player = canvas.create_image(100, 450, image=pic_mario)
diamonds = []
giant_sticks = []
game_over_screen = None
picked_up_diamonds = []  

# ===================== Create Daimond random ============================================

def create_dm():
    global diamonds, giant_sticks
    enemy_y = randrange(500, 655)
    speed_create = randrange(3000, 6000)
    dm_type = choice(["diamond", "giant_stick"])

    if dm_type == "diamond":
        dm = canvas.create_image(1350, enemy_y, image=diamond)
        diamonds.append(dm)
    elif dm_type == "giant_stick":
        dm = canvas.create_image(1350, enemy_y, image=giant_stick)
        giant_sticks.append(dm)

    move_dm(dm)
    canvas.after(speed_create, create_dm)

def delete_item(item):
    canvas.delete(item)

# ================= Move Pick Up Diamond ===================================

def move_dm(dm):
    global diamonds, giant_sticks, picked_up_diamonds
    canvas.move(dm, -5, 0)
    position_dm = canvas.coords(dm)
    position_player = canvas.coords(player)

    if len(position_dm) > 0:
        if (position_player[0] + 20 >= position_dm[0] and position_player[0] - 20 <= position_dm[0]) and (
                position_player[1] - 20 <= position_dm[1] + 20 and position_player[1] + 40 >= position_dm[1] - 20):
            if dm in diamonds:
                diamonds.remove(dm)
                picked_up_diamonds.append(dm)  
                print("Picked up a diamond!")
            elif dm in giant_sticks:
                giant_sticks.remove(dm)
                print("Picked up a giant stick!")
                game_over()

            delete_item(dm)
        elif position_dm[0] < 0:
            delete_item(dm)

    canvas.after(30, lambda: move_dm(dm))


#  ===================== Move Mario ====================================

def move(event):
    global diamonds, giant_sticks, picked_up_diamonds
    if event.keysym == "Left" and canvas.coords(player)[0] > 0:
        canvas.move(player, -10, 0)  
    elif event.keysym == "Right" and canvas.coords(player)[0] < canvas.winfo_width():
        canvas.move(player, 10, 0) 
    elif event.keysym == "Down" and canvas.coords(player)[1] < canvas.winfo_height():
        canvas.move(player, 0, 10)  
    elif event.keysym == "Up" and canvas.coords(player)[1] > 0:
        canvas.move(player, 0, -10) 

    player_coords = canvas.coords(player)
    for diamond in diamonds:
        diamond_coords = canvas.coords(diamond)
        if player_coords[0] == diamond_coords[0] and player_coords[1] == diamond_coords[1]:
            canvas.delete(diamond)  
            diamonds.remove(diamond)  
            picked_up_diamonds.append(diamond)  
            print("Picked up a diamond!")

    for giant_stick in giant_sticks:
        giant_stick_coords = canvas.coords(giant_stick)
        if player_coords[0] == giant_stick_coords[0] and player_coords[1] == giant_stick_coords[1]:
            canvas.delete(giant_stick)  
            giant_sticks.remove(giant_stick)  
            print("Picked up a giant stick!")
            game_over()

    print(canvas.coords(player))

# ============================== Game Over ===================================

def game_over():
    global game_over_screen
    canvas.delete(ALL)  
    canvas.create_image(0, 0, anchor=NW, image=game_over_image) 
    canvas.unbind("<Key>")
    canvas.after(2000, root.quit) 
    winsound.PlaySound("sound/game-lose.wav", winsound.SND_ASYNC)

# ================== Count Diamond ==========================================

def count_diamonds():
    global picked_up_diamonds
    print("Diamonds picked up:", len(picked_up_diamonds))

root.bind("<Key>", move)

create_dm()
