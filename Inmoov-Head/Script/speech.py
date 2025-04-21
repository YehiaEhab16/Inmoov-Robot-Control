##########################################################################################
####################### Project: Inmoov Head Control               #######################
####################### Version: 1.7                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 11/01/2025                          #######################
##########################################################################################

# Text to speech module

# Importing PySide modules
from PySide6.QtCore import QThread, Signal

# Importing required modules
import pyttsx3

# Text to speech class
class Speech(QThread):
    OperationComplete = Signal(bool)

    # Initialize variables
    def __init__(self):
        # Initialize thread
        super().__init__()
        # Initialize variables
        self.threadActive = False
        self.text = None

    # Speak function
    def speak(self, text: str, rate: int = 120, voice: bool = False):
        # Set text and start thread
        self.text = text
        self.rate = rate
        self.voice = voice
        if not self.threadActive:
            self.start()        

    # Main thread function
    def run(self):
        self.threadActive = True
        # Convert text to speech and emit signal upon completion
        if self.text is not None:
            try:
                # Initialize Audio Engine
                engine = pyttsx3.init()
                # Set audio properites
                engine.setProperty('voice', engine.getProperty('voices')[self.voice].id)
                engine.setProperty('rate', self.rate)
                # Output voice
                engine.say(self.text) 
                engine.runAndWait()
                # Emit signal upon completion
                self.text = None
                self.OperationComplete.emit(True)
            # Error in audio engine    
            except:
                self.text = None
                self.OperationComplete.emit(False)
        # End thread
        self.threadActive = False

    # Terminate Function
    def terminate(self):
        self.threadActive = False
        super().terminate()
