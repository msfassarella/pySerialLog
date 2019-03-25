import time
import serial
import os


#ser = serial.Serial(port='/dev/ttyUSB0',baudrate=230400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=10)
portaSerial = False
while (portaSerial == False):
   tmp = os.popen('ls /dev/ttyUSB*').read()
   print (tmp)
   print('\r\n')
   lentmp =  len(tmp)
   tmp2 = tmp[:lentmp-2]
   print (tmp2)
   if tmp2 == '/dev/ttyUSB':
      portaSerial = True
   else:
      time.sleep(5)       
    #print('errado')
tmp = tmp[:12]
print('Porta encontrada\n')
time.sleep(10)

portaSerial = False
while (portaSerial == False):
   try:
      print('Abrindo: ' + tmp) 
      ser = serial.Serial(port=tmp,baudrate=230400,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=10)
      portaSerial = True
   except:
      time.sleep(2)
      #print ('abrindo ...\r\n')
        
arquivo = open('/home/pi/Desktop/arq01.txt','a')
while True:
   for i in range(10):
     # res = ser.readline()
      try:
         res = ser.readline()
      except serial.SerialException as e:
    #There is no new data from serial port
         ser.close()
         ser = serial.Serial(port='/dev/ttyUSB0',baudrate=230400, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=10)
         
    #     return None
      except TypeError as e:
    #Disconnect of USB->UART occured
         ser.close()
         ser = serial.Serial(port='/dev/ttyUSB0',baudrate=230400, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=10)
     #    return None
    #  else:
    #Some data was received
     #   return dataIn
      print(res)
      arquivo.write(res)
   arquivo.close()
   arquivo = open('/home/pi/Desktop/arq01.txt','a')
ser.close()
#arquivo.close()
