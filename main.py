from pytube import YouTube
from customtkinter import CTkButton,CTkEntry,CTkLabel
import os
import customtkinter as ctk



def Download_link(txtfld,destination):
    a = txtfld.get()
    print(a)
    yt = YouTube(a)
    ys = yt.streams.get_highest_resolution()

    # download the file
    out_file = ys.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")



def DownloadAudio(txtfld,destination):
    a = txtfld.get()
    print(a)
    yt = YouTube(a)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.wav'
    os.rename(out_file, new_file)
    # result of success
    print(yt.title + " has been successfully downloaded.")
def CreateWindow():
    destination1 = ""#folder to save dowloadet video     $$$$$$$$$$$$$$$$$$$$$
    destination2 = ""# folder to save dowloadet audio    §§§§§§§§§§§§§§§§§§§§§
    ctk.set_appearance_mode("dark")

    window = ctk.CTk()
    #window.iconbitmap()add custom icon

    lbl1 = CTkLabel(master=window, corner_radius=8, text="YouTube", fg_color='red', font=("Helvetica", 32))
    lbl1.pack(pady = 10)
    frame = ctk.CTkFrame(window)
    frame.pack(expand = True,fill = "both",padx=20,pady=10)

    lbl2 = CTkLabel(master=frame, text="Link", corner_radius=8, fg_color='red', font=("Helvetica", 12))
    lbl2.pack(pady = 20)

    buttonFrame = ctk.CTkFrame(frame,fg_color="transparent")


    btn_1 = CTkButton(buttonFrame, text="Download_MP4", fg_color='blue', command=lambda: Download_link(txtfld,destination1))
    btn_2 = CTkButton(buttonFrame, text="Download_WAV", fg_color='blue', command=lambda: DownloadAudio(txtfld,destination2))

    txtfld = CTkEntry(frame, placeholder_text="This is Entry Widget")

    txtfld.pack(pady=10)
    buttonFrame.pack()
    btn_1.pack(side="left", padx=10)
    btn_2.pack(side="left", padx=10)



    window.title('YouTube_Downloader')
    window.configure(background='black')
    window.geometry("600x400")
    window.mainloop()
    txtfld.pack()
CreateWindow()
