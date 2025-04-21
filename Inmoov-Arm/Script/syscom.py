##########################################################################################
####################### Project: Inmoov Arm Control                #######################
####################### Version: 1.5                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 03/12/2024                          #######################
##########################################################################################

# Serial Functions #

# Importing PySide packages
from PySide6.QtCore import QThread

# Importing Serial and Time modules
import serial
import time

# Communication Thread
class Communication(QThread):
    # Time Steps
    ManualTimeStep  = 10
    AutoTimeStep    = 0.15

    # Serial data
    ContractThumb,  RelaxThumb   = 'T', 't'
    ContractIndex,  RelaxIndex   = 'I', 'i'
    ContractMiddle, RelaxMiddle  = 'M', 'm'
    ContractRing,   RelaxRing    = 'R', 'r'
    ContractLittle, RelaxLittle  = 'L', 'l'
    ContractWrist , RelaxWrist   = 'Y', 'y'
    StopCommunication = 'Z'

    # Error States
    ComInitSuccess        = 0
    ComStopSuccess        = 1
    ComInitFailure        = 2
    ComStopFailure        = 3
    ComAlreadyInitialized = 4
    ComAlreadyStopped     = 5

    # Initailize class variables
    def __init__(self, dataContainer):
        super().__init__()
        self.threadActive=False
        self.arduino=None
        self.dataContainer = dataContainer

    # Connect to arduino
    def connect(self, num:str) -> int:
        try:
            if self.arduino is None:
                self.arduino = serial.Serial(f'COM{num}', baudrate=115200, timeout=1) # Open serial port
                return self.ComInitSuccess
            else:
                return self.ComAlreadyInitialized
        except:
            return self.ComInitFailure

    # Send Data to Arduino
    def sendData(self, data:str) -> bool:
        try:
            if self.arduino is not None:
                self.arduino.write(bytes(data, 'utf-8')) # Write to serial port
            return True
        except:
            return False

    # Stop Communication
    def stop(self) -> int:
        try:
            if self.arduino is not None:
                self.arduino.close() # Close Serial Port
                self.arduino = None
                return self.ComStopSuccess
            else:
                return self.ComAlreadyStopped
        except:
            return self.ComStopFailure
    
    # Main thread function
    def run(self):
        self.threadActive = True
        while self.threadActive:
            self.sendData(''.join(self.dataContainer.data))
            time.sleep(self.AutoTimeStep)
    
    # Terminate thread
    def terminate(self):
        self.threadActive=False
        super().terminate()
