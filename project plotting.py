import serial 
import numpy  
import matplotlib.pyplot as plt 
from drawnow import *

tempC= []
pressure=[]
arduinoData = serial.Serial('com7', 115200) 
plt.ion() 
cnt=0

def makeFig(): 
    plt.ylim(23,35)                                 
    plt.title('Live Streaming Sensor Data')         
    plt.grid(True)                                  
    plt.ylabel('Temperature C')                            
    plt.plot(tempC, 'ro-', label='Degrees C')       
    plt.legend(loc='upper left')                   
    plt2=plt.twinx()                                
    plt.ylim(1009,1015)                         
    plt2.plot(pressure, 'b^-', label='Pressure (Pa)') 
    plt2.set_ylabel('Pressrue (Pa)')                    
    plt2.ticklabel_format(useOffset=False)         
    plt2.legend(loc='upper right')                 
    

while True: 
    while (arduinoData.inWaiting()==0):
        pass 
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.decode().split(',')  
    temp = float( dataArray[0])           
    P =    float( dataArray[1])        
    tempC.append(temp)  
    pressure.append(P) 
    drawnow(makeFig)  
    plt.pause(.000001)     
    cnt=cnt+1
    if(cnt>50):                   
        tempC.pop(0)               
        pressure.pop(0)
        