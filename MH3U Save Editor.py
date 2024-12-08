from functions.saveEditorAPI import*

import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk

filePath = ''
itemList = []

def getFile():
    global itemList
    filePath = tk.filedialog.askopenfilename(title="Select Save File")
    print(filePath)
    openFile(filePath)
    itemList = getItemList()
    updateListbox()
    return filePath

def updateListbox():
    itemListBox.delete(0,'end')
    index = 1
    print(itemList)
    for i in itemList:
        itemListBox.insert(index,i)
        index=index+1

#menus
root = tk.Tk()
root.title('MH3U Save File Editor')
menubar = Menu(root)

fileMenu = Menu(menubar,tearoff =0)
menubar.add_cascade(label ='File', menu = fileMenu) 
fileMenu.add_command(label ='Open Save File', command = getFile) 

#tabs
notebook = ttk.Notebook(root)

listBoxTab = ttk.Frame(notebook)
notebook.add(listBoxTab, text='Item Box')

global itemListBox
itemListBox = tk.Listbox(listBoxTab)
itemListBox.pack()

notebook.pack(expand=1, fill="both")


root.config(menu = menubar)
root.geometry("500x300")
root.mainloop()