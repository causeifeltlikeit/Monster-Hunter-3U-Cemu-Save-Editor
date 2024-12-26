class equipment:
    def __init__(self, name, byte1, byte2, byte3):
        self.name = name
        self.byte1 = byte1
        self.byte2 = byte2
        self.byte2 = byte3
    
    def printequipment(self):
        print(self.name +' '+ str(self.byte1) + str(self.byte2) + ' ' + str(hex(self.byte1)) + str(hex(self.byte2)))

    def getName(self):
        return self.name
    
    def getByte1(self):
        return self.byte1
    
    def getByte2(self):
        return self.byte2
    
    def getByte3(self):
        return self.byte3