from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App:

    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        self.entry = ttk.Entry(self.master, width=44, font=('StSong', 14), foreground='green')
        self.entry.pack(fill=BOTH, expand=YES)
        self.text = Text(self.master, width=44, height=4, font=('StSong', 14),foreground='gray')
        self.text.pack(fill=BOTH, expand=YES)
        f = Frame(self.master)
        f.pack()
        ttk.Button(f, text='开始插入', command=self.insert_start).pack(side=LEFT)
        ttk.Button(f, text='编辑处插入', command=self.insert_edit).pack(side=LEFT)
        ttk.Button(f, text='结尾插入', command=self.insert_end).pack(side=LEFT)
        ttk.Button(f, text='获取Entry', command=self.get_entry).pack(side=LEFT)
        ttk.Button(f, text='获取Text', command=self.get_text).pack(side=LEFT)

    def insert_start(self):
        self.entry.insert(0, 'Kotlin')
        self.text.insert(1.0, 'Kotlin')
    
    def insert_edit(self):
        self.entry.insert(INSERT, 'Python')
        self.text.insert(INSERT, 'Python')

    def insert_end(self):
        self.entry.insert(END, 'Swift')
        self.text.insert(END, 'Swift')

    def get_entry(self):
        messagebox.showinfo(title='输入内容', message=self.entry.get())
    
    def get_text(self):
        messagebox.showinfo(title='输入内容', message=self.text.get(1.0, END))

root = Tk()
root.title("开始测试")
App(root)
root.mainloop()
