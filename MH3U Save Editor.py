from functions.saveEditorAPI import*

import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk

filePath = ''
itemList = []

def getFile():
    filePath = tk.filedialog.askopenfilename(title="Select Save File")
    print(filePath)
    openFile(filePath)
    return filePath

#menus
root = tk.Tk()
root.title('MH3U Save File Editor')
menubar = Menu(root)

fileMenu = Menu(menubar,tearoff =0)
menubar.add_cascade(label ='File', menu = fileMenu) 
fileMenu.add_command(label ='Open Save File', command = getFile) 
fileMenu.add_command(label ='testing', command = printItemList) 

#tabs
notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)


notebook.add(tab1, text='Item Box')
notebook.add(tab2, text='Character Details')
notebook.pack(expand=1, fill="both")


root.config(menu = menubar)
root.geometry("500x300")
root.mainloop()