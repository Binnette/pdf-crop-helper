import sys
import os
import fitz  # PyMuPDF
from tkinter import *
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk

class PDFCropper:
    def __init__(self, master, pdf_path):
        self.master = master
        self.master.title("PDF Cropper")
        self.master.state('zoomed')  # Maximize the window
        self.pdf_document = fitz.open(pdf_path)
        self.pdf_path = pdf_path
        self.page_index = 0
        self.customer_index = 1
        self.image = None
        self.image_tk = None
        self.rectangles = []
        self.current_rect = None
        self.output_dir = "output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.setup_ui()

    def setup_ui(self):
        self.master.update_idletasks()  # Ensure the window dimensions are updated
        self.canvas = Canvas(self.master, cursor="cross")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=YES)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.frame = Frame(self.master)
        self.frame.pack(side=RIGHT, fill=Y)

        self.customer_label = Label(self.frame, text=f"Customer {self.customer_index}")
        self.customer_label.pack(side=TOP, fill=X)

        self.page_label = Label(self.frame, text=f"Page {self.page_index + 1} / {len(self.pdf_document)}")
        self.page_label.pack(side=TOP, fill=X)

        self.next_page_btn = Button(self.frame, text="Next Page", command=self.next_page)
        self.next_page_btn.pack(side=TOP, fill=X)

        self.next_customer_btn = Button(self.frame, text="Next Customer", command=self.next_customer)
        self.next_customer_btn.pack(side=TOP, fill=X)

        self.reset_btn = Button(self.frame, text="Reset", command=self.reset_areas)
        self.reset_btn.pack(side=TOP, fill=X)

        self.finish_btn = Button(self.frame, text="Finish", command=self.finish_app)
        self.finish_btn.pack(side=TOP, fill=X)

        self.show_page()

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_mouse_drag(self, event):
        if self.current_rect:
            self.canvas.delete(self.current_rect)
        self.current_rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                                         outline="blue", width=2)

    def on_button_release(self, event):
        self.rectangles.append((self.start_x, self.start_y, event.x, event.y))
        self.current_rect = None

    def next_page(self):
        self.crop_areas()
        self.page_index += 1
        if self.page_index >= len(self.pdf_document):
            self.next_page_btn.pack_forget()
        else:
            self.show_page()
        self.update_page_label()

    def next_customer(self):
        self.customer_index += 1
        self.customer_label.config(text=f"Customer {self.customer_index}")
        self.reset_areas()

    def show_page(self):
        page = self.pdf_document[self.page_index]
        zoom = 2  # to increase the resolution
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Resize the image to fit the height of the window
        window_height = self.master.winfo_height()
        aspect_ratio = pix.width / pix.height
        new_width = int(window_height * aspect_ratio)
        self.image = img.resize((new_width, window_height), Image.LANCZOS)
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image_tk)

    def crop_areas(self):
        for i, (x1, y1, x2, y2) in enumerate(self.rectangles):
            cropped_image = self.image.crop((x1, y1, x2, y2))
            output_path = os.path.join(self.output_dir,
                                       f"customer{self.customer_index}_page{self.page_index + 1}_area{i + 1}.png")
            cropped_image.save(output_path)
        self.rectangles.clear()

    def reset_areas(self):
        self.rectangles.clear()
        self.canvas.delete("all")
        self.show_page()

    def update_page_label(self):
        self.page_label.config(text=f"Page {self.page_index + 1} / {len(self.pdf_document)}")

    def finish_app(self):
        self.crop_areas()
        self.master.quit()
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_cropper.py input.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]

    root = Tk()
    app = PDFCropper(root, pdf_path)
    root.mainloop()
