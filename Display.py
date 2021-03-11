import serial
import time

output1 = ""
output2 = ""
while( (output1 == "") or (len(output1) > 20 ) ): 
    output1 = input("Skriv nåt: ")
while( (output2 == "") or (len(output2) > 20 ) ): 
    output2 = input("Skriv nåt: ")

while(len(output1) < 20 ):
    if(len(output1) == 19):
        output1 += " "
    else:
        output1 = " "+output1+" "
while(len(output2) < 20 ): 
    if(len(output2) == 19):
        output2 += " "
    else:
        output2 = " "+output2+" "

print("Lenght string 1: " + str(len(output1)) )
print("Lenght string 2: " + str(len(output2)) )


serPort = serial.Serial("COM7", 19200)
serPort.close()
serPort.open()

serPort.write(bytes(output1, "utf-8"))
serPort.write(bytes(output2, "utf-8"))

serPort.close()