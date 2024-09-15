from tkinter import *

root = Tk()
root.title("hello world")
root.geometry("300x200")

Label(root, text="阿里旗下四大品牌",font=('Arial',20)).pack()

#生成中间边框
frm = Frame(root)
#left


#生成左边边框
frm_L = Frame(frm)
Label(frm_L, text="淘宝", font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text="天猫", font=('Arial', 15)).pack(side=TOP)
#打包左边边框
frm_L.pack(side=LEFT)

#生成右边边框
frm_R = Frame(frm)
Label(frm_R, text="支付宝", font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text="阿里云", font=('Arial', 15)).pack(side=TOP)
#打包右边边框
frm_R.pack(side=RIGHT)

#打包中间边框
frm.pack()

root.mainloop()