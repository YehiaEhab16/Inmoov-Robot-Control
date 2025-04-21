##########################################################################################
####################### Project: Inmoov Head Control               #######################
####################### Version: 1.7                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 11/01/2025                          #######################
##########################################################################################

# GUI Main #

# Importing PySide packages
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QButtonGroup, QAbstractButton
from PySide6.QtCore import QTimer, QPropertyAnimation, QParallelAnimationGroup
from PySide6.QtGui import QPixmap ,QImage, QIcon, QCloseEvent

# Importing required modules
from syscom import Communication
from sysports import PortHandler
from path import PathManager
from camera import Camera
from speech import Speech
from gui import InmoovUI
import numpy as np
import sys

# Define main window
class InmoovHead(QWidget):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = InmoovUI()
        self.ui.setupUi(self)
        window = self.frameGeometry()
        window.moveCenter(self.screen().availableGeometry().center())
        self.move(window.topLeft())

        # Handle unexpected errors
        sys.excepthook = lambda excType, excValue, _ : QMessageBox.critical(self, "Error", f"An unexpected error occurred:\n{excType.__name__}: {excValue}")

        # Animation Duration
        self.animationDuration = 500
        
        # Create camera 1 url animation
        self.firstCameraUrlAnimation = QPropertyAnimation(self.ui.firstCameraUrlFrame, b'maximumHeight')
        self.firstCameraUrlAnimation.setDuration(self.animationDuration)

        # Create camera 2 url animation
        self.secondCameraUrlAnimation = QPropertyAnimation(self.ui.secondCameraUrlFrame, b'maximumHeight')
        self.secondCameraUrlAnimation.setDuration(self.animationDuration)

        # Create camera 2 animation
        self.secondCameraAnimation = QPropertyAnimation(self.ui.secondCameraFrame, b'maximumWidth')
        self.secondCameraAnimation.setDuration(self.animationDuration)

        # Create camera 2 animation
        self.secondaryControlButtonAnimation = QPropertyAnimation(self.ui.secondaryControlButtonFrame, b'maximumWidth')
        self.secondaryControlButtonAnimation.setDuration(self.animationDuration/2)
        self.ui.secondaryControlButtonFrame.setMaximumWidth(0)

        # Create speech animation
        self.voiceAnimation = QPropertyAnimation(self.ui.voiceCheck, b'maximumWidth')
        self.rateAnimation = QPropertyAnimation(self.ui.rateSpin, b'maximumWidth')
        self.voiceAnimation.setDuration(self.animationDuration)
        self.rateAnimation.setDuration(self.animationDuration)
        self.ui.voiceCheck.setMaximumWidth(0)
        self.ui.rateSpin.setMaximumWidth(0)

        # Create a parallel animation group
        self.speechAnimation = QParallelAnimationGroup()

        # Add both animations to the group
        self.speechAnimation.addAnimation(self.voiceAnimation)
        self.speechAnimation.addAnimation(self.rateAnimation)

        # Serial data to be sent
        self.data = None
        self.showWarningMessage = False

        # First Camera Thread
        self.firstCameraThread = Camera()
        self.firstCameraThread.ImageUpdate.connect(self.Handle_UpdateCam1)
        if self.firstCameraThread.start(0):
            self.ui.firstToggleButton.setIcon(QIcon(PathManager.CameraOffPngPath))
            self.ui.firstCameraUrlFrame.setMaximumHeight(0)
            self.showFirstCameraFeed = True
        else:
            self.ui.firstToggleButton.setIcon(QIcon(PathManager.CameraOnPngPath))
            self.showFirstCameraFeed = False

        # Second Camera Thread
        self.secondCameraThread = Camera()
        self.secondCameraThread.ImageUpdate.connect(self.Handle_UpdateCam2)
        if self.secondCameraThread.start(1):
            self.ui.secondToggleButton.setIcon(QIcon(PathManager.CameraOffPngPath))
            self.ui.secondCameraUrlFrame.setMaximumHeight(0)
            self.showSecondCameraFeed = True
        else:
            self.ui.secondCameraFrame.setMaximumWidth(0)
            self.ui.secondToggleButton.setIcon(QIcon(PathManager.CameraOnPngPath))
            self.showSecondCameraFeed = False
            self.ui.cameraLayout.setContentsMargins(50, 0, 20, 0)

        # Timer for sending data to arduino
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Handle_Hold)
        
        # Port Handler
        self.portThread = PortHandler()
        self.portThread.ConnectedPort.connect(self.Handle_Port)

        self.speechThread = Speech()
        self.speechThread.OperationComplete.connect(self.Handle_Complete)

        # Communication Thread (Automatic Mode)
        self.cameraSerialThread = Communication(self.firstCameraThread, self.secondCameraThread)

        # Communication Thread (Text to speech)
        self.speechSerialThread = Communication()

        # Handle GUI Buttons
        self.Handle_Buttons()        

    # GUI buttons
    def Handle_Buttons(self):
        self.ui.firstRotateRightButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.RotateRight))   # Rotate Right Button            
        self.ui.secondRotateRightButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.RotateRight)) # Rotate Right Button            
        self.ui.firstRotateLeftButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.RotateLeft))     # Rotate Left Button                     
        self.ui.secondRotateLeftButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.RotateLeft))   # Rotate Left Button                     
        self.ui.firstMirrorButton.clicked.connect(lambda: self.Handle_Rotate(Camera.FirstCamera, Camera.Mirror))             # Mirror Button                     
        self.ui.secondMirrorButton.clicked.connect(lambda: self.Handle_Rotate(Camera.SecondCamera, Camera.Mirror))           # Mirror Button                     
        self.ui.firstToggleButton.clicked.connect(lambda: self.Handle_Toggle(Camera.FirstCamera))                            # Toggle Camera 
        self.ui.secondToggleButton.clicked.connect(lambda: self.Handle_Toggle(Camera.SecondCamera))                          # Toggle Camera
        self.ui.textToSpeechEdit.textChanged.connect(self.Handle_Text)                                                       # Text Edit Change 
        self.ui.speakButton.clicked.connect(self.Handle_Speak)                                                               # Speak Button
        self.ui.rateSpin.lineEdit().setReadOnly(True)                                                                        # Rate Spin Box
        self.ui.startComButton.clicked.connect(self.Handle_Start)                                                            # Start Communication Button
        self.ui.endComButton.clicked.connect(self.Handle_End)                                                                # End Communication Button
        self.ui.addButton.clicked.connect(self.Handle_Add)                                                                   # Add Camera Button
        self.ui.removeButton.clicked.connect(self.Handle_Remove)                                                             # Remove Camera Button

        # Right / Up
        self.ui.rightButton.pressed.connect(lambda: self.Handle_Send(True))
        self.ui.upButton.pressed.connect(lambda: self.Handle_Send(True, True))
        self.ui.rightButton.released.connect(self.Handle_Stop)
        self.ui.upButton.released.connect(self.Handle_Stop)
        # Left / Down
        self.ui.leftButton.pressed.connect(self.Handle_Send)
        self.ui.downButton.pressed.connect(lambda: self.Handle_Send(False, True))
        self.ui.leftButton.released.connect(self.Handle_Stop)
        self.ui.downButton.released.connect(self.Handle_Stop)

        # Mode Radio Group
        self.modeRadioGroup = QButtonGroup()
        self.modeRadioGroup.addButton(self.ui.manualRadio)
        self.modeRadioGroup.addButton(self.ui.automaticRadio)
        self.modeRadioGroup.setExclusive(True)
        self.modeRadioGroup.buttonClicked.connect(self.Handle_Mode)

        # Fingers Radio Buttons
        self.fingerRadioGroup = QButtonGroup()
        self.fingerRadioGroup.addButton(self.ui.neckRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.jawRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.eyesRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.lidRadio)                                                                      
        self.fingerRadioGroup.setExclusive(True)
        self.fingerRadioGroup.buttonClicked.connect(self.Handle_Radio)   

    # Camera 1 Feed Function
    def Handle_UpdateCam1(self, pic:np.ndarray):
        if self.showFirstCameraFeed:
            self.ui.firstCameraLabel.setPixmap(QPixmap.fromImage(QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888).scaled(self.ui.firstCameraLabel.width(), self.ui.firstCameraLabel.height())))
    
    # Camera 2 Feed Function
    def Handle_UpdateCam2(self, pic:np.ndarray):
        if self.showSecondCameraFeed:
            self.ui.secondCameraLabel.setPixmap(QPixmap.fromImage(QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888).scaled(self.ui.secondCameraLabel.width(), self.ui.secondCameraLabel.height())))

    # Timer function (sending serial data)
    def Handle_Hold(self):
        self.cameraSerialThread.sendData(self.data)

    # Stop Timer function
    def Handle_Stop(self):
        self.timer.stop()

    # Handle Port Changes
    def Handle_Port(self, port:str):
        if port == PortHandler.NoDeviceFound:
            self.cameraSerialThread.stop()
            self.ui.portLineEdit.setText('')
            self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.RedPngPath))
        else:
            self.ui.portLineEdit.setText(port)  # Get connected serial ports

    # Speak Operation Complete
    def Handle_Complete(self, success: bool):
        if success:
            self.ui.speakButton.setEnabled(True)
        else:
            QMessageBox.warning(self, 'Audio Error', 'Unexpected error occurred in audio engine\nPlease check your audio output and try again')
        self.speechSerialThread.sendData(Communication.EndSpeak)

    # Rotate Camera
    def Handle_Rotate(self, cameraIndex: int, direction: int):
        if cameraIndex == Camera.FirstCamera:
            self.firstCameraThread.rotate(direction)
        else:
            self.secondCameraThread.rotate(direction)

    # Toggle Camera Visibility
    def Handle_Toggle(self, cameraIndex: int):
        if cameraIndex == Camera.FirstCamera:
            if not self.ui.firstCameraUrlFrame.maximumHeight():
                self.showFirstCameraFeed = False
                self.firstCameraThread.terminate()
                self.ui.firstCameraLabel.setText('Cam 1\n(No Link)')
                startHeight = 0
                endHeight = self.ui.portFrame.height()
                self.ui.firstToggleButton.setIcon(QIcon(PathManager.CameraOnPngPath))
            else:
                url = self.ui.firstUrlLineEdit.text()
                # Check if URL is a digit and attempt to start the camera
                if url.isdigit() and self.firstCameraThread.start(int(url)):
                    self.showFirstCameraFeed = True
                    startHeight = self.ui.portFrame.height()
                    endHeight = 0
                    self.ui.firstToggleButton.setIcon(QIcon(PathManager.CameraOffPngPath))
                else:
                    # Handle invalid URL or camera access error
                    QMessageBox.warning(self, 'Camera Error', 'Error accessing camera\nPlease check camera url and try again')
                    return
                
            # Show Animation
            self.firstCameraUrlAnimation.setStartValue(startHeight)
            self.firstCameraUrlAnimation.setEndValue(endHeight)   
            self.firstCameraUrlAnimation.start()
            
        else:
            if not self.ui.secondCameraUrlFrame.maximumHeight():
                self.showSecondCameraFeed = False
                self.ui.cameraLayout.setContentsMargins(50, 0, 20, 0)
                self.secondCameraThread.terminate()
                self.ui.secondCameraLabel.setText('Cam 2\n(No Link)')
                startHeight = 0
                endHeight = self.ui.portFrame.height()
                self.ui.secondToggleButton.setIcon(QIcon(PathManager.CameraOnPngPath))
            else:
                url = self.ui.secondUrlLineEdit.text()
                # Check if URL is a digit and attempt to start the camera
                if url.isdigit() and self.secondCameraThread.start(int(url)):
                    self.showSecondCameraFeed = True
                    self.ui.cameraLayout.setContentsMargins(20, 0, 20, 0)
                    startHeight = self.ui.portFrame.height()
                    endHeight = 0
                    self.ui.secondToggleButton.setIcon(QIcon(PathManager.CameraOffPngPath))
                else:
                    # Handle invalid URL or camera access error
                    QMessageBox.warning(self, 'Camera Error', 'Error accessing camera\nPlease check camera url and try again')
                    return
                
            # Show Animation
            self.secondCameraUrlAnimation.setStartValue(startHeight)
            self.secondCameraUrlAnimation.setEndValue(endHeight)   
            self.secondCameraUrlAnimation.start()

    # Text Edit Change
    def Handle_Text(self):
        text = self.ui.textToSpeechEdit.toPlainText()
        if text and self.ui.voiceCheck.width() == 0:
            self.rateAnimation.setStartValue(0)
            self.rateAnimation.setEndValue(self.ui.feedbackLabel.width())
            self.voiceAnimation.setStartValue(0)
            self.voiceAnimation.setEndValue(self.ui.feedbackLabel.width())
            self.speechAnimation.start()
        elif not text and self.ui.voiceCheck.width() != 0:
            self.rateAnimation.setStartValue(self.ui.feedbackLabel.width())
            self.rateAnimation.setEndValue(0)
            self.voiceAnimation.setStartValue(self.ui.feedbackLabel.width())
            self.voiceAnimation.setEndValue(0)
            self.speechAnimation.start()

    # Speak Function
    def Handle_Speak(self):
        text = self.ui.textToSpeechEdit.toPlainText()
        if text:
            self.ui.speakButton.setEnabled(False)
            self.speechThread.speak(text=text, rate=self.ui.rateSpin.value(), voice=self.ui.voiceCheck.isChecked())
            self.speechSerialThread.sendData(Communication.StartSpeak)
        else:
            QMessageBox.warning(self, 'Text to Speech Error', 'Please enter valid text to be sent to Inmoov')

    # Start Communication
    def Handle_Start(self):
        port = self.ui.portLineEdit.text() # Read Com Port
        if port.isdigit():
            # Try to initialize connection
            comStatus = self.cameraSerialThread.connect(port)
            if comStatus == Communication.InitSuccess:
                # Succeess Initializing serial communication
                self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.GreenPngPath))
            elif comStatus == Communication.AlreadyInitialized:
                # Already initialized
                QMessageBox.warning(self, 'Communication Error', 'Serial communication already initialized')
            else:
                # Error connecting
                QMessageBox.warning(self, 'Communication Error', "Couldn't start serial communication")
        else:
            # Error connecting
            QMessageBox.warning(self, 'Communication Error', 'Please select available com port')

    # End Serial Communication
    def Handle_End(self):
        comStatus = self.cameraSerialThread.stop()
        if comStatus == Communication.StopSuccess:
            # Succeess ending serial communication
            self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.RedPngPath))
        elif comStatus == Communication.AlreadyStopped:
            # Already Stopped
            QMessageBox.warning(self, 'Communication Error', 'No serial communication available')
        else:
            # No serial communication available 
            QMessageBox.warning(self, 'Communication Error', "Couldn't end serial communication")       

    # Add camera button
    def Handle_Add(self):
        if self.ui.secondCameraFrame.width() == 0:
            self.secondCameraAnimation.setStartValue(0)
            self.secondCameraAnimation.setEndValue(self.ui.firstCameraFrame.width())
            self.secondCameraAnimation.start()
        
    # Remove camera button
    def Handle_Remove(self):
        self.secondCameraAnimation.setStartValue(self.ui.firstCameraFrame.width())
        self.secondCameraAnimation.setEndValue(0)
        self.secondCameraAnimation.start()

    # Send checked data
    def Handle_Send(self, primaryDirection: bool = False, secondaryDirection: bool = False):
        if self.ui.neckRadio.isChecked():
            self.data = Communication.NeckRight if primaryDirection else Communication.NeckLeft
        elif self.ui.jawRadio.isChecked():
            self.data = Communication.JawUp if primaryDirection else Communication.JawDown
        elif self.ui.lidRadio.isChecked():
            self.data = Communication.LidOpen if primaryDirection else Communication.LidClose
        elif self.ui.eyesRadio.isChecked():
            if primaryDirection:
                self.data = Communication.EyesUp if secondaryDirection else  Communication.EyesRight
            else:
                self.data = Communication.EyesDown if secondaryDirection else Communication.EyesLeft
        else:
            self.data = Communication.Stop
        # Start Timer to send
        self.timer.start(Communication.ManualTimeStep)

    # Handle manual and automatic modes
    def Handle_Mode(self, button:QAbstractButton):
        if button == self.ui.manualRadio:
            # Manual Mode
            self.firstCameraThread.setMode(Camera.ModeManual)
            self.secondCameraThread.setMode(Camera.ModeManual)
            # Kill Threads
            self.cameraSerialThread.terminate()
            # Enable all manual buttons
            self.ui.upButton.setEnabled(True)
            self.ui.rightButton.setEnabled(True)
            self.ui.downButton.setEnabled(True)
            self.ui.leftButton.setEnabled(True)
        else:
            # Automatic mode
            self.firstCameraThread.setMode(Camera.ModeAutomatic)
            self.secondCameraThread.setMode(Camera.ModeAutomatic)
            # Start Threads
            self.cameraSerialThread.start()
            # Disable all manual buttons
            self.ui.upButton.setEnabled(False)
            self.ui.rightButton.setEnabled(False)
            self.ui.downButton.setEnabled(False)
            self.ui.leftButton.setEnabled(False)

    # Handle Finger Radio Buttons
    def Handle_Radio(self, button:QAbstractButton):
        if button == self.ui.neckRadio:
            self.ui.rightButton.setText('Right')
            self.ui.leftButton.setText('Left')
            if self.ui.secondaryControlButtonFrame.width()!=0:
                self.secondaryControlButtonAnimation.setStartValue(self.ui.controlButtonsFrame.width())
                self.secondaryControlButtonAnimation.setEndValue(0)
                self.secondaryControlButtonAnimation.start()
        elif button == self.ui.jawRadio:
            self.ui.rightButton.setText('Up')
            self.ui.leftButton.setText('Down')
            if self.ui.secondaryControlButtonFrame.width()!=0:
                self.secondaryControlButtonAnimation.setStartValue(self.ui.controlButtonsFrame.width())
                self.secondaryControlButtonAnimation.setEndValue(0)
                self.secondaryControlButtonAnimation.start()
        elif button == self.ui.lidRadio:
            self.ui.rightButton.setText('Open')
            self.ui.leftButton.setText('Close')
            if self.ui.secondaryControlButtonFrame.width()!=0:
                self.secondaryControlButtonAnimation.setStartValue(self.ui.controlButtonsFrame.width())
                self.secondaryControlButtonAnimation.setEndValue(0)
                self.secondaryControlButtonAnimation.start()
        else:
            self.ui.rightButton.setText('Right')
            self.ui.leftButton.setText('Left')
            if self.ui.secondaryControlButtonFrame.width()==0:
                self.secondaryControlButtonAnimation.setStartValue(0)
                self.secondaryControlButtonAnimation.setEndValue(self.ui.controlButtonsFrame.width())
                self.secondaryControlButtonAnimation.start()

    # Overriding close event to dispose camera
    def closeEvent(self, event:QCloseEvent):
        # Kill all threads
        self.cameraSerialThread.terminate()
        self.speechSerialThread.terminate()
        self.firstCameraThread.terminate()
        self.secondCameraThread.terminate()
        self.speechThread.terminate()
        self.portThread.terminate()
        event.accept()

# Executing GUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    InmoovHead().show()
    app.exec()
    