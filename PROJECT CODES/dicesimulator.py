from tkinter import*
import random
root=Tk()
root.title("Roll Dice")
root.geometry("500x550")
label1 = Label(root,font = ('',250,'bold'),text="")
def rolldice():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label1.configure(text = f'{random.choice(dice)}')
    label1.pack()
button = Button(root,font = ('',35,'bold'),text="roll dice", command = rolldice)
button.pack()
root.mainloop()
