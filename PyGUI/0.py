import tkinter 

#create a main window
root = tkinter.Tk()

#create a label with text
label = tkinter.Label(root, text="确认购买此商品？")
#pack the label into the window
label.pack()

#create a button
button1 = tkinter.Button(root, text="确认")
#pack the button into the window
button1.pack(side=tkinter.LEFT)

#create another button
button2 = tkinter.Button(root, text="取消")
#pack the button into the window
button2.pack(side=tkinter.RIGHT)

root.mainloop()