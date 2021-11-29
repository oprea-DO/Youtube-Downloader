from pytube import YouTube
from tkinter import *

root=Tk()

root.geometry("500x300")
root.resizable(0,0)
root.title("Youtube - MP4/MP3")

Label(root, text = "Welcome to the Youtube - MP4/MP3 App").pack()
Label(root).pack()

link = StringVar()
Label(root, text = "Paste link here:").pack()
link_enter = Entry(root, width = 50, textvariable=link).pack()

def downloader():
  url = YouTube(str(link.get()))
  video = url.streams.first()
  video.download()
  Label(root, text = "Download successful").pack()

Button(root, command = downloader, text = "Download").pack

root.mainloop()
