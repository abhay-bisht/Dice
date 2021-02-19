from tkinter import *
import random
root=Tk()
root.title("ROOL THE DICE ")
root.geometry("500x500")
root.configure(bg="steelblue")
root.wm_iconbitmap("drive.ico")
label= Label(root,font="helvetica 200 bold",text="")
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f"{random.choice(dice)}",bg='thistle')
    label.pack()
Button(root,text=":_press to roll_:",command=roll,font="helvetica 20 bold",bg='lime').pack(side=TOP,pady=40)
root.mainloop()