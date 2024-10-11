from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, filedialog


def main():
    # Start the Tkinter event loop
    root.mainloop()

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Disk Image Files", "*.img;*.iso;*.dd")])
    file_var.set(file_path)

def carve_png_files():
    print("Carving PNG files...")
    src_file_path = file_var.get()
    dst_file_path = "./carved_png_files"

    # Define header and footer for PNG files
    PNG_HEADER = bytes([0x89, 0x50, 0x4e, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
    PNG_FOOTER = bytes([0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, 0x44, 0xAE, 0x42, 0x60, 0x82])

    # Set the chunk size
    chunk_size = 1024 * 1024  

    # Initialize position and counter for carved files
    position = 0
    count = 0

    with open(src_file_path, "rb") as file:
        while True:
            # Read a chunk from the file
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file

            # Search for the header in the chunk
            header_index = chunk.find(PNG_HEADER)

            while header_index != -1:
                # Calculate the absolute position of the header in the entire file
                absolute_header_index = position + header_index

                # Search for the footer in the chunk starting from the header
                footer_index = chunk.find(PNG_FOOTER, header_index)

                if footer_index != -1:
                    # Calculate the end of the footer
                    footer_end = absolute_header_index + footer_index + len(PNG_FOOTER)

                    # Ensure the footer is after the header
                    if absolute_header_index < footer_end:
                        count += 1
                        dst_data = chunk[header_index:footer_end]
                        dst_file_name = f"{dst_file_path}_{count}.png"
                        open(dst_file_name, "wb").write(dst_data)
                        print("Carved:", dst_file_name)

                    # Update position to search for the next PNG file
                    position = footer_end

                # Find the next header in the remaining part of the chunk
                header_index = chunk.find(PNG_HEADER, header_index + 1)

        # Print the total number of carved files
        print(f"Successfully Carved {count} PNG Files...")
    
    status_label.config(text=f"Successfully Carved {count} PNG Files...", foreground="green", font="Helvatica")
    
    
def carve_jpeg_files():
    print("Carving JPEG files...")

    src_file_path = file_var.get()
    dst_file_path = "./carved_JPEG_files"

    # Define header and footer for JPEG files
    JPEG_HEADER = bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46])
    JPEG_FOOTER = bytes([0xFF, 0xD9])

    # Set the chunk size
    chunk_size = 1024 * 1024

    # Initialize position and counter for carved files
    position = 0
    count = 0

    with open(src_file_path, "rb") as file:
        while True:
            # Read a chunk from the file
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file

            # Search for the header in the chunk
            header_index = chunk.find(JPEG_HEADER)

            while header_index != -1:
                # Calculate the absolute position of the header in the entire file
                absolute_header_index = position + header_index

                # Search for the footer in the chunk starting from the header
                footer_index = chunk.find(JPEG_FOOTER, header_index)

                if footer_index != -1:
                    # Calculate the end of the footer
                    footer_end = absolute_header_index + footer_index + len(JPEG_FOOTER)

                    # Ensure the footer is after the header
                    if absolute_header_index < footer_end:
                        count += 1
                        dst_data = chunk[header_index:footer_end]
                        dst_file_name = f"{dst_file_path}_{count}.jpeg"
                        open(dst_file_name, "wb").write(dst_data)
                        print("Carved:", dst_file_name)

                    # Update position to search for the next JPEG file
                    position += footer_end

                # Find the next header in the remaining part of the chunk
                header_index = chunk.find(JPEG_HEADER, header_index + 1)

    # Print the total number of carved files
    print(f"Successfully Carved {count} JPEG Files...")

    status_label.config(text=f"Successfully Carved {count} JPEG Files...", foreground="green", font="Helvatica")

def carve_pdf_files():
    print("Carving PDF files...")

    src_file_path = file_var.get()
    dst_file_path = "./carved_PDF_files"

    # Define header and footer for PDF files
    PDF_HEADER = bytes([0x25, 0x50, 0x44, 0x46, 0x2D, 0x31, 0x2E])
    PDF_FOOTER = bytes([0x25, 0x25, 0x45, 0x4F, 0x46])

    # Set the chunk size
    chunk_size = 1024 * 1024

    # Initialize position and counter for carved files
    position = 0
    count = 0

    with open(src_file_path, "rb") as file:
        while True:
            # Read a chunk from the file
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file

            # Search for the header in the chunk
            header_index = chunk.find(PDF_HEADER)

            while header_index != -1:
                # Calculate the absolute position of the header in the entire file
                absolute_header_index = position + header_index

                # Search for the footer in the chunk starting from the header
                footer_index = chunk.find(PDF_FOOTER, header_index)

                if footer_index != -1:
                    # Calculate the end of the footer
                    footer_end = absolute_header_index + footer_index + len(PDF_FOOTER)

                    # Ensure the footer is after the header
                    if absolute_header_index < footer_end:
                        count += 1
                        dst_data = chunk[header_index:footer_end]
                        dst_file_name = f"{dst_file_path}_{count}.pdf"
                        open(dst_file_name, "wb").write(dst_data)
                        print("Carved:", dst_file_name)

                    # Update position to search for the next PDF file
                    position += footer_end

                # Find the next header in the remaining part of the chunk
                header_index = chunk.find(PDF_HEADER, header_index + 1)

    # Print the total number of carved files
    print(f"Successfully Carved {count} PDF Files...")

    status_label.config(text=f"Successfully Carved {count} PDF Files...", foreground="green", font="Helvatica")

