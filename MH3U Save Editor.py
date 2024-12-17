from editAPI.saveEditorAPI import*

import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from tkinter import ttk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import Entry
from tkinter import Button
from tkinter import Label

global itemBoxTree
global root

filePath = ''
itemList = []
boxIndex = 1

def getFile():
    global itemList
    filePath = tk.filedialog.askopenfilename(title="Select Save File")
    openFile(filePath)
    itemList = getItemList(boxIndex)
    updateListboxTree()

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
    global itemBoxTree
    for i in itemBoxTree.get_children():
        itemBoxTree.delete(i)
    index = 1 + ((boxIndex-1) *100)
    for i in itemList:
        itemBoxTree.insert('', 'end', values=(index, i[0], i[1]))
        index = index + 1
        
def modifyItem(a):
    #create popup window
    top = Toplevel(root)
    #center it on current window placement
    top.geometry("+%d+%d" %(root.winfo_x()+100,root.winfo_y()+100))
    curItem = itemBoxTree.focus()
    
    label1 = Label( top, text='Choose Item')
    label2 = Label( top, text='Choose Quantity')
    label1.grid(row = 0, column = 0, pady = 2)
    label2.grid(row = 1, column = 0, pady = 2)
    
    #Which Item Entry
    itemEntry = ttk.Combobox(top, values=getItemNameList())
    itemEntry.current(getItemNameList().index(itemBoxTree.item(curItem)['values'][1]))
    itemEntry.grid(row = 0, column = 1, pady = 2)
    
    #How Many Entry
    quantityEntry = ttk.Combobox(top, values=list(range(100)))
    quantityEntry.current(itemBoxTree.item(curItem)['values'][2])
    quantityEntry.grid(row = 1, column = 1, pady = 2)
    
    #Create a Button Widget in the Toplevel Window
    button= Button(top, text="Ok", command=lambda:itemBoxSubmit(top,quantityEntry,itemEntry,curItem))
    button.grid(row = 2, column = 1, pady = 2)
        
def itemBoxSubmit(top,quantityEntry,itemEntry,curItem):
    global itemList
    index = itemBoxTree.item(curItem)['values'][0]-1
    
    #change tree
    itemBoxTree.item(curItem, values=(itemBoxTree.item(curItem)['values'][0], getItemNameList()[itemEntry.current()], int(quantityEntry.current())))
    
    #change itemlist, not sure if strictly necessary but whatever
    itemList[index % 100] = (getItemNameList()[itemEntry.current()],int(quantityEntry.current()),getItemCodesFromIndex(itemEntry.current()))
    
    #change overall save data
    changeItem(index,getItemCodesFromIndex(itemEntry.current()),int(quantityEntry.current()))
    
    #kill popup
    top.destroy()

def changePage(a):
    global boxIndex
    global itemList
    boxIndex = boxNumber.current() + 1
    itemList = getItemList(boxIndex - 1)
    updateListboxTree()

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

#Create item box and bind to detect changes
itemBoxTree = itemBoxTreeCreator(listBoxTab)
itemBoxTree.bind('<Double-Button-1>', modifyItem)

#create box number chooser and bind to detect changes
boxNumber = ttk.Combobox(listBoxTab, values=list(range(1,11)))
boxNumber.current(0)
boxNumber.pack()
boxNumber.bind('<<ComboboxSelected>>', changePage)

root.config(menu = menubar)
root.geometry("500x300")
root.mainloop()