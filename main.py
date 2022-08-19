from tkinter import *
from pytube import YouTube

window= Tk()
window.geometry('500x300')
window.resizable(0, 0)
window.title('youtube downloader')

Label(window, text="Downloader", font='san-serif 14 bold').pack()
link = StringVar()
Label(window, text="LINK", font='san-serif 15').place(x=150, y=55)
link_enter = Entry(window, width=70, textvariable=link).place(x=30, y=85)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text="Downloaded", font="san-serif 15").place(x=100, y=120)

Button(window, text='Download', font='san-serif 16 bold', bg='yellow', padx=2,command=download).place(x=170, y=150)

window.mainloop()
