import serial

class Display:
    def __init__(self, comPort):
        self.comPort = comPort
        self.SerialInit = True
        try:
            self.SerialPort = serial.Serial(comPort, 19200)
            self.SerialPort.close()
            self.SerialPort.open()
        except:
            print("Serial port failed")
            self.SerialInit = False

    def printCenter(self, STR1, STR2):
        if(not self.SerialInit):
            return False
        while(len(STR1) < 20 ):
            if(len(STR1) == 19):
                STR1 += " "
            else:
                 STR1 = " "+ STR1+" "
        while(len(STR2) < 20 ): 
            if(len(STR2) == 19):
                STR2 += " "
            else:
                STR2 = " "+STR2+" "
        
        output = STR1 + STR2
        self.SerialPort.write(bytes(output, "utf-8"))

    def printLeft(self, STR1, STR2):
        if(not self.SerialInit):
            return False
        while(len(STR1) < 20 ):
            STR1 += " "
        while(len(STR2) < 20 ):
            STR2 += " "

        output = STR1 + STR2
        self.SerialPort.write(bytes(output, "utf-8"))

    def printRight(self, STR1, STR2):
        if(not self.SerialInit):
            return False
        while(len(STR1) < 20 ):
            STR1 = " " + STR1
        while(len(STR2) < 20 ): 
            STR2 = " " + STR2
        
        output = STR1 + STR2
        self.SerialPort.write(bytes(output, "utf-8"))  

    def close(self):
        if(not self.SerialInit):
            return False
        self.SerialPort.close()