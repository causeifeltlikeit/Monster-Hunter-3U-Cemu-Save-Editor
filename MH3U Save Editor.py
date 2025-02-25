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
global equipmentBoxTree

global root
global playerNameEntry
global zennyEntry
    


filePath = ''
itemList = []
equipmentList = []
boxIndex = 1
eboxIndex = 1

def openFile():
    global itemList
    global equipmentList
    filePath = tk.filedialog.askopenfilename(title="Select Save File")
    openSaveFile(filePath)
    itemList = getItemList(boxIndex - 1)
    equipmentList = getEquipmentList(eboxIndex)
    playerInfoTabUpdater()
    updateListboxTree()
    updateEquipmentboxTree()

def saveFile():
    saveSaveFile('user2')
    
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

def equipmentBoxTreeCreator(tab):
    equipmentBoxTree = ttk.Treeview(tab,column = ('c1','c2','c3'),show='headings', height=5)
    equipmentBoxTree.pack(expand=1, fill="both")
    equipmentBoxTree.column("c1", anchor=tk.CENTER,width=80)
    equipmentBoxTree.heading("c1", text="Equipment Number")
    equipmentBoxTree.column("c2", anchor=tk.W,width=80)
    equipmentBoxTree.heading("c2", text="Type")
    equipmentBoxTree.column("c3", anchor=tk.W,width=80)
    equipmentBoxTree.heading("c3", text="Equipment")
    return equipmentBoxTree

def updateListboxTree():
    global itemBoxTree
    for i in itemBoxTree.get_children():
        itemBoxTree.delete(i)
    index = 1 + ((boxIndex-1) *100)
    for i in itemList:
        itemBoxTree.insert('', 'end', values=(index, i[0], i[1]))
        index = index + 1

def updateEquipmentboxTree():
    global equipmentBoxTree
    for i in equipmentBoxTree.get_children():
        equipmentBoxTree.delete(i)
    index = 1 + ((boxIndex-1) *100)
    for i in equipmentList:
        equipmentBoxTree.insert('', 'end', values=(index, getEquipmentType(i[1][0]), i[0]))
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
    itemEntry = ttk.Combobox(top, values=getItemListNames())
    itemEntry.current(getItemListNames().index(itemBoxTree.item(curItem)['values'][1]))
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
    itemBoxTree.item(curItem, values=(itemBoxTree.item(curItem)['values'][0], getItemListNames()[itemEntry.current()], int(quantityEntry.current())))
    #change itemlist, not sure if strictly necessary but whatever
    itemList[index % 100] = (getItemListNames()[itemEntry.current()],int(quantityEntry.current()))
    #change overall save data
    changeItem(index,getItemListNames()[itemEntry.current()],int(quantityEntry.current()))
    #kill popup
    top.destroy()
    
def modifyEquipment(a):
    #create popup window
    top = Toplevel(root)
    #center it on current window placement
    top.geometry("+%d+%d" %(root.winfo_x()+100,root.winfo_y()+100))
    curItem = equipmentBoxTree.focus()
    label1 = Label( top, text='Choose Equipment Type')
    label2 = Label( top, text='Choose Equipment')
    label3 = Label( top, text='Choose Skill One')
    label4 = Label( top, text='Choose Skill Two')
    label5 = Label( top, text='Slots?')
    label1.grid(row = 0, column = 0, pady = 2)
    label2.grid(row = 1, column = 0, pady = 2)
    label3.grid(row = 2, column = 0, pady = 2)
    label4.grid(row = 3, column = 0, pady = 2)
    label5.grid(row = 5, column = 0, pady = 2)
    
    typeChoose = ttk.Combobox(top, values=getEquipmentTypeList())
    #typeChoose.current(getItemNameList().index(itemBoxTree.item(curItem)['values'][1]))
    typeChoose.grid(row = 0, column = 1, pady = 2)

def changePage(a):
    global boxIndex
    global itemList
    boxIndex = boxNumber.current() + 1
    itemList = getItemList(boxIndex - 1)
    updateListboxTree()

def echangePage(a):
    global eboxIndex
    global equipmentList
    eboxIndex = eboxNumber.current() + 1
    equipmentList = getEquipmentList(eboxIndex)
    print(eboxIndex)
    updateEquipmentboxTree()
    
def playerInfoTabCreator(playerInfoTab):
    global playerNameEntry
    global zennyEntry
    label1 = Label( playerInfoTab, text='Player Name')
    label2 = Label( playerInfoTab, text='Zenny Amount')
    playerNameEntry = tk.Entry(playerInfoTab)
    zennyEntry = tk.Entry(playerInfoTab)
    label1.grid(row = 0, column = 0, pady = 2)
    label2.grid(row = 1, column = 0, pady = 2)
    playerNameEntry.grid(row = 0, column = 1, pady = 2)
    zennyEntry.grid(row = 1, column = 1, pady = 2)
    submitButton = Button(playerInfoTab, text="Change", command=changePlayerInfo)
    submitButton.grid(row=2, column=0)

def playerInfoTabUpdater():
    global playerNameEntry
    global zennyEntry
    playerNameEntry.delete(0,tk.END)
    playerNameEntry.insert(0,getPlayerName())
    zennyEntry.delete(0,tk.END)
    zennyEntry.insert(0,str(getZennyAmount()))

def changePlayerInfo():
    changePlayerName(str(playerNameEntry.get()))
    changeZennyAmount(int(zennyEntry.get()))
    
    
    
root = tk.Tk()
root.title('MH3U Save File Editor')

#menus
menubar = Menu(root)
fileMenu = Menu(menubar,tearoff =0)
menubar.add_cascade(label ='File', menu = fileMenu) 
fileMenu.add_command(label ='Open File', command = openFile) 
fileMenu.add_command(label ='Save File', command = saveFile) 


#tabs
notebook = ttk.Notebook(root)

#Player into tab
playerInfoTab = ttk.Frame(notebook)
notebook.add(playerInfoTab, text='Player Info')
playerInfoTabCreator(playerInfoTab)

#Item List Box Tab
listBoxTab = ttk.Frame(notebook)
notebook.add(listBoxTab, text='Item Box')
#Create item box and bind to detect changes
itemBoxTree = itemBoxTreeCreator(listBoxTab)
itemBoxTree.bind('<Double-Button-1>', modifyItem)
#create box number chooser and bind to detect changes
boxNumber = ttk.Combobox(listBoxTab, values=list(range(1,11)))
boxNumber.current(0)
boxNumber.pack()
boxNumber.bind('<<ComboboxSelected>>', changePage)

#Equipment List Box Tab
equipmentBoxtab = ttk.Frame(notebook)
notebook.add(equipmentBoxtab, text='Equipment Box')
#Create item box and bind to detect changes
equipmentBoxTree = equipmentBoxTreeCreator(equipmentBoxtab)
equipmentBoxTree.bind('<Double-Button-1>', modifyEquipment)
eboxNumber = ttk.Combobox(equipmentBoxtab, values=list(range(1,11)))
eboxNumber.current(0)
eboxNumber.pack()
eboxNumber.bind('<<ComboboxSelected>>', echangePage)


notebook.pack(expand=1, fill="both")
root.config(menu = menubar)
root.geometry("500x300")
root.mainloop()