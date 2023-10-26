
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
