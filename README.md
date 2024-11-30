# PDF Cropper

PDF Cropper is a Python Tkinter application that allows you to crop and save specific areas of PDF pages. The application displays each page of a given PDF in full screen and provides tools to select and crop rectangular areas, saving them as PNG images. Once cropped, the images are displayed in a web browser so you can print them as a new PDF file. The main goal is to avoid wasting paper when printing only a few areas of a PDF file.

## Features

- Display PDF pages in full screen
- Select multiple rectangular areas on a page to crop
- Save cropped areas as PNG images in a specified output folder
- Navigate through PDF pages with "Next" and "Finish" buttons
- Print cropped images as a new PDF file via the web browser

## Prerequisites

- Python 3.x

## Get the App

```sh
git clone https://github.com/yourusername/pdf-cropper.git
cd pdf-cropper
```

## Run on Windows

### Crop PDF File

1. Run the script `1_crop_pdf.bat`
2. Select a PDF file to crop
3. Use the interface to select areas
4. Press "Next page" to navigate through pages
5. Press "Next customer" to switch to the next customer
6. Repeat until all pages are cropped
7. Press "Finish" to close the application

### Print Cropped Images as PDF

1. Run the script `2_show_png.bat`
2. Your web browser will open and show all the images
3. Press `Ctrl + P` to print the images as PDF
   - Use the scale percentage to fit the images to pages
   - Adjust the margins to fit the layout

## Run on Linux/Mac

### Crop PDF File

1. Create/activate the virtual environment and install dependencies
   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install pymupdf pillow
   ```
2. Run the PDF cropper with your PDF file as input.pdf
   ```sh
   python pdf_cropper.py input.pdf
   ```
3. Use the interface to select areas
4. Press "Next page" to navigate through pages
5. Press "Next customer" to switch to the next customer
6. Repeat until all pages are cropped
7. Press "Finish" to close the application

### Print Cropped Images as PDF

1. Run `python serve_images.py`
2. Your web browser will open and show all the images
3. Press `Ctrl + P` to print the images as PDF
   - Use the scale percentage to fit the images to pages
   - Adjust the margins to fit the layout

## Acknowledgements

This project uses the following libraries:
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF)
- [Pillow](https://python-pillow.org/)
