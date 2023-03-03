#python program with tkinter

from tkinter import *
root = Tk()

frame = Frame(root)
Label(frame, text='Text To Finde : ').pack(side=LEFT)

edit = Entry(frame)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()

butt = Button(frame, text='Find Now')
butt.pack(side=RIGHT)
frame.pack(side=TOP)

text = Text(root)
text.insert('1.0','''Type your text here ... ''')
text.pack(side=BOTTOM)

def find():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx : break

            lastidx = '%s+%dc' % (idx, len(s))

            text.tag_add('found', idx, lastidx)
            idx = lastidx

        text.tag_config('found', background='#0084D5', foreground='#fff')
    edit.focus_set()
butt.config(command=find)

root.mainloop()
