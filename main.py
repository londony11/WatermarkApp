"""Import app dependencies."""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class App:
    """Application class."""


    def __init__(self, master):
        master.title("Watermark")
        master.config(padx=100, pady=50)

        self.canvas = Canvas(width=200, height=200, bg="grey", highlightthickness=0)
        self.img_bg = PhotoImage(file="img/img_bg.png")
        self.image_container = self.canvas.create_image(100, 100, image=self.img_bg)
        self.canvas.grid(column=1, row=1)

        self.open_button = Button(text="Open Photo", command=self.open_photo)
        self.open_button.grid(column=1, row=2)

        add_watermark_button = Button(text="Add Watermark")
        add_watermark_button.grid(column=1, row=3)


    def open_photo(self):
        """File open funciton."""
        img_path = filedialog.askopenfilename()
        img_pil = Image.open(img_path).resize((200, 200))
        self.img_tk = ImageTk.PhotoImage(img_pil)
        self.canvas.itemconfig(self.image_container, image=self.img_tk)


window = Tk()
app = App(window)
window.mainloop()
