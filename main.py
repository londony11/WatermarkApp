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
        self.master_frame = Frame(master)

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
        Button(text="Open Photo", command=self.open_img).grid(column=1, row=2, columnspan=2, sticky="nesw")

        # Add Text button
        Button(text="Add Text", command=self.text_dialog).grid(column=1, row=3, sticky="nesw")

        # Add Logo button
        Button(text="Add Logo", command=self.logo_dialog).grid(column=2, row=3, sticky="nesw")


    def open_img(self):
        """Image open funciton"""
       
        # get image path
        img_path = filedialog.askopenfilename(initialdir="img/photo_collection")
       
        # Get image, image size
        img_pil = Image.open(img_path)
        self.img_width = min(img_pil.size[0], 1920)
        self.img_height = min(img_pil.size[1], 1020)
        img_pil.thumbnail((self.img_width, self.img_height))
        self.img_width = img_pil.size[0]
        self.img_height = img_pil.size[1]
       
        # Display image
        self.img_bg = ImageTk.PhotoImage(img_pil)
        self.canvas.configure(width=self.img_width, height=self.img_height)
        self.canvas.itemconfig(self.image_container, image=self.img_bg, anchor="nw")


    def text_dialog(self):
        """Text menu"""


        def add_text():
            """Put text to the image"""
            user_input = text_box.get(1.0, "end-1c")
            watermark_text = self.canvas.create_text(self.img_width/2, self.img_height/2, text=user_input, font=("Ariel", 40, "bold"), anchor="nw")

        text_menu = Toplevel(window)
        text_menu.title("Add Text")
        text_frame = Frame(text_menu, padx=100, pady=50)
        text_frame.grid()

        # Input box
        Label(text_frame, text="Text:", font=("Ariel", 40, "bold")).grid(column=1, row=1)
        text_box = Text(text_frame, height=5, width=40)
        text_box.grid(column=2, columnspan=2, row=1)

        # Add text button
        Button(text_frame, text="Add Text", command=add_text).grid(column=2, row=2, sticky="nesw")

        # Cancel button
        Button(text_frame, text="Cancel", command=text_menu.destroy).grid(column=3, row=2, sticky="nesw")
    
    
    def logo_dialog(self):
        """Logo menu"""

        logo_menu = Toplevel(window)
        logo_menu.title("Add logo")
        logo_frame = Frame(logo_menu, padx=100, pady=50)
        logo_frame.grid()

        # Input box
        Label(logo_frame, text="Logo:", font=("Ariel", 40, "bold")).grid(column=1, row=1)

        # Add logo place
        self.canvas_logo = Canvas(logo_frame, bg="gray")
        # logo_bg = ImageTk.PhotoImage(self.img_bg_pil)
        # self.canvas_logo.create_image(0, 0, image=logo_bg, anchor="nw")
        self.canvas_logo.grid(row=1, column=2, columnspan=2)

        # Open logo button
        Button(logo_frame, text="Open Logo", command=self.open_logo).grid(column=2, row=2, sticky="nesw")

        # Add logo button
        Button(logo_frame, text="Add Logo").grid(column=3, row=2, sticky="nesw")

        # Cancel button
        Button(logo_frame, text="Cancel", command=logo_menu.destroy).grid(column=2, row=3, columnspan=2, sticky="nesw")


    def open_logo(self):
        """Image open funciton"""


        def add_logo():
            """Put logo to the image"""
            watermark_logo = self.canvas.create_image(0, 0, image=self.logo_bg, anchor="nw")
    
        # get image path
        logo_path = filedialog.askopenfilename(initialdir="img/logo_collection")
    
        # Get image, image size
        logo_pil = Image.open(logo_path)
        self.logo_width = logo_pil.size[0]
        self.logo_height = logo_pil.size[1]
    
        # Display image
        self.logo_bg = ImageTk.PhotoImage(logo_pil)
        self.canvas_logo.configure(width=self.logo_width, height=self.logo_height)
        self.logo_container = self.canvas_logo.create_image(0, 0, image=self.logo_bg, anchor="nw")
        

window = Tk()
app = App(window)
window.mainloop()
