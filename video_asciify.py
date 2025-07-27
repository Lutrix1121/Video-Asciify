# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 20:16:42 2024

@author: Lutrix
"""

import tkinter as tk
import Download
import Conversion
import globals
import shutil

def get_video_link():
    return link_entry.get()

def on_download():
    globals.set_video_link(get_video_link())
    Download.download_video()


root = tk.Tk()
root.title("YouTube Video Downloader")
root.geometry("400x300")

link_label = tk.Label(root, text="Paste the link to the youtube video you want to asciify:")
link_label.pack(pady=5)
link_entry = tk.Entry(root, width=50)
link_entry.pack(pady=5)

# Przyciski
download_button = tk.Button(root, text="Download video", command=on_download)
download_button.pack(pady=10)

latest_file_button = tk.Button(root, text="Show latest video file", command=Download.get_latest_file)
latest_file_button.pack(pady=10)

start_button = tk.Button(root, text="Start asciify", command=lambda: Conversion.conversion(globals.CURRENT_FILE))
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=10)
root.mainloop()
