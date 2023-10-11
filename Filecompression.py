## import tk to create a tkinter app
import tkinter as tk
## import module filedialog from tkinter
from tkinter import filedialog
## import module zipfile
import zipfile
## import meesagebox module from tkinter
from tkinter import messagebox
import os

## function that handles the opening of file manager and ask user to select that file s/he wants to compress into zip file
def compress_file():
    ## gets the file and assign the path to filepath
    filepath = filedialog.askopenfilename()
    if not filepath:
        messagebox.showerror("Error", "No file selected")
        return
    ## open the file from filepath, append it with zip extension, set mode for writing
    with zipfile.ZipFile(filepath + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipObj:
        ## create and write the new zip file
        zipObj.write(filepath)
    ## display a message
    messagebox.showinfo("File was compressed successfully.")


## function that will handle file decompresion
def decompress_file():
    ## open the file that will be decompress and assign to filepath
    filepath = filedialog.askopenfilename()
    if not filepath:
        messagebox.showerror("Error", "No file selected")
        return
    ## pass filepath to ZipFile in read mode and assign object to zip_ref
    with zipfile.ZipFile(filepath, 'r') as zip_ref:
        ## use method extract from zipfile to decompress file
        destination = filedialog.askdirectory()
        zip_ref.extractall(path=destination)
    ## display a message
    messagebox.showinfo("File was decompressed successfully.")

## create tkinter object and assign to root variable
root = tk.Tk()
# button to click to select a file and calling method compress_file when clicked
compress_button = tk.Button(root, text="Select file to compress", command=compress_file)

## button to click to select a file and calling decompress_file method 
decompress_button = tk.Button(root, text="Select file to decompress", command=decompress_file)

compress_button.grid(row=0, column=0)
decompress_button.grid(row=1, column=0)

root.mainloop()