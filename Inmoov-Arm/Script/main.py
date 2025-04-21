##########################################################################################
####################### Project: Inmoov Arm Control                #######################
####################### Version: 1.5                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 03/12/2024                          #######################
##########################################################################################

# GUI Main #

# Importing PySide packages
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QButtonGroup, QAbstractButton
from PySide6.QtGui import QPixmap ,QImage, QIcon, QCloseEvent
from PySide6.QtCore import QTimer, QPropertyAnimation

# Importing required modules
from syscom import Communication
from sysports import PortHandler
from path import PathManager
from camera import Camera
from gui import InmoovUI
import numpy as np
import sys

# Define main window
class InmoovArm(QWidget):
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
        
        # Create Animation
        self.animation = QPropertyAnimation(self.ui.cameraUrlFrame, b'maximumHeight')
        self.animation.setDuration(500)

        # Serial data to be sent
        self.data = Communication.StopCommunication 
        self.showWarningMessage = False

        # Camera Thread
        self.cameraThread = Camera()
        self.cameraThread.ImageUpdate.connect(self.Handle_UpdateCam)
        if self.cameraThread.start():
            self.ui.toggleCameraButton.setIcon(QIcon(PathManager.CameraOffPngPath))
            self.ui.cameraUrlFrame.setMaximumHeight(0)
            self.showCameraFeed = True
        else:
            self.showCameraFeed = False
            self.ui.toggleCameraButton.setIcon(QIcon(PathManager.CameraOnPngPath))

        # Timer for sending data to arduino
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.Handle_Hold)
        
        # Port Handler
        self.portThread = PortHandler()
        self.portThread.ConnectedPort.connect(self.Handle_Port)

        # Communication Thread (Automatic Mode)
        self.serialThread = Communication(self.cameraThread)

        # Handle GUI Buttons
        self.Handle_Buttons()

    # GUI buttons
    def Handle_Buttons(self):
        self.ui.rotateRightButton.clicked.connect(lambda: self.Handle_Rotate(Camera.RotateRight))  # Rotate Right Button            
        self.ui.rotateLeftButton.clicked.connect(lambda: self.Handle_Rotate(Camera.RotateLeft))    # Rotate Left Button                     
        self.ui.mirrorButton.clicked.connect(lambda: self.Handle_Rotate(Camera.Mirror))            # Mirror Button                     
        self.ui.startComButton.clicked.connect(self.Handle_Start)                                  # Start Communication Button
        self.ui.endComButton.clicked.connect(self.Handle_End)                                      # End Communication Button
        self.ui.toggleCameraButton.clicked.connect(self.Handle_Toggle)                             # Toggle Camera 

        # Contract
        self.ui.contractButton.pressed.connect(self.Handle_Contract)
        self.ui.contractButton.released.connect(self.Handle_Stop)
        # Relax
        self.ui.relaxButton.pressed.connect(self.Handle_Relax)
        self.ui.relaxButton.released.connect(self.Handle_Stop)

        # Mode Radio Group
        self.modeRadioGroup = QButtonGroup()
        self.modeRadioGroup.addButton(self.ui.manualRadio)
        self.modeRadioGroup.addButton(self.ui.automaticRadio)
        self.modeRadioGroup.setExclusive(True)
        self.modeRadioGroup.buttonClicked.connect(self.Handle_Mode)

        # Fingers Radio Buttons
        self.fingerRadioGroup = QButtonGroup()
        self.fingerRadioGroup.addButton(self.ui.thumbRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.wristRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.indexRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.middleRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.ringRadio)                                    
        self.fingerRadioGroup.addButton(self.ui.littleRadio)                                    
        self.fingerRadioGroup.setExclusive(True)
        self.fingerRadioGroup.buttonClicked.connect(self.Handle_Radio)   

    # Handle Port Changes
    def Handle_Port(self, port:str):
        if port == PortHandler.NoDeviceFound:
            self.serialThread.stop()
            self.ui.portLineEdit.setText('')
            self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.RedPngPath))
        else:
            self.ui.portLineEdit.setText(port)  # Get connected serial ports

    # Start Communication
    def Handle_Start(self):
        port = self.ui.portLineEdit.text() # Read Com Port
        if port.isdigit():
            # Try to initialize connection
            comStatus = self.serialThread.connect(port)
            if comStatus == Communication.ComInitSuccess:
                # Succeess Initializing serial communication
                self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.GreenPngPath))
            elif comStatus == Communication.ComAlreadyInitialized:
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
        comStatus = self.serialThread.stop()
        if comStatus == Communication.ComStopSuccess:
            # Succeess ending serial communication
            self.ui.feedbackLabel.setPixmap(QPixmap(PathManager.RedPngPath))
        elif comStatus == Communication.ComAlreadyStopped:
            # Already Stopped
            QMessageBox.warning(self, 'Communication Error', 'No serial communication available')
        else:
            # No serial communication available 
            QMessageBox.warning(self, 'Communication Error', "Couldn't end serial communication")            

    # Toggle Camera Visibility
    def Handle_Toggle(self):
        if self.ui.cameraUrlFrame.maximumHeight() == 0:
            self.cameraThread.terminate()
            self.showCameraFeed = False
            self.ui.cameraLabel.setText('Cam 1\n(No Link)')
            startHeight = 0
            endHeight = self.ui.portFrame.height()
            self.ui.toggleCameraButton.setIcon(QIcon(PathManager.CameraOnPngPath))
        else:
            url = self.ui.urlLineEdit.text()
            # Check if URL is a digit and attempt to start the camera
            if url.isdigit() and self.cameraThread.start(int(url)):
                startHeight = self.ui.portFrame.height()
                endHeight = 0
                self.showCameraFeed = True
                self.ui.toggleCameraButton.setIcon(QIcon(PathManager.CameraOffPngPath))
            else:
                # Handle invalid URL or camera access error
                QMessageBox.warning(self, 'Camera Error', 'Error accessing camera\nPlease check camera url and try again')
                return
            
        # Show Animation
        self.animation.setStartValue(startHeight)
        self.animation.setEndValue(endHeight)   
        self.animation.start()

    # Timer function (sending serial data)
    def Handle_Hold(self):
        self.serialThread.sendData(self.data)

    # Stop Timer function
    def Handle_Stop(self):
        self.timer.stop()

    # Rotate Camera
    def Handle_Rotate(self, direction:int):
        self.cameraThread.rotate(direction)

    # Camera Feed Function
    def Handle_UpdateCam(self, pic:np.ndarray):
        if self.showCameraFeed:
            self.ui.cameraLabel.setPixmap(QPixmap.fromImage(QImage(pic.data, pic.shape[1], pic.shape[0], QImage.Format_RGB888).scaled(self.ui.cameraLabel.width(), self.ui.cameraLabel.height())))  # Update Label
        
    # Handle manual and automatic modes
    def Handle_Mode(self, button:QAbstractButton):
        if button == self.ui.manualRadio:
            # Manual Mode
            self.cameraThread.setMode(Camera.ModeManual)
            # Kill Threads
            self.serialThread.terminate()
            # Enable all manual buttons
            self.ui.relaxButton.setEnabled(True)
            self.ui.contractButton.setEnabled(True)
        else:
            # Automatic mode
            self.cameraThread.setMode(Camera.ModeAutomatic)
            # Start Threads
            self.serialThread.start()
            # Disable all manual buttons
            self.ui.relaxButton.setEnabled(False)
            self.ui.contractButton.setEnabled(False)

    # Contract Fingers
    def Handle_Contract(self):
        if self.ui.thumbRadio.isChecked():
            self.data = Communication.ContractThumb
        elif self.ui.indexRadio.isChecked():
            self.data = Communication.ContractIndex
        elif self.ui.middleRadio.isChecked():
            self.data = Communication.ContractMiddle
        elif self.ui.ringRadio.isChecked():
            self.data = Communication.ContractRing
        elif self.ui.littleRadio.isChecked():
            self.data = Communication.ContractLittle
        elif self.ui.wristRadio.isChecked():
            self.data = Communication.ContractWrist
        else:
            self.data = Communication.StopCommunication
        # Start Timer to send
        self.timer.start(Communication.ManualTimeStep)
    
    # Contract Fingers
    def Handle_Relax(self):
        if self.ui.thumbRadio.isChecked():
            self.data = Communication.RelaxThumb
        elif self.ui.indexRadio.isChecked():
            self.data = Communication.RelaxIndex
        elif self.ui.middleRadio.isChecked():
            self.data = Communication.RelaxMiddle
        elif self.ui.ringRadio.isChecked():
            self.data = Communication.RelaxRing
        elif self.ui.littleRadio.isChecked():
            self.data = Communication.RelaxLittle
        elif self.ui.wristRadio.isChecked():
            self.data = Communication.RelaxWrist
        else:
            self.data = Communication.StopCommunication
        # Start Timer to send
        self.timer.start(Communication.ManualTimeStep)

    # Handle Finger Radio Buttons
    def Handle_Radio(self, button:QAbstractButton):
        if button == self.ui.wristRadio:
            self.ui.contractButton.setText('Rotate Right')
            self.ui.relaxButton.setText('Rotate Left')
        else:
            self.ui.contractButton.setText('Contract')
            self.ui.relaxButton.setText('Relax')

    # Overriding close event to dispose camera
    def closeEvent(self, event:QCloseEvent):
        # Kill all threads
        self.cameraThread.terminate()
        self.serialThread.terminate()
        self.portThread.terminate()
        event.accept()

# Executing GUI
if __name__ == '__main__':
    app = QApplication(sys.argv)
    InmoovArm().show()
    app.exec()