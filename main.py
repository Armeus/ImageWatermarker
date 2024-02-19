import tkinter as tk
from tkinter import filedialog


def file_select():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)


window = tk.Tk()
window.title("Image Watermarker")
window.minsize(width=200, height=175)
window.config(padx=20, pady=20, background='grey')

wm_label = tk.Label(text="Add a Watermark", font=("Ariel", 24, "bold"), background='grey')
wm_label.pack()
wm_label.config(padx=20, pady=20)

button = tk.Button(window, text='Select File', command=file_select,
                   width=10, height=2, background='light grey')
button.pack()

window.mainloop()
