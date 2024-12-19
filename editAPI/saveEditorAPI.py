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

def changePlayerName(changedName):
    global saveFileData
    characters = list(changedName)
    offset = nameOffset
    for i in characters:
        saveFileData[offset] = int.from_bytes(i.encode('utf-8'))
        offset = offset + 1
    
    while (offset < nameOffset + 10):
        saveFileData[offset] = 0
        offset = offset + 1

def getPlayerName():
    name = saveFileData[nameOffset:nameOffset + 10]
    return name.decode()
    
    
def getItemList(pageNumber):
    tempList = []
    offset = itemBoxOffset + ( 4 * pageNumber * 100)
    for i in range(pageNumber * 100,(pageNumber * 100)+100):
        tempList.append((str(itemList[(saveFileData[offset],saveFileData[offset+1])].name), saveFileData[offset+3],(saveFileData[offset],saveFileData[offset+1])))
        offset = offset + 4
    return tempList

def changeItem(itemLocation, itemID, itemQuantity):
    global saveFileData
    offset = itemBoxOffset + (4*itemLocation)
    saveFileData[offset] = itemList[itemID].byte1
    saveFileData[offset + 1] = itemList[itemID].byte2
    saveFileData[offset + 3] = itemQuantity
    
def getZennyAmount():
    return int.from_bytes(saveFileData[zennyOffset].to_bytes() + saveFileData[zennyOffset + 1].to_bytes() + saveFileData[zennyOffset + 2].to_bytes())

def changeZennyAmount(value):
    global saveFileData
    valueBytes = bytearray(value.to_bytes(3))
    offset = zennyOffset
    for i in valueBytes:
        saveFileData[offset] = i
        offset = offset + 1