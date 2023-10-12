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

        # Setup default background
        self.canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.img_bg_pil = Image.open("img/img_bg.png").resize((200, 200))
        self.img_bg = ImageTk.PhotoImage(self.img_bg_pil)
        self.image_container = self.canvas.create_image(0, 0, image=self.img_bg, anchor="nw")
        self.canvas.grid(column=1, row=1, columnspan=2)

        # Setup variables
        self.img_width = 100
        self.img_height = 100

        # Open Photo button
        Button(text="Open Photo", command=self.open_photo).grid(column=1, row=2, columnspan=2, sticky="nesw")

        # Add Text button
        Button(text="Add Text", command=self.add_text).grid(column=1, row=3, sticky="nesw")

        # Add Logo button
        Button(text="Add Logo").grid(column=2, row=3, sticky="nesw")


    def open_photo(self):
        """Image open funciton"""
       
        # get image path
        img_path = filedialog.askopenfilename()
       
        # Get image, image size
        img_pil = Image.open(img_path)
        self.img_width = img_pil.size[0]
        self.img_height = img_pil.size[1]
       
        # Display image
        self.img_bg = ImageTk.PhotoImage(img_pil)
        self.canvas.configure(width=self.img_width, height=self.img_height)
        self.canvas.itemconfig(self.image_container, image=self.img_bg, anchor="nw")


    def add_text(self):
        """Add Text menu"""


        def get_user_input():
            user_input = text_box.get(1.0, "end-1c")
            watermark_text = self.canvas.create_text(self.img_width/2, self.img_height/2, text=user_input, font=("Ariel", 40, "bold"), anchor="nw")


        text_menu = Toplevel(window)
        text_menu.title("Add Text")
        menu_frame = Frame(text_menu, padx=100, pady=50)
        menu_frame.grid()

        # Input box
        Label(menu_frame, text="Text:").grid(column=1, row=1)
        text_box = Text(menu_frame, height=5, width=40)
        text_box.grid(column=2, columnspan=2, row=1)

        # Add text button
        Button(menu_frame, text="Add Text", command=get_user_input).grid(column=2, row=2, sticky="nesw")

        # Cancel button
        Button(menu_frame, text="Cancel", command=text_menu.destroy).grid(column=3, row=2, sticky="nesw")






window = Tk()
app = App(window)
window.mainloop()
