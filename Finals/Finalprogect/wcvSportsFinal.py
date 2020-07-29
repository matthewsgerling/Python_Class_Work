# Name: Matthew Gerling
# File: wcvSportsFinal

# INFO: The three different inputs are baseball softball and high school
# this website is fairly new and does not hold alot of information

from tkinter import *
from Finals.Finalprogect.vimeoApp import VimeoAPI

tk = Tk()
vimeo = VimeoAPI()

frame = Frame(tk)

Label(frame, text='Search For:').pack(side=LEFT)
edit = Entry(frame)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
search = Button(frame, text='Search')
search.pack(side=RIGHT)
frame.pack(side=TOP)

display = Text(tk)

display.pack(side=BOTTOM)


def find():
    folder = edit.get()
    videos = vimeo.list_folder(folder)

    display.insert('1.0', videos)
    edit.focus_set()


search.config(command=find)
tk.mainloop()
