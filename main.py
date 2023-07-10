from pytube import YouTube
from tkinter import *
import os


def Download_link():
    a = txtfld.get()
    print(a)
    yt = YouTube(a)
    ys = yt.streams.get_highest_resolution()
    destination = '.'

    # download the file
    out_file = ys.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")



def DownloadAudio():
    a = txtfld.get()
    print(a)
    yt = YouTube(a)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    #destination = 'python "C:\Benutzer\net\Musik"'
    destination = '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")


window = Tk()

lbl1 = Label(window, text="YouTube", fg='red', font=("Helvetica", 32))
lbl1.configure(bg='black')
lbl1.place(x=230, y=50)
lbl2 = Label(window, text="Link", fg='red', font=("Helvetica", 12))
lbl2.configure(bg='black')
lbl2.place(x=300, y=150)


txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=250, y=200)


btn_1 = Button(window, text="Download_MP4", fg='blue', command=lambda: Download_link())
btn_1.configure(bg='grey')
btn_1.place(x=350, y=100)
btn_2 = Button(window, text="Download_MP3", fg='blue', command=lambda: DownloadAudio())
btn_2.configure(bg='grey')
btn_2.place(x=200, y=100)

window.title('YouTube_Downloader')
window.configure(bg='black')
window.geometry("600x400")
window.mainloop()
txtfld.pack()
