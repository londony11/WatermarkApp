"""Import app dependencies."""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import subprocess


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
        self.img_final = Image.new("RGB", (self.img_width, self.img_height), (255, 255, 255, 0))

        # Open Photo button
        Button(text="Open Photo", command=self.open_img).grid(column=1, row=2, columnspan=2, sticky="nesw")

        # Add Text button
        Button(text="Add Text", command=self.text_dialog).grid(column=1, row=3, sticky="nesw")

        # Add Logo button
        Button(text="Add Logo", command=self.logo_dialog).grid(column=2, row=3, sticky="nesw")

        # Open Save button
        Button(text="Save Photo", command=self.save_img).grid(column=1, row=4, columnspan=2, sticky="nesw")


    def open_img(self):
        """Image open funciton"""
       
        # Get image path
        img_path = filedialog.askopenfilename(initialdir="img/photo_collection")
       
        # Get image, image size
        img_pil = Image.open(img_path)
        self.img_width = min(img_pil.size[0], 1920)
        self.img_height = min(img_pil.size[1], 1020)
        img_pil.thumbnail((self.img_width, self.img_height))
        self.img_width = img_pil.size[0]
        self.img_height = img_pil.size[1]

        # Update final image for saving
        self.img_final = img_pil
        # self.final_img.show()

        # Display image
        self.img_bg = ImageTk.PhotoImage(img_pil)
        self.canvas.configure(width=self.img_width, height=self.img_height)
        self.canvas.itemconfig(self.image_container, image=self.img_bg, anchor="nw")


    def text_dialog(self):
        """Text menu"""


        def add_text():
            """Put text to the image"""
            
            # Get user inputs
            user_input = text_box.get(1.0, "end-1c")
            
            # Update final image for saving
            draw = ImageDraw.Draw(self.img_final)
            font = ImageFont.truetype("Arial Black", 40)
            text_length = int(draw.textlength(text=user_input, font=font))
            draw.text((self.img_width-text_length-10, self.img_height-50), text=user_input, font=font)
            # self.img_final.show()

            # Display image with text
            self.canvas.create_text(self.img_width-text_length-10, self.img_height-50, text=user_input, font=("Arial Black", 40), anchor="nw")
            

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
        self.canvas_logo = Canvas(logo_frame, highlightthickness=0)
        self.canvas_logo.update()
        canvas_logo_width = self.canvas_logo.winfo_reqwidth()
        self.logo_bg = ImageTk.PhotoImage(self.img_bg_pil)
        self.canvas_logo.create_image((canvas_logo_width-200)/2, 0, image=self.logo_bg, anchor="nw")
        self.canvas_logo.grid(row=1, column=2, columnspan=2)

        # Open logo button
        Button(logo_frame, text="Open Logo", command=self.open_logo).grid(column=2, row=2, sticky="nesw")

        # Add logo button
        Button(logo_frame, text="Add Logo", command=self.add_logo).grid(column=3, row=2, sticky="nesw")

        # Cancel button
        Button(logo_frame, text="Cancel", command=logo_menu.destroy).grid(column=2, row=3, columnspan=2, sticky="nesw")


    def open_logo(self):
        """Image open funciton"""
    
        # Get image path
        logo_path = filedialog.askopenfilename(initialdir="img/logo_collection")
    
        # Get image, image size
        self.logo_pil = Image.open(logo_path)
        self.logo_width = min(self.logo_pil.size[0], 200)
        self.logo_height = min(self.logo_pil.size[1], 200)
        self.logo_pil.thumbnail((self.logo_width, self.logo_height))
        self.logo_width = self.logo_pil.size[0]
        self.logo_height = self.logo_pil.size[1]
        # self.logo_pil.show()
    
        # Show logo in menu
        self.logo_bg = ImageTk.PhotoImage(self.logo_pil)
        self.canvas_logo.configure(width=self.logo_width, height=self.logo_height)
        self.logo_container = self.canvas_logo.create_image(0, 0, image=self.logo_bg, anchor="nw")


    def add_logo(self):
        """Put logo to the image"""
        
        # Update final image for saving
        self.img_final.paste(self.logo_pil, box=((self.img_width - self.logo_width), (self.img_height - self.logo_height)))
        # self.img_final.show()

        # Display image
        self.canvas.create_image((self.img_width - self.logo_width), (self.img_height - self.logo_height), image=self.logo_bg, anchor="nw")
    
        
    def save_img(self):
        """Save image"""

        self.img_final.save("result.jpg")
        subprocess.call(["open", "result.jpg"])


window = Tk()
app = App(window)
window.mainloop()
