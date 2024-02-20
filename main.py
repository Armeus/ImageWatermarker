import tkinter as tk
from tkinter import filedialog, PhotoImage
from PIL import Image, ImageTk, ImageOps


def image_select():
    # On button click will prompt user to select an image file
    filename = filedialog.askopenfilename(filetypes=[('image files', '.png .jpg')])
    starting_image = Image.open(filename)
    # Once file is selected it will update the GUI to show the selected image
    update_thumbnail(starting_image)
    # Update label and buttons to next step
    wm_label.config(text='Choose your Watermark')
    button.config(command=lambda: wm_select(starting_image))


def wm_select(updated_image):
    # Only allow .pngs due to watermark needing to have transparency
    filename = filedialog.askopenfilename(filetypes=[('image files', '.png')])
    wm_im = ImageOps.contain(Image.open(filename), updated_image.size)
    updated_image.paste(wm_im, (0, 0), wm_im)
    update_thumbnail(updated_image)
    # Update label and buttons to prompt user to save updated image
    wm_label.config(text='Image Watermarked!')
    button.config(text='Save Image', command=lambda: save_image(updated_image))


# Updates label with current image thumbnail
def update_thumbnail(image):
    im_thumbnail = ImageOps.contain(image, size=(200, 200))
    photo = ImageTk.PhotoImage(im_thumbnail)
    im_label.config(image=photo)
    im_label.img = photo


def save_image(output_image):
    filename = filedialog.asksaveasfilename(initialfile='.png', filetypes=[('image files', '.png .jpg'), ('all files', '*.*')])
    output_image.save(filename, format='PNG')


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

# Create initial button to select file
button = tk.Button(window, text='Select File', command=image_select,
                   width=10, height=2, background='light grey')
button.pack()

window.mainloop()
