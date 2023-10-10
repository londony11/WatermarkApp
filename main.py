from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def open_photo():
    img_path = filedialog.askopenfilename()
    img_pil = Image.open(img_path)
    img_pil.save("img/01.png")
    img_tk = PhotoImage("img/01.png")
    canvas.itemconfig
    return 0


window = Tk()
window.title("Watermark")
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=200, bg="grey", highlightthickness=0)
img_bg = PhotoImage(file="img/img_bg.png")
canvas.create_image(100, 100, image=img_bg)
canvas.grid(column=1, row=1)

open_button = Button(text="Open Photo", command=open_photo)
open_button.grid(column=1, row=2)

add_watermark_button = Button(text="Add Watermark")
add_watermark_button.grid(column=1, row=3)

window.mainloop()
