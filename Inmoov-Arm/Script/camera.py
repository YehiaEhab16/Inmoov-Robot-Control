##########################################################################################
####################### Project: Inmoov Arm Control                #######################
####################### Version: 1.5                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 03/12/2024                          #######################
##########################################################################################

# Camera class #

# Importing PySide packages
from PySide6.QtCore import QThread,Signal

# Importing Image Modules
import mediapipe as mp
import numpy as np
import cv2

# Camera Thread
class Camera(QThread):
    # Camera interface variables
    ImageUpdate = Signal(np.ndarray)

    # Camera rotate states
    RotateRight = 0
    RotateLeft = 1
    Mirror = 2

    # Camera modes
    ModeManual = 3
    ModeAutomatic = 4

    # Serial data
    ContractThumb,  RelaxThumb   = 'A', 'a'
    ContractIndex,  RelaxIndex   = 'B', 'b'
    ContractMiddle, RelaxMiddle  = 'C', 'c'
    ContractRing,   RelaxRing    = 'D', 'd'
    ContractLittle, RelaxLittle  = 'E', 'e'
    ContractWrist , RelaxWrist   = 'F', 'f'
    RelaxArray = [RelaxThumb, RelaxIndex, RelaxMiddle, RelaxRing, RelaxLittle, RelaxWrist]

    # Init camera class
    def __init__(self):
        super().__init__()
        self.mirror=False
        self.orientation=0
        self.mode=self.ModeManual
        self.data = self.RelaxArray.copy()

        # Fingers dictionary
        self.fingers = dict()
        self.mpHands = None 

    # Kill Thread
    def terminate(self):
        self.threadActive=False
        self.capture.release() # Release Camera
        super().terminate()

    # Set Camera URL
    def start(self, url:int=0) -> bool:
        self.url = url
        self.capture = cv2.VideoCapture(self.url, cv2.CAP_DSHOW) # Camera URL
        self.threadActive = self.capture.isOpened()
        super().start()
        return self.threadActive

    # Get data
    def getData(self):
        return self.data
    
    # Set manual or automatic mode
    def setMode(self, mode:int):
        self.mode=mode

    # Rotate Camera
    def rotate(self, direction:int):
        # Update orientation based on direction
        if direction == self.RotateRight:
            self.orientation = (self.orientation + 1) % 4
        elif direction == self.RotateLeft:
            self.orientation = (self.orientation - 1) % 4
        elif direction == self.Mirror:
            self.mirror = not self.mirror

    # Adjust camera orientation
    def adjustOrientation(self):
        # Apply mirror
        if self.mirror:
            self.frame = cv2.flip(self.frame, 1) 

        # Rotate frame based on updated orientation
        if self.orientation == 1:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_90_CLOCKWISE)
        elif self.orientation == 2:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_180)
        elif self.orientation == 3:
            self.frame = cv2.rotate(self.frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Main thread function
    def run(self):        
        # Mediapipe hand detection
        if self.mpHands is None:
            self.mpHands = mp.solutions.hands
            self.hands = self.mpHands.Hands(max_num_hands=2)
            self.mpDraw = mp.solutions.drawing_utils
        
        # Thread Loop
        while self.threadActive:
            ret, self.frame = self.capture.read()    # Read Camera
            if ret == False:
                continue
            
            # Adjsut mirror and rotate camera
            self.adjustOrientation()
            
            # Face Detection and Recognition
            if self.mode == self.ModeAutomatic:
                # Get Hands position
                self.getHandsPosition()

            # Display RGB Image
            Image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)                

            # Update Image
            self.ImageUpdate.emit(Image)

    # Get hands postions
    def getHandsPosition(self):
        # Initialize finger count variable
        fingerCount=0
        # Convert to RGB
        imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        # Detect Hands
        results = self.hands.process(imgRGB)
        # Show Detected Hands
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                # Get hand index to check label (left or right)
                handIndex = results.multi_hand_landmarks.index(handLms)
                handLabel = results.multi_handedness[handIndex].classification[0].label

                # Set variable to keep landmarks positions (x and y)
                handLandmarks = []
                self.mpDraw.draw_landmarks(self.frame,handLms,self.mpHands.HAND_CONNECTIONS)
                for id,lm in enumerate(handLms.landmark):
                    handLandmarks.append([lm.x, lm.y])
                    h,w,_ = self.frame.shape
                    cx,cy=int(lm.x * w), int(lm.y * h)
                    self.fingers[id]=[cx,cy]

                # Wrist
                if handLabel == "Left":
                    if handLandmarks[20][0] < handLandmarks[4][0]:
                        self.data[5]=self.RelaxWrist
                    else:
                        self.data[5]=self.ContractWrist
                        handLabel = "Right"

                elif handLabel == "Right":
                    if handLandmarks[20][0] > handLandmarks[4][0]:
                        self.data[5]=self.RelaxWrist
                    else:
                        self.data[5]=self.ContractWrist
                        handLabel = "Left"

                # Thumb
                if handLabel == "Left":
                    if handLandmarks[4][0] > handLandmarks[3][0]:
                        fingerCount = fingerCount+1
                        self.data[0]=self.RelaxThumb
                    else:
                        self.data[0]=self.ContractThumb
                elif handLabel == "Right":
                    if handLandmarks[4][0] < handLandmarks[3][0]:
                        fingerCount = fingerCount+1
                        self.data[0]=self.RelaxThumb
                    else:
                        self.data[0]=self.ContractThumb

                # Index finger
                if handLandmarks[8][1] < handLandmarks[6][1]:      
                    fingerCount = fingerCount+1
                    self.data[1]=self.RelaxIndex
                else:
                    self.data[1]=self.ContractIndex
                
                # Middle finger
                if handLandmarks[12][1] < handLandmarks[10][1]:
                    fingerCount = fingerCount+1
                    self.data[2]=self.RelaxMiddle
                else:
                    self.data[2]=self.ContractMiddle

                #Ring finger
                if handLandmarks[16][1] < handLandmarks[14][1]: 
                    fingerCount = fingerCount+1
                    self.data[3]=self.RelaxRing
                else:
                    self.data[3]=self.ContractRing
                
                 # Pinky Finger
                if handLandmarks[20][1] < handLandmarks[18][1]:
                    fingerCount = fingerCount+1
                    self.data[4]=self.RelaxLittle
                else:
                    self.data[4]=self.ContractLittle

        else:
            self.data = self.RelaxArray.copy()
        
        # Display finger count
        cv2.putText(self.frame, str(fingerCount), (30, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (20, 120, 255), 8)
