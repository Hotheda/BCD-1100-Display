import BCD1100

SERIALPORT = "COM7"

myDisplay = BCD1100.Display(SERIALPORT)

output1 = ""
output2 = ""

while( (output1 == "") or (len(output1) > 20 ) ): 
    output1 = input("Skriv nåt: ")
while( (output2 == "") or (len(output2) > 20 ) ): 
    output2 = input("Skriv nåt: ")

myDisplay.printCenter(output1, output2)

myDisplay.close()