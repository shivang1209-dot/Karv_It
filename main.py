import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import threading


def run_subprocess(command):
    """Run a subprocess command in a separate thread."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def disk_imager():
    """Launch the Disk Imager tool."""
    threading.Thread(target=run_subprocess, args=(['python', './usb_image_gui.py'],)).start()
    print("Launching Disk Imager...")


def file_carver():
    """Launch the File Carver tool."""
    threading.Thread(target=run_subprocess, args=(['python', './file_carver_gui.py'],)).start()
    print("Launching File Carver...")


def create_main_window():
    """Create the main window for KarvIt."""
    root = tk.Tk()
    root.title("KarvIt: File Carving Tool")
    root.geometry("500x350")
    root.configure(bg="#0CF5EA")

    # Load logo image
    logo_image = Image.open("./logo.png").resize((75, 75))
    logo_tk_image = ImageTk.PhotoImage(logo_image)
    logo_label = ttk.Label(root, image=logo_tk_image, background="#0CF5EA")
    logo_label.place(x=2, y=2, anchor='nw')

    # Configure styles
    style = ttk.Style()
    style.configure('TButton', background="#0CF5EA", padding=(5, 5))

    # Configure labels and buttons
    font_bold = ("Langdon", 20, "bold")
    usb_label = ttk.Label(root, text="Welcome To KarvIt !!!", font=font_bold, foreground="#3C4692", background="#0CF5EA")
    usb_label.place(x=130, y=25)

    disk_imager_button = ttk.Button(root, text="Disk Imager", command=disk_imager)
    disk_imager_button.place(x=175, y=100, width=150, height=40)

    file_carver_button = ttk.Button(root, text="File Carver", command=file_carver)
    file_carver_button.place(x=175, y=200, width=150, height=40)

    root.mainloop()


if __name__ == "__main__":
    create_main_window()