def carve_evtx_files():
    print("Carving EVTX files...")
    src_file_path = file_var.get()
    
    dst_file_path = "./carved_log_files"

    # Define header and footer for EVTX files
    EVTX_HEADER = bytes([0x45, 0x6C, 0x66, 0x46, 0x69, 0x6C, 0x65])
    EVTX_FOOTER = bytes([0x68, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x68, 0x03, 0x00, 0x00])

    # Set the chunk size
    chunk_size = 1024 * 1024

    # Initialize position and counter for carved files
    position = 0
    count = 0

    with open(src_file_path, "rb") as file:
        while True:
            # Read a chunk from the file
            chunk = file.read(chunk_size)
            if not chunk:
                break  # End of file

            # Search for the header in the chunk
            header_index = chunk.find(EVTX_HEADER)

            while header_index != -1:
                # Calculate the absolute position of the header in the entire file
                absolute_header_index = position + header_index

                # Search for the footer in the chunk starting from the header
                footer_index = chunk.find(EVTX_FOOTER, header_index)

                if footer_index != -1:
                    # Calculate the end of the footer
                    footer_end = absolute_header_index + footer_index + len(EVTX_FOOTER)

                    # Ensure the footer is after the header
                    if absolute_header_index < footer_end:
                        count += 1
                        dst_data = chunk[header_index:footer_end]
                        dst_file_name = f"{dst_file_path}_{count}.evtx"
                        open(dst_file_name, "wb").write(dst_data)
                        print("Carved:", dst_file_name)

                    # Update position to search for the next EVTX file
                    position += footer_end

                # Find the next header in the remaining part of the chunk
                header_index = chunk.find(EVTX_HEADER, header_index + 1)

    # Print the total number of carved files
    print(f"Successfully Carved {count} EVTX Files...")

    status_label.config(text=f"Successfully Carved {count} EVTX Files...", foreground="green", font="Helvatica")

def exit_application():
    print("Closing Window...")
    root.destroy()


# Create themed Tkinter window
root = tk.Tk()
root.title("KarvIt: File Carving Tool")
window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")
bg_color = "#0CF5EA"
logo_image = Image.open("Resources/KarvIt_Logo.png")
logo_image = logo_image.resize((100, 50))
logo_tk_image = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(root, image=logo_tk_image, background=bg_color)
logo_label.place(x=2, y=2, anchor='nw')

# Configure background color
style = ttk.Style()
style.configure('TButton', background=bg_color, relief='raised', padding=(5, 5))

# Configure fonts
font_bold = ("Courier", 12, "bold")
font_normal = ("Courier", 10)

root.configure(bg=bg_color)

# Widgets
usb_label = ttk.Label(root, text="Karv It - File Carver", font=("Langdon", 20, "bold"), foreground="#3C4692", background=bg_color)
usb_label.place(x=160, y=25)

# Dropdown for selecting the disk image file
file_var = tk.StringVar()
file_label = ttk.Label(root, text="Choose Disk Image File:", font=font_normal, background=bg_color)
file_label.place(x=80, y=100)
file_entry = ttk.Entry(root, textvariable=file_var, state="readonly", width=30)
file_entry.place(x=275, y=100)
browse_button = ttk.Button(root, text="Browse", command=browse_file)
browse_button.place(x=470, y=95)

# Buttons in pairs on two rows with spacing
button_y = 160
png_carver = ttk.Button(root, text="Carve PNG Files", command=carve_png_files)
png_carver.place(x=100, y=button_y, width=150, height=40)

jpeg_carver = ttk.Button(root, text="Carve JPEG Files", command=carve_jpeg_files)
jpeg_carver.place(x=300, y=button_y, width=150, height=40)

button_y += 70
pdf_carver = ttk.Button(root, text="Carve PDF Files", command=carve_pdf_files)
pdf_carver.place(x=100, y=button_y, width=150, height=40)

evtx_carver = ttk.Button(root, text="Carve EVTX Files", command=carve_evtx_files)
evtx_carver.place(x=300, y=button_y, width=150, height=40)

status_label = ttk.Label(root, text="", font=font_normal, background=bg_color)
status_label.place(x=125, y=button_y + 70)

# Exit button in the row below
exit_button = ttk.Button(root, text="Close Window", command=root.destroy)
exit_button.place(x=200, y=button_y + 120, width=150, height=40)

if __name__ == "__main__":
    main()
