from data.offsets import *
from data.itemCodes import *

saveFileData = None

def openFile(fileName):
    global saveFileData
    with open(fileName,"rb") as f:
        data = f.read()
    saveFileData = bytearray(data)

def saveFile(fileName):
    f = open(fileName, "wb")
    f.write(saveFileData)
    f.close()

def changeName(changedName):
    global saveFileData
    characters = list(changedName)
    offset = nameOffset
    for i in characters:
        saveFileData[offset] = int.from_bytes(i.encode('utf-8'))
        offset = offset + 1
    
    while (offset < 53):
        saveFileData[offset] = 0
        offset = offset + 1
    
def printItemList():
    offset = itemBoxOffset
    for i in range(1,1000):
        print(str(itemList[(saveFileData[offset],saveFileData[offset+1])].name) + ' ' + str(saveFileData[offset+3]))
        offset = offset + 4
        
def changeItem(itemLocation, itemID, itemQuantity):
    global saveFileData
    offset = itemBoxOffset + (4*itemLocation)
    saveFileData[offset] = itemList[itemID].byte1
    saveFileData[offset + 1] = itemList[itemID].byte2
    saveFileData[offset + 3] = itemQuantity
    
def printZennyAmount():
    print(int.from_bytes(saveFileData[zennyOffset].to_bytes() + saveFileData[zennyOffset + 1].to_bytes() + saveFileData[zennyOffset + 2].to_bytes()))

def changeZennyAmount(value):
    global saveFileData
    valueBytes = bytearray(value.to_bytes(3))
    offset = zennyOffset
    for i in valueBytes:
        saveFileData[offset] = i
        offset = offset + 1

#openFile('user1')
#printItemList()