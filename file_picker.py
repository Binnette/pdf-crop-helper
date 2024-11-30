import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")],
        title="Select a PDF file"
    )

    if file_path:
        print(file_path)
    else:
        print("No file selected")

if __name__ == "__main__":
    main()
