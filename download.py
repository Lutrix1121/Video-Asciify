from tkinter import messagebox
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress
import glob
import globals
import os

save_path=None

def choose_path():
    global save_path
    save_path = filedialog.askdirectory()
    return save_path

def download_video():
    link = globals.VIDEO_LINK
    if not link.strip():
        messagebox.showwarning("Warning","No video link, Provide the YouTube video link.")
        return
    
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(choose_path())
        messagebox.showinfo("Operation completed", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't download video: {e}")
        
def download_audio():
    link = globals.VIDEO_LINK
    if not link.strip():
        messagebox.showwarning("Warning","No video link, Provide the YouTube video link.")
        return
    
    try:
        yt = YouTube(link, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(choose_path())
        messagebox.showinfo("Operation completed", f"Downloaded: {yt.title}")
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't download audio: {e}")

def save_file_name():
    try:
        list_of_files = glob.glob(f'{save_path}/*.mp4') if save_path else glob.glob(f'{os.getcwd()}/*.mp4')
        if not list_of_files:
            messagebox.showinfo("Error", "Couldn't find any video files in the directory.")
            return
        latest_file = max(list_of_files, key=os.path.getctime)
        globals.CURRENT_FILE = os.path.basename(latest_file)
    except Exception as e:
        messagebox.showerror("Error", f"Couldn't find the video file: {e}")

def get_latest_file():
    save_file_name()
    if globals.CURRENT_FILE:
        messagebox.showinfo("Latest video file", f"Latest video file: {os.path.basename(globals.CURRENT_FILE)}")
