from customtkinter import CTkButton,CTkEntry,CTkLabel
import os
import yt_dlp as youtube_dl
import customtkinter as ctk
from customtkinter import filedialog
from tkinter import messagebox
import traceback

ffmpeg_path = #destination do ffmpeg.exe

def download_video(url, destination):
    if not (url and destination):
        messagebox.showwarning("Input Error", "Please provide a valid URL and destination.")

        return

    ydl_opts = {
        'format': 'bestvideo[height<=1080]/best[height<=1080]',
        'outtmpl': os.path.join(destination[0], '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video has been successfully downloaded.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        traceback.print_exc()

def download_audio(url,destination):
    if not (url and destination):
        messagebox.showwarning("Input Error", "Please provide a valid URL and destination.")

        return
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(destination[0], '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Audio has been successfully downloaded.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        traceback.print_exc()
def ChangeDestination(curDestination):
    tempDestination = filedialog.askdirectory()
    if tempDestination:
        print(f"Destination changed to: {tempDestination}")
        curDestination[0] = tempDestination
    else:
        print("No destination selected.")
def CreateWindow():
    destination = ["."]
    ctk.set_appearance_mode("dark")
    #window = CTk()
    window = ctk.CTk()
    #window.iconbitmap()

    lbl1 = CTkLabel(master=window, corner_radius=8, text="YouTube", fg_color='red', font=("Helvetica", 32))
    lbl1.pack(pady = 10)
    frame = ctk.CTkFrame(window)
    frame.pack(expand = True,fill = "both",padx=20,pady=10)

    lbl2 = CTkLabel(master=frame, text="Link", corner_radius=8, fg_color='red', font=("Helvetica", 12))
    lbl2.pack(pady = 20)

    buttonFrame = ctk.CTkFrame(frame,fg_color="transparent")


    btn_1 = CTkButton(buttonFrame, text="Download_MP4", fg_color='blue', command=lambda: download_video(txtfld.get(),destination))
    btn_2 = CTkButton(buttonFrame, text="Download_WAV", fg_color='blue', command=lambda: download_audio(txtfld.get(),destination))

    btn_3 = CTkButton(frame, text="Change directory", fg_color='blue', command=lambda: ChangeDestination(destination))
    txtfld = CTkEntry(frame, placeholder_text="YouTube Link")

    txtfld.pack(pady=10)
    buttonFrame.pack()
    btn_1.pack(side="left", padx=10)
    btn_2.pack(side="left", padx=10)
    btn_3.pack(pady=10)


    window.title('YouTube_Downloader')
    window.configure(background='black')
    window.geometry("600x400")
    window.mainloop()
    txtfld.pack()

if __name__ == "__main__":
    CreateWindow()
