# KarvIt: File Carving Tool

## Description

KarvIt is a Python-based GUI application designed for file carving. It allows users to extract specific file types, such as PNG, JPEG, PDF, and EVTX, from disk images. This tool is useful for digital forensics, data recovery, and analysis.

## Features

- **Disk Imager**: Launches a disk imaging tool for creating disk images.
- **File Carver**: Carves various file types (PNG, JPEG, PDF, EVTX) from disk images.
- **User-Friendly GUI**: Simple and intuitive interface built with Tkinter.

## Requirements

To run this application, you need to have Python installed along with the following packages:

- `tkinter`
- `Pillow` (PIL)
- `pytsk3`
- `subprocess`
- `threading`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shivang1209-dot/Karv_It.git
   cd Karv_It
   pip install -r requirements.txt
   python main.py

2. A sample zipped disk image is present in the Resources folder, unzip it and you can use that file for extracting PNGs, and JPEGs. 
