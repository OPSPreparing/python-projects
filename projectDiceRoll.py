import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roller")
def roll_dice():
    a = random.randint(1, 6)
    label = tk.Label(window, text=a).pack()
    
button = tk.Button(window, text="click", command=roll_dice)
button.pack()
dice = [1, 2, 3, 4, 5, 6]
# image = ImageTk.PhotoImage(Image.open("dice1.png"))

window.mainloop()

