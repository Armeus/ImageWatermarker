# Imports
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps


class App(tk.Frame):
    # Initialize GUI with using Tkinter
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # Create labels used
        self.im_label = tk.Label(background='grey')
        self.im_label.pack()
        self.wm_label = tk.Label(text="Upload an Image", font=("Ariel", 24, "bold"), background='grey')
        self.wm_label.pack()
        self.wm_label.config(padx=20, pady=20)
        # Create buttons used
        self.next_button = tk.Button(parent, text='Select File', command=self.image_select,
                                     width=10, height=2, background='light grey')
        self.next_button.pack()
        self.back_button = tk.Button(parent, text='Go Back', command=self.go_back,
                                     width=10, height=2, background='light grey')

    # Prompts user to select initial image and updates GUI for next step
    def image_select(self):
        try:
            # On button click will prompt user to select an image file
            filename = filedialog.askopenfilename(filetypes=[('image files', '.png .jpg')])
            starting_image = Image.open(filename)
            # Once file is selected it will update the GUI to show the selected image
            self.update_thumbnail(starting_image)
            # Update label and buttons to next step
            self.wm_label.config(text='Choose your Watermark')
            self.back_button.pack()
            self.next_button.config(command=lambda: self.wm_select(starting_image))
        except AttributeError:
            tk.messagebox.showerror(title='Error', message='No File Selected')

    # Prompts user to select watermark template and updates GUI for final step
    def wm_select(self, updated_image):
        try:
            # Only allow .pngs due to watermark needing to have transparency
            filename = filedialog.askopenfilename(filetypes=[('image files', '.png')])
            wm_im = ImageOps.contain(Image.open(filename), updated_image.size)
            updated_image.paste(wm_im, (0, 0), wm_im)
            self.update_thumbnail(updated_image)
            # Update label and buttons to prompt user to save updated image
            self.wm_label.config(text='Image Watermarked!')
            self.next_button.config(text='Save Image', command=lambda: self.save_image(updated_image))
        except AttributeError:
            tk.messagebox.showerror(title='Error', message='No File Selected')

    # Updates label with current image thumbnail
    def update_thumbnail(self, image):
        im_thumbnail = ImageOps.contain(image, size=(200, 200))
        photo = ImageTk.PhotoImage(im_thumbnail)
        self.im_label.config(image=photo)
        self.im_label.img = photo

    # Prompts user to save image as
    def save_image(self, output_image):
        try:
            filename = filedialog.asksaveasfilename(defaultextension='.png',
                                                    filetypes=[('image files', '.png .jpg'), ('all files', '*.*')])
            output_image.save(filename, format='PNG')
        except FileNotFoundError:
            tk.messagebox.showerror(title='Error', message='File Not Found')

    # Reverts GUI to initial state, allowing user to start from beginning
    def go_back(self):
        self.im_label.config(image='')
        self.wm_label.config(text='Upload an Image')
        self.next_button.config(text='Select File', command=self.image_select)
        self.back_button.pack_forget()


def main():
    root = tk.Tk()
    root.title("Image Watermarker")
    root.minsize(width=500, height=300)
    root.config(padx=20, pady=20, background='grey')
    App(root).pack(expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
