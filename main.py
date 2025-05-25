import os
import traceback
import yt_dlp as youtube_dl
import tkinter as tk
from tkinter import messagebox, filedialog

ffmpeg_path = r"Your Paht to ffmpeg.exe"

def download_video(url, destination):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video has been successfully downloaded.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        traceback.print_exc()

def download_audio(url, destination):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(destination, '%(title)s.%(ext)s'),
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

def create_gui():
    def on_download_video():
        url = url_entry.get()
        destination = filedialog.askdirectory()
        if url and destination:
            download_video(url, destination)
        else:
            messagebox.showwarning("Input Error", "Please provide a valid URL and destination.")

    def on_download_audio():
        url = url_entry.get()
        destination = filedialog.askdirectory()
        if url and destination:
            download_audio(url, destination)
        else:
            messagebox.showwarning("Input Error", "Please provide a valid URL and destination.")

    root = tk.Tk()
    root.title("YouTube Downloader")
    root.geometry("400x200")

    tk.Label(root, text="YouTube URL:").pack(pady=10)
    url_entry = tk.Entry(root, width=50)
    url_entry.pack(pady=5)

    tk.Button(root, text="Download Video", command=on_download_video).pack(pady=10)
    tk.Button(root, text="Download Audio", command=on_download_audio).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":

    create_gui()
