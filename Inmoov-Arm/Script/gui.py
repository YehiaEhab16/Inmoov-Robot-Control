##########################################################################################
####################### Project: Inmoov Arm Control                #######################
####################### Version: 1.5                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 03/12/2024                          #######################
##########################################################################################

from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QSizePolicy, QVBoxLayout
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
import resources

class InmoovUI(object):
    def setupUi(self, Inmoov):
        if not Inmoov.objectName():
            Inmoov.setObjectName(u"Inmoov")
        Inmoov.resize(700, 600)
        Inmoov.setMinimumSize(QSize(700, 600))
        icon = QIcon()
        icon.addFile(u":/Icons/Icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Inmoov.setWindowIcon(icon)
        Inmoov.setStyleSheet(u"QWidget#Inmoov{\n"
"background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"}\n"
"\n"
" QLineEdit {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"    border-radius: 10px;\n"
"    padding:2px;\n"
"    border: 2px solid rgba(150, 150, 150, 150);\n"
"    color: silver;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: rgba(255,255,255,100);\n"
"}\n"
"\n"
""
                        "QRadioButton {\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/Icons/unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/Icons/hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Icons/checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/Icons/checked_hover.png);\n"
"}\n"
"\n"
"QMessageBox {\n"
" background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"  width: 400px; \n"
"  height: 400px;\n"
"}\n"
"QMessageBox QLabel {\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QMessageBox QPushButton {\n"
"   	background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px "
                        "solid rgba(150, 150, 150,150); \n"
"  	font-size: 14px;\n"
"  	min-height: 15px; \n"
"  	min-width: 60px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"  background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"   background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}")
        self.verticalLayout = QVBoxLayout(Inmoov)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.topFrame = QFrame(Inmoov)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 10, 15, 10)
        self.cameraControlFrame = QFrame(self.topFrame)
        self.cameraControlFrame.setObjectName(u"cameraControlFrame")
        self.cameraControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.cameraControlFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rotateLeftButton = QPushButton(self.cameraControlFrame)
        self.rotateLeftButton.setObjectName(u"rotateLeftButton")
        self.rotateLeftButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/rotate_left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rotateLeftButton.setIcon(icon1)
        self.rotateLeftButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.rotateLeftButton)

        self.mirrorButton = QPushButton(self.cameraControlFrame)
        self.mirrorButton.setObjectName(u"mirrorButton")
        self.mirrorButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/mirror.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.mirrorButton.setIcon(icon2)
        self.mirrorButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.mirrorButton)

        self.rotateRightButton = QPushButton(self.cameraControlFrame)
        self.rotateRightButton.setObjectName(u"rotateRightButton")
        self.rotateRightButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/rotate_right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rotateRightButton.setIcon(icon3)
        self.rotateRightButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.rotateRightButton)


        self.horizontalLayout_3.addWidget(self.cameraControlFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.manualRadio = QRadioButton(self.topFrame)
        self.manualRadio.setObjectName(u"manualRadio")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.manualRadio.setFont(font)
        self.manualRadio.setChecked(True)

        self.horizontalLayout_3.addWidget(self.manualRadio, 0, Qt.AlignmentFlag.AlignHCenter)

        self.logoLabel = QLabel(self.topFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMaximumSize(QSize(145, 30))
        self.logoLabel.setPixmap(QPixmap(u":/Labels/logo.png"))
        self.logoLabel.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logoLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.automaticRadio = QRadioButton(self.topFrame)
        self.automaticRadio.setObjectName(u"automaticRadio")
        self.automaticRadio.setFont(font)

        self.horizontalLayout_3.addWidget(self.automaticRadio, 0, Qt.AlignmentFlag.AlignHCenter)

        self.toggleCameraButton = QPushButton(self.topFrame)
        self.toggleCameraButton.setObjectName(u"toggleCameraButton")
        self.toggleCameraButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/camera_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggleCameraButton.setIcon(icon4)
        self.toggleCameraButton.setIconSize(QSize(30, 30))
        self.toggleCameraButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.toggleCameraButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.topFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.middleFrame = QFrame(Inmoov)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy)
        self.middleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.middleFrame)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(50, 0, 50, 0)
        self.cameraFrame = QFrame(self.middleFrame)
        self.cameraFrame.setObjectName(u"cameraFrame")
        sizePolicy.setHeightForWidth(self.cameraFrame.sizePolicy().hasHeightForWidth())
        self.cameraFrame.setSizePolicy(sizePolicy)
        self.cameraFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.cameraFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cameraLabel = QLabel(self.cameraFrame)
        self.cameraLabel.setObjectName(u"cameraLabel")
        self.cameraLabel.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        self.cameraLabel.setFont(font1)
        self.cameraLabel.setStyleSheet(u"border-width: 3px;\n"
"border-color: rgb(74,73,120);\n"
"border-radius: 15px;\n"
"color:white;")
        self.cameraLabel.setScaledContents(True)
        self.cameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.cameraLabel)


        self.verticalLayout_11.addWidget(self.cameraFrame)

        self.cameraUrlFrame = QFrame(self.middleFrame)
        self.cameraUrlFrame.setObjectName(u"cameraUrlFrame")
        self.cameraUrlFrame.setStyleSheet(u"")
        self.cameraUrlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraUrlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.cameraUrlFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.changeUrlLabel = QLabel(self.cameraUrlFrame)
        self.changeUrlLabel.setObjectName(u"changeUrlLabel")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.changeUrlLabel.setFont(font2)
        self.changeUrlLabel.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.changeUrlLabel)

        self.urlLineEdit = QLineEdit(self.cameraUrlFrame)
        self.urlLineEdit.setObjectName(u"urlLineEdit")
        self.urlLineEdit.setMinimumSize(QSize(160, 0))
        self.urlLineEdit.setFont(font2)

        self.horizontalLayout_6.addWidget(self.urlLineEdit)


        self.verticalLayout_11.addWidget(self.cameraUrlFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.middleFrame)

        self.bottomFrame = QFrame(Inmoov)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 5)
        self.controlArmFrame = QFrame(self.bottomFrame)
        self.controlArmFrame.setObjectName(u"controlArmFrame")
        self.controlArmFrame.setStyleSheet(u"QFrame #controlArmFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.controlArmFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlArmFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.controlArmFrame)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 5, 10, 0)
        self.fingersFrame = QFrame(self.controlArmFrame)
        self.fingersFrame.setObjectName(u"fingersFrame")
        self.fingersFrame.setStyleSheet(u"QRadioButton {\n"
"color: rgb(255,120,20);\n"
"}")
        self.horizontalLayout_9 = QHBoxLayout(self.fingersFrame)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.leftFingersFrame = QFrame(self.fingersFrame)
        self.leftFingersFrame.setObjectName(u"leftFingersFrame")
        self.leftFingersFrame.setStyleSheet(u"")
        self.leftFingersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftFingersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.leftFingersFrame)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.thumbRadio = QRadioButton(self.leftFingersFrame)
        self.thumbRadio.setObjectName(u"thumbRadio")
        self.thumbRadio.setFont(font2)
        self.thumbRadio.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.thumbRadio)

        self.indexRadio = QRadioButton(self.leftFingersFrame)
        self.indexRadio.setObjectName(u"indexRadio")
        self.indexRadio.setFont(font2)
        self.indexRadio.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.indexRadio)

        self.middleRadio = QRadioButton(self.leftFingersFrame)
        self.middleRadio.setObjectName(u"middleRadio")
        self.middleRadio.setFont(font2)
        self.middleRadio.setStyleSheet(u"")

        self.verticalLayout_10.addWidget(self.middleRadio)


        self.horizontalLayout_9.addWidget(self.leftFingersFrame)

        self.rightFingersFrame = QFrame(self.fingersFrame)
        self.rightFingersFrame.setObjectName(u"rightFingersFrame")
        self.rightFingersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightFingersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.rightFingersFrame)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ringRadio = QRadioButton(self.rightFingersFrame)
        self.ringRadio.setObjectName(u"ringRadio")
        self.ringRadio.setFont(font2)
        self.ringRadio.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.ringRadio)

        self.littleRadio = QRadioButton(self.rightFingersFrame)
        self.littleRadio.setObjectName(u"littleRadio")
        self.littleRadio.setFont(font2)
        self.littleRadio.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.littleRadio)

        self.wristRadio = QRadioButton(self.rightFingersFrame)
        self.wristRadio.setObjectName(u"wristRadio")
        self.wristRadio.setFont(font2)
        self.wristRadio.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.wristRadio)


        self.horizontalLayout_9.addWidget(self.rightFingersFrame)


        self.horizontalLayout_8.addWidget(self.fingersFrame)

        self.controlButtonsFrame = QFrame(self.controlArmFrame)
        self.controlButtonsFrame.setObjectName(u"controlButtonsFrame")
        self.controlButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.controlButtonsFrame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.contractButton = QPushButton(self.controlButtonsFrame)
        self.contractButton.setObjectName(u"contractButton")
        self.contractButton.setMinimumSize(QSize(120, 35))
        self.contractButton.setFont(font2)
        self.contractButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.contractButton)

        self.relaxButton = QPushButton(self.controlButtonsFrame)
        self.relaxButton.setObjectName(u"relaxButton")
        self.relaxButton.setMinimumSize(QSize(120, 35))
        self.relaxButton.setFont(font2)
        self.relaxButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(85, 170, 255, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.relaxButton)


        self.horizontalLayout_8.addWidget(self.controlButtonsFrame)


        self.horizontalLayout_7.addWidget(self.controlArmFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.communicationFrame = QFrame(self.bottomFrame)
        self.communicationFrame.setObjectName(u"communicationFrame")
        self.communicationFrame.setStyleSheet(u"QFrame #communicationFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.communicationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.communicationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.communicationFrame)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 10)
        self.portFrame = QFrame(self.communicationFrame)
        self.portFrame.setObjectName(u"portFrame")
        self.portFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.portFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.portFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.comLabel = QLabel(self.portFrame)
        self.comLabel.setObjectName(u"comLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comLabel.sizePolicy().hasHeightForWidth())
        self.comLabel.setSizePolicy(sizePolicy1)
        self.comLabel.setFont(font2)
        self.comLabel.setStyleSheet(u"color:white;")
        self.comLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.comLabel)

        self.portLineEdit = QLineEdit(self.portFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        sizePolicy1.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy1)
        self.portLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.portLineEdit.setFont(font2)
        self.portLineEdit.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.portLineEdit)

        self.feedbackLabel = QLabel(self.portFrame)
        self.feedbackLabel.setObjectName(u"feedbackLabel")
        self.feedbackLabel.setMaximumSize(QSize(50, 48))
        self.feedbackLabel.setPixmap(QPixmap(u":/Labels/red.png"))
        self.feedbackLabel.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.feedbackLabel)


        self.verticalLayout_6.addWidget(self.portFrame)

        self.controlComFrame = QFrame(self.communicationFrame)
        self.controlComFrame.setObjectName(u"controlComFrame")
        self.controlComFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlComFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.controlComFrame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.startComButton = QPushButton(self.controlComFrame)
        self.startComButton.setObjectName(u"startComButton")
        sizePolicy1.setHeightForWidth(self.startComButton.sizePolicy().hasHeightForWidth())
        self.startComButton.setSizePolicy(sizePolicy1)
        self.startComButton.setMinimumSize(QSize(120, 35))
        self.startComButton.setFont(font2)
        self.startComButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.startComButton)

        self.endComButton = QPushButton(self.controlComFrame)
        self.endComButton.setObjectName(u"endComButton")
        sizePolicy1.setHeightForWidth(self.endComButton.sizePolicy().hasHeightForWidth())
        self.endComButton.setSizePolicy(sizePolicy1)
        self.endComButton.setMinimumSize(QSize(120, 35))
        self.endComButton.setFont(font2)
        self.endComButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgba(255, 30, 30, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color :rgba(255, 30, 30, 150);    \n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.endComButton)


        self.verticalLayout_6.addWidget(self.controlComFrame)


        self.horizontalLayout_7.addWidget(self.communicationFrame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.bottomFrame)


        self.retranslateUi(Inmoov)

        QMetaObject.connectSlotsByName(Inmoov)
    # setupUi

    def retranslateUi(self, Inmoov):
        Inmoov.setWindowTitle(QCoreApplication.translate("Inmoov", u"Inmoov Humanoid", None))
        self.rotateLeftButton.setText("")
        self.mirrorButton.setText("")
        self.rotateRightButton.setText("")
        self.manualRadio.setText(QCoreApplication.translate("Inmoov", u"Manual Mode", None))
        self.logoLabel.setText("")
        self.automaticRadio.setText(QCoreApplication.translate("Inmoov", u"Automatic Mode", None))
        self.toggleCameraButton.setText("")
        self.cameraLabel.setText(QCoreApplication.translate("Inmoov", u"Cam 1\n"
"(No Link)", None))
        self.changeUrlLabel.setText(QCoreApplication.translate("Inmoov", u"Camera URL:", None))
        self.urlLineEdit.setText(QCoreApplication.translate("Inmoov", u"0", None))
        self.urlLineEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Change Camera URL", None))
        self.thumbRadio.setText(QCoreApplication.translate("Inmoov", u"Thumb", None))
        self.indexRadio.setText(QCoreApplication.translate("Inmoov", u"Index Finger", None))
        self.middleRadio.setText(QCoreApplication.translate("Inmoov", u"Middle Finger", None))
        self.ringRadio.setText(QCoreApplication.translate("Inmoov", u"Ring Finger", None))
        self.littleRadio.setText(QCoreApplication.translate("Inmoov", u"Little Finger", None))
        self.wristRadio.setText(QCoreApplication.translate("Inmoov", u"Wrist", None))
        self.contractButton.setText(QCoreApplication.translate("Inmoov", u"Contract", None))
        self.relaxButton.setText(QCoreApplication.translate("Inmoov", u"Relax", None))
        self.comLabel.setText(QCoreApplication.translate("Inmoov", u"COM:", None))
        self.portLineEdit.setInputMask("")
        self.portLineEdit.setText("")
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Ex: 9", None))
        self.feedbackLabel.setText("")
        self.startComButton.setText(QCoreApplication.translate("Inmoov", u"Start Comm", None))
        self.endComButton.setText(QCoreApplication.translate("Inmoov", u"End Comm", None))
    # retranslateUi

