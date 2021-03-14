import serial

class Display:
    def __init__(self, comPort):
        self.comPort = comPort
        self.SerialPort = serial.Serial(comPort, 19200)
        self.SerialPort.close()
        self.SerialPort.open()

    def printCenter(self, STR1, STR2):
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

    def close(self):
        self.SerialPort.close()