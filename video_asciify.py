import tkinter as tk
from tkinter import ttk
import download
import gui_functions

class VideoASCIIConverter:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x500")
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Video to ASCII Converter", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        # File selection section
        pick_label = tk.Label(self.root, text="Choose a video from disc drive:")
        pick_label.pack(pady=5)
        choose_button = tk.Button(
            self.root, 
            text="Choose Path", 
            command=gui_functions.choose_path, 
            width=20, 
            height=2,
            bg="lightblue"
        )
        choose_button.pack(pady=5)

        # YouTube link section
        link_label = tk.Label(self.root, text="Or paste the link to the youtube video you want to asciify:")
        link_label.pack(pady=5)
        self.link_entry = tk.Entry(self.root, width=50)
        self.link_entry.pack(pady=5)

        # Action buttons
        download_button = tk.Button(
            self.root, 
            text="Download video", 
            command=lambda: gui_functions.on_download(self.link_entry),
            width=20,
            height=2,
            bg="lightblue"
        )
        download_button.pack(pady=10)

        latest_file_button = tk.Button(
            self.root, 
            text="Show latest video file", 
            command=download.get_latest_file,
            width=20,
            height=2,
            bg="lightblue"
        )
        latest_file_button.pack(pady=10)

        start_button = tk.Button(
            self.root, 
            text="Start asciifying", 
            command=lambda: gui_functions.start_conversion(
                self.progress_frame, self.progress_var, self.progress_label, self.root
            ),
            width=20,
            height=2,
            bg="lightgreen"
        )
        start_button.pack(pady=10)

        # Progress section
        self.progress_frame = tk.Frame(self.root)
        self.progress_frame.pack_forget()
                
        self.progress_var = tk.DoubleVar()
        self.progress_label = tk.Label(
            self.progress_frame, 
            text="Progress: 0/0 frames processed (0%)", 
            font=("Arial", 9)
        )
        self.progress_label.pack()
                
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            variable=self.progress_var,
            maximum=100,
            length=300,
            mode='determinate'
        )
        self.progress_bar.pack(pady=5)

        # Quit button
        quit_button = tk.Button(
            self.root, 
            text="Quit", 
            command=self.root.destroy, 
            width=20, 
            height=2,
            bg="red"
        )
        quit_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = VideoASCIIConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()