from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import subprocess
import threading

def run_subprocess(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def disk_imager():
    threading.Thread(target=run_subprocess, args=(['python', "./usb_image_gui.py"],)).start()
    print("Exiting Karv It...")
    
def file_carver():
    threading.Thread(target=run_subprocess, args=(['python', "./file_carver_gui.py"],)).start()
    print("Exiting Karv It...")

def main():
    root = tk.Tk()
    root.title("KarvIt: File Carving Tool")
    window_width = 500
    window_height = 350
    root.geometry(f"{window_width}x{window_height}")
    bg_color = "#0CF5EA"

    # Configure background color
    style = ttk.Style()
    style.configure('TButton', background=bg_color, relief='raised', padding=(5, 5))

    # Configure fonts
    font_bold = ("Langdon", 20, "bold")
    font_normal = ("Courier", 12)

    root.configure(bg=bg_color)

    # Widgets
    usb_label = ttk.Label(root, text="Welcome To KarvIt !!! ", font= font_bold, foreground="#3C4692", background=bg_color)
    usb_label.place(x=130, y=25)

    # Buttons in pairs on two rows
    disk_imager_button = ttk.Button(root, text="Disk Imager", command=disk_imager)
    disk_imager_button.place(x=175, y=100, width=150, height=40)

    file_carver_button = ttk.Button(root, text="File Carver", command=file_carver)
    file_carver_button.place(x=175, y=200, width=150, height=40)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
