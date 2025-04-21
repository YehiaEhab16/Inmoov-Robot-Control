##########################################################################################
####################### Project: Inmoov Head Control               #######################
####################### Version: 1.7                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 11/01/2025                          #######################
##########################################################################################

# Serial Functions #

# Importing PySide packages
from PySide6.QtCore import QThread

# Importing Serial and Time modules
import serial
import time
import re

# Importing defined modules
from path import PathManager

# Communication Thread
class Communication(QThread):
    Arduino = None
    # Time Steps
    ManualTimeStep = 10
    AutoTimeStep   = 0.01

    # Order of sending
    Neck    = 0
    Jaw     = 1
    EyesHor = 2
    EyesVer = 3
    Lids    = 4

    # Serial data
    NeckRight , NeckLeft, NeckAngle    = 'r', 'l', 'N'
    JawUp     , JawDown , JawAngle     = 'u', 'd', 'J'
    LidOpen   , LidClose, LidsAngle    = 'O', 'C', 'a'
    EyesRight , EyesLeft, EyesHorAngle = 'R', 'L', 'E'
    EyesUp    , EyesDown, EyesVerAngle = 'U', 'D', 'e'
    StartSpeak, EndSpeak, Stop         = 'S', 's', 'A'

    # Angles list
    Angles = [NeckAngle, JawAngle, EyesHorAngle, EyesVerAngle, LidsAngle]

    # Motors minimum and maximumvalues
    EyesHorMin, EyesVerMin, NeckMin, JawMin, LidsMin = 30 , 60 , 0  , 0  , 0
    EyesHorMax, EyesVerMax, NeckMax, JawMax, LidsMax = 150, 120, 180, 180, 60

    # Motors default values
    JawDefault     = JawMin
    LidsDefault    = LidsMin
    NeckDefault    = ( NeckMin    + NeckMax    ) / 2
    EyesHorDefault = ( EyesHorMin + EyesHorMax ) / 2 
    EyesVerDefault = ( EyesVerMin + EyesVerMax ) / 2

    # Error States
    InitSuccess        = 0
    StopSuccess        = 1
    InitFailure        = 2
    StopFailure        = 3
    AlreadyInitialized = 4
    AlreadyStopped     = 5

    # Initailize class variables
    def __init__(self, dataContainer1 = None, dataContainer2 = None):
        super().__init__()
        self.threadActive = False
        self.dataContainer1 = dataContainer1
        self.dataContainer2 = dataContainer2

    # Update Servo Ranges 
    def updateConfigs(self) -> bool:
        try:
            with open(PathManager.InmoovConfigPath, 'r') as f:
                content = f.read()

            # Regular expressions to extract minimum values
            NeckMin    = re.search(r'#define\s+NECK_MIN\s+(\d+)', content)
            JawMin     = re.search(r'#define\s+JAW_MIN\s+(\d+)', content)
            LidsMin    = re.search(r'#define\s+LID_MIN\s+(\d+)', content)
            EyesHorMin = re.search(r'#define\s+EYES_H_MIN\s+(\d+)', content)
            EyesVerMin = re.search(r'#define\s+EYES_V_MIN\s+(\d+)', content)

            # Regular expressions to extract maximum values
            NeckMax    = re.search(r'#define\s+NECK_MAX\s+(\d+)', content)
            JawMax     = re.search(r'#define\s+JAW_MAX\s+(\d+)', content)
            LidsMax    = re.search(r'#define\s+LID_MAX\s+(\d+)', content)
            EyesHorMax = re.search(r'#define\s+EYES_H_MAX\s+(\d+)', content)
            EyesVerMax = re.search(r'#define\s+EYES_V_MAX\s+(\d+)', content)

            # Assigning minimum values
            Communication.NeckMin    = int(NeckMin.group(1))    if NeckMin    else None
            Communication.JawMin     = int(JawMin.group(1))     if JawMin     else None
            Communication.LidsMin    = int(LidsMin.group(1))    if LidsMin    else None
            Communication.EyesHorMin = int(EyesHorMin.group(1)) if EyesHorMin else None
            Communication.EyesVerMin = int(EyesVerMin.group(1)) if EyesVerMin else None

            # Assigning maximum values
            Communication.NeckMax    = int(NeckMax.group(1))    if NeckMax    else None
            Communication.JawMax     = int(JawMax.group(1))     if JawMax     else None
            Communication.LidsMax    = int(LidsMax.group(1))    if LidsMax    else None
            Communication.EyesHorMax = int(EyesHorMax.group(1)) if EyesHorMax else None
            Communication.EyesVerMax = int(EyesVerMax.group(1)) if EyesVerMax else None

            # Updating defaults
            Communication.JawDefault = Communication.JawMin
            Communication.LidsDefault = Communication.LidsMin
            Communication.NeckDefault = (Communication.NeckMin + Communication.NeckMax) / 2
            Communication.EyesHorDefault = (Communication.EyesHorMin + Communication.EyesHorMax) / 2
            Communication.EyesVerDefault = (Communication.EyesVerMin + Communication.EyesVerMax) / 2

            # Succesful update
            return True
        
        # Error while parsing data
        except:
            return False

    # Connect to arduino
    def connect(self, num: str) -> int:
        try:
            if not Communication.Arduino:
                Communication.Arduino = serial.Serial(f'COM{num}', baudrate=115200, timeout=1) # Open serial port
                return self.InitSuccess
            else:
                return self.AlreadyInitialized
        except:
            return self.InitFailure

    # Send Data to Arduino
    def sendData(self, data: str | list[str]) -> bool:
        try:
            if Communication.Arduino:
                if type(data) == list:
                    data = ''.join([d + a for d, a in zip(data, self.Angles)])
                Communication.Arduino.write(bytes(data, 'utf-8')) # Write to serial port
            return True
        except:
            return False

    # Stop Communication
    def stop(self) -> int:
        try:
            if Communication.Arduino:
                Communication.Arduino.close() # Close Serial Port
                Communication.Arduino = None
                return self.StopSuccess
            else:
                return self.AlreadyStopped
        except:
            return self.StopFailure
    
    # Main thread function
    def run(self):
        self.threadActive = True
        while self.threadActive:
            if self.dataContainer2:
                self.sendData(max(self.dataContainer1.data, self.dataContainer2.data))
            else:
                self.sendData(self.dataContainer1.data)
            time.sleep(self.AutoTimeStep)
    
    # Terminate thread
    def terminate(self):
        self.threadActive = False
        super().terminate()