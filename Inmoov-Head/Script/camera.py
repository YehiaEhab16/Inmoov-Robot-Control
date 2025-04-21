##########################################################################################
####################### Project: Inmoov Head Control               #######################
####################### Version: 1.7                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 11/01/2025                          #######################
##########################################################################################

# Camera class #

# Importing PySide packages
from PySide6.QtCore import QThread, Signal

# Importing Image Modules
import mediapipe as mp
import numpy as np
import cv2

# Importing defined modules
from syscom import Communication as Com

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

    # Camera Indeces
    FirstCamera = 5
    SecondCamera = 6

    # Update config fladg
    ConfigsUpdated = False

    # Init camera class
    def __init__(self):
        super().__init__()
        self.mirror=False
        self.orientation=0
        self.mode = self.ModeManual
        self.data = list(map(str, [Com.NeckMin, Com.JawMin, Com.EyesHorMin, Com.EyesVerMin, Com.LidsMin]))

    # Kill Thread
    def terminate(self):
        self.threadActive=False
        self.capture.release() # Release Camera
        super().terminate()

    # Set Camera URL
    def start(self, url: int = 0) -> bool:
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
        # Mediapipe face and hand detection
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1)
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = mp.solutions.face_detection.FaceDetection()

        # Udate Servo Ranges
        if not Camera.ConfigsUpdated:
            Camera.ConfigsUpdated = True
            Camera.ConfigsUpdated = Com().updateConfigs()
        
        # Thread Loop
        while self.threadActive:
            ret, self.frame = self.capture.read()    # Read Camera
            if ret == False:
                continue
            
            # Adjsut mirror and rotate camera
            self.adjustOrientation()
            
            # Face Detection and Recognition
            if self.mode == self.ModeAutomatic:
                # Convert to RGB
                self.height, self.width, _ = self.frame.shape
                imgRGB = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # Get Hands position
                self.getFacePosition(imgRGB)
                self.getHandsPosition(imgRGB)

            # Display RGB Image
            self.ImageUpdate.emit(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    # Get face postions
    def getFacePosition(self, imgRGB: np.ndarray):
        # Detect the faces
        results = self.faceDetection.process(imgRGB)

        # Show Detected Faces
        if results.detections:
            # Get boundary box of face with highest detection score
            bboxC = sorted(results.detections, key=lambda detection: detection.score[0], reverse=True)[0].location_data.relative_bounding_box
            x, y, w, h = int(bboxC.xmin * self.width), int(bboxC.ymin * self.height), int(bboxC.width * self.width), int(bboxC.height * self.height)

            # Draw Boundary Box around face
            cv2.rectangle(self.frame, (x, y), (x + w, y + h), (20, 120, 255), 2)

            # Send data according to position
            self.data[Com.Neck] = str(int(np.clip(np.interp(x + w // 2, [60, 500], [Com.NeckMin, Com.NeckMax]), Com.NeckMin, Com.NeckMax)))
        else:
            self.data[Com.Neck] = str(int(Com.NeckDefault))
        
        # Display head direction
        cv2.putText(self.frame, f'Head: {self.data[Com.Neck]}', (10, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20, 120, 255), 2, cv2.LINE_AA)

    # Get hands postions
    def getHandsPosition(self, imgRGB: np.ndarray):
        # Detect Hands
        results = self.hands.process(imgRGB)
        # Show Detected Hands
        if results.multi_hand_landmarks:
            # Loop on available landmarks
            for handLms in results.multi_hand_landmarks:
                # Convert landmark positions to pixel values
                tx, ty = int(handLms.landmark[4].x * self.width), int(handLms.landmark[4].y * self.height)
                ix, iy = int(handLms.landmark[8].x * self.width), int(handLms.landmark[8].y * self.height)
                
                # Calculate distnace between index and thumb
                distance = np.sqrt((ix - tx)**2 + (iy - ty)**2)
                
                # Draw hand landmarks
                self.mpDraw.draw_landmarks(self.frame, handLms, self.mpHands.HAND_CONNECTIONS)
                if handLms.landmark[8].y < handLms.landmark[5].y and handLms.landmark[12].y < handLms.landmark[9].y and handLms.landmark[16].y > handLms.landmark[13].y and handLms.landmark[20].y > handLms.landmark[17].y:
                    self.data[Com.EyesHor] = str(int(np.clip(np.interp(ix, [60, 500], [Com.EyesHorMin, Com.EyesHorMax]), Com.EyesHorMin, Com.EyesHorMax)))
                    self.data[Com.EyesVer] = str(int(np.clip(np.interp(iy, [40, 300], [Com.EyesVerMax, Com.EyesVerMin]), Com.EyesVerMin, Com.EyesVerMax)))
                    self.data[Com.Lids]    = str(int(Com.LidsDefault))
                    
                    # Draw thumb index
                    cv2.circle(self.frame, (ix, iy), 7, (255, 0, 0), cv2.FILLED)
                elif  handLms.landmark[8].y < handLms.landmark[5].y and handLms.landmark[12].y > handLms.landmark[9].y and handLms.landmark[16].y > handLms.landmark[13].y and handLms.landmark[20].y > handLms.landmark[17].y:
                    self.data[Com.EyesHor], self.data[Com.EyesVer] = str(int(Com.EyesHorDefault)), str(int(Com.EyesVerDefault))
                    self.data[Com.Lids] = str(int(np.clip(np.interp(distance, [20, 200], [Com.LidsMax, Com.LidsMin]), Com.LidsMin, Com.LidsMax)))

                    # Draw line between index and thumb
                    cv2.line(self.frame, (tx, ty), (ix, iy), (20, 120, 255), 3)
                    cv2.circle(self.frame, (tx, ty), 5, (0, 255, 0), cv2.FILLED)
                    cv2.circle(self.frame, (ix, iy), 5, (0, 255, 0), cv2.FILLED) 
        else:
            self.data[Com.EyesHor], self.data[Com.EyesVer], self.data[Com.Lids] = str(int(Com.EyesHorDefault)), str(int(Com.EyesVerDefault)), str(int(Com.LidsDefault))
            
        # Display eyes and lids direction
        cv2.putText(self.frame, f'Lids: {self.data[Com.Lids]}',         (440, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20, 120, 255), 2, cv2.LINE_AA)
        cv2.putText(self.frame, f'Eyes Hor: {self.data[Com.EyesHor]}' , (440, 430), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20, 120, 255), 2, cv2.LINE_AA)
        cv2.putText(self.frame, f'Eyes Ver: {self.data[Com.EyesVer]}' , (440, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (20, 120, 255), 2, cv2.LINE_AA)
