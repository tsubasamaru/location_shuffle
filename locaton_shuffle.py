import tkinter
import random

def click_btn():
    label['text'] = random.choice(label_list)
    label.update()

def enter_bg(event):
    event.widget['bg'] = 'lightgreen'

def leave_bg(event):
    event.widget['bg'] = 'SystemButtonFace'


root = tkinter.Tk()
root.title('Location shuffle')
root.geometry('500x500')
cvs = tkinter.Canvas(root, width = 500, height = 500, bg = 'skyblue')
cvs.pack()

label = tkinter.Label(root, width = 20, text = '？？？？', font = ('Lucida Console', 20))
label.place(x = 100, y = 100)
label_list = ['KYOTO', 'BRIGTON', 'NEWYORK', 'SHANGHAI']

btn = tkinter.Button(root, width = 20, text = 'Button', font = ('Lucida Console', 20), command = click_btn)
btn.place(x = 100, y = 300)
btn.bind('<Enter>', enter_bg)
btn.bind('<Leave>', leave_bg)


root.mainloop()















