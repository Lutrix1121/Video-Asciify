import tkinter as tk
from tkinter import messagebox, filedialog
import download
import globals

def get_video_link(link_entry):
    return link_entry.get()

def choose_path():
    path = filedialog.askopenfilename(        
        title="Select Data File",
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    if path:
        globals.CURRENT_FILE = path
        messagebox.showinfo("Path Selected", f"Path set to: {path}")
        return path
    else:
        messagebox.showwarning("Warning", "No path selected.")
        return None

def on_download(link_entry):
    """Handle video download process"""
    globals.set_video_link(get_video_link(link_entry))
    download.download_video()
    download.save_file_name()

def update_progress(current, total, percentage, progress_frame, progress_var, progress_label, root):
    """Update progress bar and label"""
    if not progress_frame.winfo_ismapped():
        show_progress_frame(progress_frame, progress_var, progress_label, root)
    progress_var.set(percentage)
    progress_label.config(text=f"Progress: {current}/{total} frames processed ({percentage:.1f}%)")
    root.update()

def show_progress_frame(progress_frame, progress_var, progress_label, root):
    """Show and reset progress frame"""
    progress_frame.pack(pady=10, padx=20, fill='x')
    progress_var.set(0)  # Reset progress
    progress_label.config(text="Progress: 0/0 frames processed (0%)")
    root.update()

def hide_progress_frame(progress_frame):
    """Hide progress frame"""
    progress_frame.pack_forget()

def start_conversion(progress_frame, progress_var, progress_label, root):
    """Start the ASCII conversion process"""
    import converter
    hide_progress_frame(progress_frame)
    converter.conversion(
        globals.CURRENT_FILE,
        progress_callback=lambda c, t, p: update_progress(c, t, p, progress_frame, progress_var, progress_label, root)
    )