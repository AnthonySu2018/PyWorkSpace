import tkinter

root = tkinter.Tk()

button1 = tkinter.Button(root, anchor = tkinter.E, text="购物车", width = 30, height = 7)
button1.pack()

button2 = tkinter.Button(root, anchor = tkinter.E, text="收藏", bg = 'blue')
button2.pack()

button3 = tkinter.Button(root, text='直接购买', width = 12, height=1)
button3.pack()

button4 = tkinter.Button(root, text='关注', width = 40, height = 7, state = tkinter.DISABLED)
button4.pack()

root.mainloop()