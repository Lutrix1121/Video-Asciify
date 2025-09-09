import tkinter as tk
from tkinter import ttk
import download
import gui_functions

class VideoASCIIConverter:
    def __init__(self, root):
        self.root = root
        self.dark_mode = False
        self.setup_window()
        self.create_widgets()
        self.apply_theme()
        
    def setup_window(self):
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        
    def apply_theme(self):
        if self.dark_mode:
            # Dark mode colors
            bg_color = "#2b2b2b"
            fg_color = "#ffffff"
            button_bg = "#404040"
            button_fg = "#ffffff"
            entry_bg = "#404040"
            entry_fg = "#ffffff"
            special_buttons = {
                'choose': "#3a5998",
                'download': "#3a5998",
                'save': "#b8860b", 
                'latest': "#3a5998",
                'start': "#228b22",
                'quit': "#8b0000"
            }
        else:
            # Light mode colors
            bg_color = "#f0f0f0"
            fg_color = "#000000"
            button_bg = "SystemButtonFace"
            button_fg = "#000000"
            entry_bg = "#ffffff"
            entry_fg = "#000000"
            special_buttons = {
                'choose': "lightblue",
                'download': "lightblue",
                'save': "yellow",
                'latest': "lightblue", 
                'start': "lightgreen",
                'quit': "red"
            }
            
        # Apply to root window
        self.root.configure(bg=bg_color)
        
        # Apply to all widgets
        for widget in self.root.winfo_children():
            self.apply_theme_to_widget(widget, bg_color, fg_color, button_bg, button_fg, 
                                     entry_bg, entry_fg, special_buttons)
                                     
        # Update theme toggle button text
        self.theme_button.configure(text="     ☀️" if self.dark_mode else "🌙")
        
    def apply_theme_to_widget(self, widget, bg_color, fg_color, button_bg, button_fg, 
                            entry_bg, entry_fg, special_buttons):
        widget_class = widget.winfo_class()
        
        if widget_class == "Label":
            widget.configure(bg=bg_color, fg=fg_color)
        elif widget_class == "Button":
            # Check if it's a special button by text
            button_text = widget.cget('text')
            if button_text == "Download video":
                widget.configure(bg=special_buttons['download'], fg=button_fg)
            elif button_text == "Choose Path":
                widget.configure(bg=special_buttons['choose'], fg=button_fg)
            elif button_text == "Save path":
                widget.configure(bg=special_buttons['save'], fg=button_fg)
            elif button_text == "Show latest video file":
                widget.configure(bg=special_buttons['latest'], fg=button_fg)
            elif button_text == "Start asciifying":
                widget.configure(bg=special_buttons['start'], fg=button_fg)
            elif button_text == "Quit":
                widget.configure(bg=special_buttons['quit'], fg=button_fg)
            else:
                widget.configure(bg=button_bg, fg=button_fg)
        elif widget_class == "Entry":
            widget.configure(bg=entry_bg, fg=entry_fg, insertbackground=fg_color)
        elif widget_class == "Frame":
            widget.configure(bg=bg_color)
            # Recursively apply to frame children
            for child in widget.winfo_children():
                self.apply_theme_to_widget(child, bg_color, fg_color, button_bg, button_fg,
                                         entry_bg, entry_fg, special_buttons)
        elif widget_class == "Progressbar":
            # Configure progressbar style for dark/light mode
            style = ttk.Style()
            if self.dark_mode:
                style.configure("TProgressbar", background="#4a9eff")
            else:
                style.configure("TProgressbar", background="#0078d4")
        
    def create_widgets(self):
        # Theme toggle button (top right)
        self.theme_button = tk.Button(
            self.root,
            text="🌙",
            command=self.toggle_theme,
            width=3,
            height=1,
            font=("Arial", 12)
        )
        self.theme_button.place(x=350, y=10)

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

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        # Buttons row
        buttons_row = tk.Frame(button_frame)
        buttons_row.pack(pady=5)

        # Action buttons
        downloadVideo_button = tk.Button(
            buttons_row, 
            text="Download video", 
            command=lambda: gui_functions.on_download_video(self.link_entry),
            width=20,
            height=2,
            bg="lightblue"
        )
        downloadVideo_button.pack(side = 'left', pady=5, padx = 5)

        downloadAudio_button = tk.Button(
            buttons_row, 
            text="Download audio", 
            command=lambda: gui_functions.on_download_audio(self.link_entry),
            width=20,
            height=2,
            bg="lightblue"
        )
        downloadAudio_button.pack(side = 'left', pady=5, padx = 5)     

        save_button = tk.Button(
            self.root,
            text="Save path",
            command=gui_functions.save_path,
            width=20,
            height=2,
            bg="yellow"
        )
        save_button.pack(pady=10)   

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