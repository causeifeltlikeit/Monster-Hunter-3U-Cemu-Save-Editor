from editAPI.saveEditorAPI import*

import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Entry
from tkinter import Button


global itemBoxTree
global root

filePath = ''
itemList = []
boxIndex = 1

def getFile():
    global itemList
    
    filePath = tk.filedialog.askopenfilename(title="Select Save File")

    openFile(filePath)
    itemList = getItemList()
    updateListboxTree()
    return filePath

def saveTheFile():
    saveFile('user2')
    
def itemBoxTreeCreator(tab):
    itemBoxTree = ttk.Treeview(tab,column = ('c1','c2','c3'),show='headings', height=5)
    itemBoxTree.pack(expand=1, fill="both")
    itemBoxTree.column("c1", anchor=tk.CENTER,width=80)
    itemBoxTree.heading("c1", text="Item Number")
    itemBoxTree.column("c2", anchor=tk.W,width=80)
    itemBoxTree.heading("c2", text="Item")
    itemBoxTree.column("c3", anchor=tk.W,width=80)
    itemBoxTree.heading("c3", text="Quantity")
    return itemBoxTree

def updateListboxTree():
    for i in itemBoxTree.get_children():
        itemBoxTree.delete(i)
    index = 1 + ((boxIndex-1) *100)
    for i in itemList:
        itemBoxTree.insert('', 'end', values=(index, i[0], i[1]))
        index = index + 1
        
def submit(top,curItem, quantityEntry):
    global itemList
    try:
        itemQuant = int(quantityEntry.get())
        index = itemBoxTree.item(curItem)['values'][0]-1
        #change tree
        itemBoxTree.item(curItem, values=(itemBoxTree.item(curItem)['values'][0], itemBoxTree.item(curItem)['values'][1], itemQuant))
        #change itemlist, not sure if strictly necessary but whatever
        itemList[index] = (itemList[index][0],itemQuant,itemList[index][2])
        #change overall save data
        changeItem(index,itemList[index][2],itemQuant)
        top.destroy()
    except:
        top.destroy()
    
   
def modifyItem(a):
    
    top = Toplevel(root)
    top.geometry("+%d+%d" %(root.winfo_x()+100,root.winfo_y()+100))
    
    
    curItem = itemBoxTree.focus()

    #itemEntry = Entry(top, width= 25)
    quantityEntry = Entry(top, width= 25)
    #itemEntry.pack()
    quantityEntry.pack()
   
    #Create a Button Widget in the Toplevel Window
    button= Button(top, text="Ok", command=lambda:submit(top,curItem, quantityEntry))
    button.pack(pady=5, side= tk.TOP)

root = tk.Tk()
root.title('MH3U Save File Editor')

#menus
menubar = Menu(root)
fileMenu = Menu(menubar,tearoff =0)
menubar.add_cascade(label ='File', menu = fileMenu) 
fileMenu.add_command(label ='Open File', command = getFile) 
fileMenu.add_command(label ='Save File', command = saveTheFile) 


#tabs
notebook = ttk.Notebook(root)
listBoxTab = ttk.Frame(notebook)
notebook.add(listBoxTab, text='Item Box')
notebook.pack(expand=1, fill="both")

itemBoxTree = itemBoxTreeCreator(listBoxTab)
itemBoxTree.bind('<Double-Button-1>', modifyItem)


root.config(menu = menubar)
root.geometry("500x300")
root.mainloop()