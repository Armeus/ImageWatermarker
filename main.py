import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps


def image_select():
    try:
        # On button click will prompt user to select an image file
        filename = filedialog.askopenfilename(filetypes=[('image files', '.png .jpg')])
        starting_image = Image.open(filename)
        # Once file is selected it will update the GUI to show the selected image
        update_thumbnail(starting_image)
        # Update label and buttons to next step
        wm_label.config(text='Choose your Watermark')
        back_button.pack()
        next_button.config(command=lambda: wm_select(starting_image))
    except AttributeError:
        tk.messagebox.showerror(title='Error', message='No File Selected')


def wm_select(updated_image):
    try:
        # Only allow .pngs due to watermark needing to have transparency
        filename = filedialog.askopenfilename(filetypes=[('image files', '.png')])
        wm_im = ImageOps.contain(Image.open(filename), updated_image.size)
        updated_image.paste(wm_im, (0, 0), wm_im)
        update_thumbnail(updated_image)
        # Update label and buttons to prompt user to save updated image
        wm_label.config(text='Image Watermarked!')
        next_button.config(text='Save Image', command=lambda: save_image(updated_image))
    except AttributeError:
        tk.messagebox.showerror(title='Error', message='No File Selected')


# Updates label with current image thumbnail
def update_thumbnail(image):
    im_thumbnail = ImageOps.contain(image, size=(200, 200))
    photo = ImageTk.PhotoImage(im_thumbnail)
    im_label.config(image=photo)
    im_label.img = photo


# Prompts user to save image as
def save_image(output_image):
    try:
        filename = filedialog.asksaveasfilename(defaultextension='.png',
                                                filetypes=[('image files', '.png .jpg'), ('all files', '*.*')])
        output_image.save(filename, format='PNG')
    except FileNotFoundError:
        tk.messagebox.showerror(title='Error', message='File Not Found')



# Reverts GUI to initial state, allowing user to start from beginning
def go_back():
    im_label.config(image='')
    wm_label.config(text='Upload an Image')
    next_button.config(text='Select File', command=image_select)
    back_button.pack_forget()


# Initialize GUI with using Tkinter
window = tk.Tk()
window.title("Image Watermarker")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20, background='grey')

# Create labels used
im_label = tk.Label(background='grey')
im_label.pack()
wm_label = tk.Label(text="Upload an Image", font=("Ariel", 24, "bold"), background='grey')
wm_label.pack()
wm_label.config(padx=20, pady=20)

# Create initial buttons to select file
next_button = tk.Button(window, text='Select File', command=image_select,
                   width=10, height=2, background='light grey')
next_button.pack()
back_button = tk.Button(window, text='Go Back', command=go_back, width=10, height=2, background='light grey')

window.mainloop()
