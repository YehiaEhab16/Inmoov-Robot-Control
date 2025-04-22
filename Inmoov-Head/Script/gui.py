##########################################################################################
####################### Project: Inmoov Head Control               #######################
####################### Version: 1.7                               #######################
####################### Authors: Yehia Ehab                        #######################
####################### Date : 11/01/2025                          #######################
##########################################################################################


from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout, QSpinBox, QCheckBox
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
import resources

class InmoovUI(object):
    def setupUi(self, Inmoov):
        if not Inmoov.objectName():
            Inmoov.setObjectName(u"Inmoov")
        Inmoov.resize(800, 650)
        Inmoov.setMinimumSize(QSize(800, 650))
        icon = QIcon()
        icon.addFile(u":/Labels/Icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
"QSpinBox {\n"
"selection-background-color: transparent;\n"
"  background-color: rgba(80, 80, 80, 150);\n"
"  color: white;\n"
"  border: 2px solid rgba(150, 150, 150,150); \n"
"  border-radius: 10px;\n"
"  padding: 4 px;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 15px;\n"
"  height: 15px;\n"
"  border-left-width: 1px;\n"
"  border-left-color: rgb(150, 150, 150);\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 8px;\n"
"  background-color: rgb(255, 120, 20);\n"
"  image: url(:Icons/up_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-button {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
""
                        "  width: 15px;\n"
"  height: 15px;\n"
"  border-left-width: 1px;\n"
"  border-left-color: rgb(150, 150, 150);\n"
"  border-left-style: solid;\n"
"  border-bottom-right-radius: 8px;\n"
"  background-color: rgb(255, 120, 20);\n"
"   image: url(:/Icons/down_arrow.png);\n"
"}\n"
"\n"
"QCheckBox  {\n"
"	spacing: 0 px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 35 px;\n"
"    height: 35 px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/Icons/male.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     image: url(:/Icons/female.png);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QCheckBox:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
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
"	background-color: rgba(80, 80, 8"
                        "0, 150);\n"
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
"    image: url(:/Icons/"
                        "checked_hover.png);\n"
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
" 	border: 2px solid rgba(150, 150, 150,150); \n"
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
"}\n"
"\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-"
                        "color:rgb(30, 30, 30);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background: rgb(200, 200, 200);\n"
"    min-height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"   background: rgb(255, 144, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image:  url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image :url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:verti"
                        "cal:on\n"
"{\n"
"\n"
"    border-image: url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(Inmoov)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 10, 15, 10)
        self.topFrame = QFrame(Inmoov)
        self.topFrame.setObjectName(u"topFrame")
        self.topFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.topFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.manualRadio = QRadioButton(self.topFrame)
        self.manualRadio.setObjectName(u"manualRadio")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualRadio.sizePolicy().hasHeightForWidth())
        self.manualRadio.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.manualRadio.setFont(font)
        self.manualRadio.setChecked(True)

        self.horizontalLayout.addWidget(self.manualRadio)

        self.automaticRadio = QRadioButton(self.topFrame)
        self.automaticRadio.setObjectName(u"automaticRadio")
        sizePolicy.setHeightForWidth(self.automaticRadio.sizePolicy().hasHeightForWidth())
        self.automaticRadio.setSizePolicy(sizePolicy)
        self.automaticRadio.setFont(font)

        self.horizontalLayout.addWidget(self.automaticRadio)


        self.verticalLayout.addWidget(self.topFrame, 0, Qt.AlignmentFlag.AlignTop)

        self.middleFrame = QFrame(Inmoov)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy1)
        self.middleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.cameraLayout = QHBoxLayout(self.middleFrame)
        self.cameraLayout.setSpacing(30)
        self.cameraLayout.setObjectName(u"cameraLayout")
        self.cameraLayout.setContentsMargins(20, 0, 20, 0)
        self.firstCameraFrame = QFrame(self.middleFrame)
        self.firstCameraFrame.setObjectName(u"firstCameraFrame")
        self.firstCameraFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.firstCameraFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.firstCameraControlFrame = QFrame(self.firstCameraFrame)
        self.firstCameraControlFrame.setObjectName(u"firstCameraControlFrame")
        self.firstCameraControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.firstCameraControlFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.firstRotateLeftButton = QPushButton(self.firstCameraControlFrame)
        self.firstRotateLeftButton.setObjectName(u"firstRotateLeftButton")
        self.firstRotateLeftButton.setStyleSheet(u"QPushButton{\n"
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
        self.firstRotateLeftButton.setIcon(icon1)
        self.firstRotateLeftButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstRotateLeftButton)

        self.firstMirrorButton = QPushButton(self.firstCameraControlFrame)
        self.firstMirrorButton.setObjectName(u"firstMirrorButton")
        self.firstMirrorButton.setStyleSheet(u"QPushButton{\n"
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
        self.firstMirrorButton.setIcon(icon2)
        self.firstMirrorButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstMirrorButton)

        self.firstRotateRightButton = QPushButton(self.firstCameraControlFrame)
        self.firstRotateRightButton.setObjectName(u"firstRotateRightButton")
        self.firstRotateRightButton.setStyleSheet(u"QPushButton{\n"
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
        self.firstRotateRightButton.setIcon(icon3)
        self.firstRotateRightButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstRotateRightButton)

        self.firstToggleButton = QPushButton(self.firstCameraControlFrame)
        self.firstToggleButton.setObjectName(u"firstToggleButton")
        self.firstToggleButton.setStyleSheet(u"QPushButton{\n"
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
        self.firstToggleButton.setIcon(icon4)
        self.firstToggleButton.setIconSize(QSize(30, 30))
        self.firstToggleButton.setChecked(False)

        self.horizontalLayout_11.addWidget(self.firstToggleButton)


        self.verticalLayout_4.addWidget(self.firstCameraControlFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.firstCameraLabel = QLabel(self.firstCameraFrame)
        self.firstCameraLabel.setObjectName(u"firstCameraLabel")
        sizePolicy1.setHeightForWidth(self.firstCameraLabel.sizePolicy().hasHeightForWidth())
        self.firstCameraLabel.setSizePolicy(sizePolicy1)
        self.firstCameraLabel.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(18)
        self.firstCameraLabel.setFont(font1)
        self.firstCameraLabel.setStyleSheet(u"border-width: 3px;\n"
"border-color: rgb(74,73,120);\n"
"border-radius: 15px;\n"
"color:white;")
        self.firstCameraLabel.setScaledContents(True)
        self.firstCameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.firstCameraLabel)

        self.firstCameraUrlFrame = QFrame(self.firstCameraFrame)
        self.firstCameraUrlFrame.setObjectName(u"firstCameraUrlFrame")
        self.firstCameraUrlFrame.setStyleSheet(u"")
        self.firstCameraUrlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraUrlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.firstCameraUrlFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.changeFirstUrlLabel = QLabel(self.firstCameraUrlFrame)
        self.changeFirstUrlLabel.setObjectName(u"changeFirstUrlLabel")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.changeFirstUrlLabel.setFont(font2)
        self.changeFirstUrlLabel.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.changeFirstUrlLabel)

        self.firstUrlLineEdit = QLineEdit(self.firstCameraUrlFrame)
        self.firstUrlLineEdit.setObjectName(u"firstUrlLineEdit")
        self.firstUrlLineEdit.setMinimumSize(QSize(160, 0))
        self.firstUrlLineEdit.setFont(font2)

        self.horizontalLayout_6.addWidget(self.firstUrlLineEdit)

        self.addButton = QPushButton(self.firstCameraUrlFrame)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setStyleSheet(u"QPushButton{\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/Icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addButton.setIcon(icon5)
        self.addButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_6.addWidget(self.addButton)


        self.verticalLayout_4.addWidget(self.firstCameraUrlFrame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.cameraLayout.addWidget(self.firstCameraFrame)

        self.secondCameraFrame = QFrame(self.middleFrame)
        self.secondCameraFrame.setObjectName(u"secondCameraFrame")
        self.secondCameraFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondCameraFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.secondCameraFrame)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.secondCameraControlFrame = QFrame(self.secondCameraFrame)
        self.secondCameraControlFrame.setObjectName(u"secondCameraControlFrame")
        self.secondCameraControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondCameraControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.secondCameraControlFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.secondRotateLeftButton = QPushButton(self.secondCameraControlFrame)
        self.secondRotateLeftButton.setObjectName(u"secondRotateLeftButton")
        self.secondRotateLeftButton.setStyleSheet(u"QPushButton{\n"
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
        self.secondRotateLeftButton.setIcon(icon1)
        self.secondRotateLeftButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.secondRotateLeftButton)

        self.secondMirrorButton = QPushButton(self.secondCameraControlFrame)
        self.secondMirrorButton.setObjectName(u"secondMirrorButton")
        self.secondMirrorButton.setStyleSheet(u"QPushButton{\n"
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
        self.secondMirrorButton.setIcon(icon2)
        self.secondMirrorButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.secondMirrorButton)

        self.secondRotateRightButton = QPushButton(self.secondCameraControlFrame)
        self.secondRotateRightButton.setObjectName(u"secondRotateRightButton")
        self.secondRotateRightButton.setStyleSheet(u"QPushButton{\n"
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
        self.secondRotateRightButton.setIcon(icon3)
        self.secondRotateRightButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.secondRotateRightButton)

        self.secondToggleButton = QPushButton(self.secondCameraControlFrame)
        self.secondToggleButton.setObjectName(u"secondToggleButton")
        self.secondToggleButton.setStyleSheet(u"QPushButton{\n"
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
        self.secondToggleButton.setIcon(icon4)
        self.secondToggleButton.setIconSize(QSize(30, 30))
        self.secondToggleButton.setChecked(False)

        self.horizontalLayout_3.addWidget(self.secondToggleButton)


        self.verticalLayout_5.addWidget(self.secondCameraControlFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.secondCameraLabel = QLabel(self.secondCameraFrame)
        self.secondCameraLabel.setObjectName(u"secondCameraLabel")
        sizePolicy1.setHeightForWidth(self.secondCameraLabel.sizePolicy().hasHeightForWidth())
        self.secondCameraLabel.setSizePolicy(sizePolicy1)
        self.secondCameraLabel.setMinimumSize(QSize(0, 0))
        self.secondCameraLabel.setFont(font1)
        self.secondCameraLabel.setStyleSheet(u"border-width: 3px;\n"
"border-color: rgb(74,73,120);\n"
"border-radius: 15px;\n"
"color:white;")
        self.secondCameraLabel.setScaledContents(True)
        self.secondCameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.secondCameraLabel)

        self.secondCameraUrlFrame = QFrame(self.secondCameraFrame)
        self.secondCameraUrlFrame.setObjectName(u"secondCameraUrlFrame")
        self.secondCameraUrlFrame.setStyleSheet(u"")
        self.secondCameraUrlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondCameraUrlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.secondCameraUrlFrame)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.changeSecondUrlLabel = QLabel(self.secondCameraUrlFrame)
        self.changeSecondUrlLabel.setObjectName(u"changeSecondUrlLabel")
        self.changeSecondUrlLabel.setFont(font2)
        self.changeSecondUrlLabel.setStyleSheet(u"color:white;")

        self.horizontalLayout_12.addWidget(self.changeSecondUrlLabel)

        self.secondUrlLineEdit = QLineEdit(self.secondCameraUrlFrame)
        self.secondUrlLineEdit.setObjectName(u"secondUrlLineEdit")
        self.secondUrlLineEdit.setMinimumSize(QSize(160, 0))
        self.secondUrlLineEdit.setFont(font2)

        self.horizontalLayout_12.addWidget(self.secondUrlLineEdit)

        self.removeButton = QPushButton(self.secondCameraUrlFrame)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setStyleSheet(u"QPushButton{\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/Icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.removeButton.setIcon(icon6)
        self.removeButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_12.addWidget(self.removeButton)


        self.verticalLayout_5.addWidget(self.secondCameraUrlFrame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.cameraLayout.addWidget(self.secondCameraFrame)


        self.verticalLayout.addWidget(self.middleFrame)

        self.bottomFrame = QFrame(Inmoov)
        self.bottomFrame.setObjectName(u"bottomFrame")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 0, 15, 0)
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
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.partsFrame = QFrame(self.controlArmFrame)
        self.partsFrame.setObjectName(u"partsFrame")
        self.partsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.partsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.partsFrame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.neckRadio = QRadioButton(self.partsFrame)
        self.neckRadio.setObjectName(u"neckRadio")
        self.neckRadio.setFont(font2)
        self.neckRadio.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.neckRadio)

        self.jawRadio = QRadioButton(self.partsFrame)
        self.jawRadio.setObjectName(u"jawRadio")
        self.jawRadio.setFont(font2)
        self.jawRadio.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.jawRadio)

        self.eyesRadio = QRadioButton(self.partsFrame)
        self.eyesRadio.setObjectName(u"eyesRadio")
        self.eyesRadio.setFont(font2)
        self.eyesRadio.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.eyesRadio)

        self.lidRadio = QRadioButton(self.partsFrame)
        self.lidRadio.setObjectName(u"lidRadio")
        font3 = QFont()
        font3.setPointSize(12)
        self.lidRadio.setFont(font3)

        self.verticalLayout_2.addWidget(self.lidRadio)


        self.horizontalLayout_8.addWidget(self.partsFrame)

        self.controlButtonsFrame = QFrame(self.controlArmFrame)
        self.controlButtonsFrame.setObjectName(u"controlButtonsFrame")
        self.controlButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.controlButtonsFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rightButton = QPushButton(self.controlButtonsFrame)
        self.rightButton.setObjectName(u"rightButton")
        self.rightButton.setMinimumSize(QSize(80, 35))
        self.rightButton.setFont(font2)
        self.rightButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.rightButton)

        self.leftButton = QPushButton(self.controlButtonsFrame)
        self.leftButton.setObjectName(u"leftButton")
        self.leftButton.setMinimumSize(QSize(80, 35))
        self.leftButton.setFont(font2)
        self.leftButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(85, 170, 255, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.leftButton)


        self.horizontalLayout_8.addWidget(self.controlButtonsFrame)

        self.secondaryControlButtonFrame = QFrame(self.controlArmFrame)
        self.secondaryControlButtonFrame.setObjectName(u"secondaryControlButtonFrame")
        self.secondaryControlButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryControlButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.secondaryControlButtonFrame)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.upButton = QPushButton(self.secondaryControlButtonFrame)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setMinimumSize(QSize(80, 35))
        self.upButton.setFont(font2)
        self.upButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(228, 96, 218, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(228, 96, 218, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.upButton)

        self.downButton = QPushButton(self.secondaryControlButtonFrame)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setMinimumSize(QSize(80, 35))
        self.downButton.setFont(font2)
        self.downButton.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(85, 170, 255, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(85, 170, 255, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.downButton)


        self.horizontalLayout_8.addWidget(self.secondaryControlButtonFrame)


        self.horizontalLayout_7.addWidget(self.controlArmFrame, 0, Qt.AlignmentFlag.AlignLeft)

        self.speakFrame = QFrame(self.bottomFrame)
        self.speakFrame.setObjectName(u"speakFrame")
        self.speakFrame.setStyleSheet(u"QFrame #speakFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.speakFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.speakFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.speakFrame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 5)
        self.textToSpeechEdit = QTextEdit(self.speakFrame)
        self.textToSpeechEdit.setObjectName(u"textToSpeechEdit")
        sizePolicy.setHeightForWidth(self.textToSpeechEdit.sizePolicy().hasHeightForWidth())
        self.textToSpeechEdit.setSizePolicy(sizePolicy)
        self.textToSpeechEdit.setMaximumSize(QSize(16777215, 60))
        self.textToSpeechEdit.setFont(font3)
        self.textToSpeechEdit.setStyleSheet(u" QTextEdit {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"    border-radius: 10px;\n"
"    padding:2px;\n"
"    border: 2px solid rgba(150, 150, 150, 150);\n"
"    color: silver;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}")
        self.textToSpeechEdit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        self.textToSpeechEdit.setOverwriteMode(True)

        self.verticalLayout_10.addWidget(self.textToSpeechEdit)

        self.speakControlFrame = QFrame(self.speakFrame)
        self.speakControlFrame.setObjectName(u"speakControlFrame")
        self.speakControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.speakControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.speakControlFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.voiceCheck = QCheckBox(self.speakControlFrame)
        self.voiceCheck.setObjectName(u"voiceCheck")
        sizePolicy.setHeightForWidth(self.voiceCheck.sizePolicy().hasHeightForWidth())
        self.voiceCheck.setSizePolicy(sizePolicy)
        self.voiceCheck.setToolTipDuration(2000)

        self.horizontalLayout_2.addWidget(self.voiceCheck, 0, Qt.AlignmentFlag.AlignLeft)

        self.speakButton = QPushButton(self.speakControlFrame)
        self.speakButton.setObjectName(u"speakButton")
        sizePolicy.setHeightForWidth(self.speakButton.sizePolicy().hasHeightForWidth())
        self.speakButton.setSizePolicy(sizePolicy)
        self.speakButton.setMinimumSize(QSize(90, 35))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.speakButton.setFont(font4)
        self.speakButton.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.speakButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rateSpin = QSpinBox(self.speakControlFrame)
        self.rateSpin.setObjectName(u"rateSpin")
        self.rateSpin.setMaximumSize(QSize(50, 16777215))
        font5 = QFont()
        font5.setPointSize(11)
        self.rateSpin.setFont(font5)
        self.rateSpin.setToolTipDuration(2000)
        self.rateSpin.setStyleSheet(u"")
        self.rateSpin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rateSpin.setKeyboardTracking(False)
        self.rateSpin.setProperty("showGroupSeparator", False)
        self.rateSpin.setMinimum(60)
        self.rateSpin.setMaximum(400)
        self.rateSpin.setSingleStep(20)
        self.rateSpin.setValue(120)

        self.horizontalLayout_2.addWidget(self.rateSpin, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_10.addWidget(self.speakControlFrame)


        self.horizontalLayout_7.addWidget(self.speakFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.communicationFrame = QFrame(self.bottomFrame)
        self.communicationFrame.setObjectName(u"communicationFrame")
        self.communicationFrame.setStyleSheet(u"QFrame #communicationFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.communicationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.communicationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.communicationFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 0)
        self.portFrame = QFrame(self.communicationFrame)
        self.portFrame.setObjectName(u"portFrame")
        self.portFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.portFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.portFrame)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.comLabel = QLabel(self.portFrame)
        self.comLabel.setObjectName(u"comLabel")
        sizePolicy.setHeightForWidth(self.comLabel.sizePolicy().hasHeightForWidth())
        self.comLabel.setSizePolicy(sizePolicy)
        self.comLabel.setFont(font2)
        self.comLabel.setStyleSheet(u"color:white;")
        self.comLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.comLabel)

        self.portLineEdit = QLineEdit(self.portFrame)
        self.portLineEdit.setObjectName(u"portLineEdit")
        sizePolicy.setHeightForWidth(self.portLineEdit.sizePolicy().hasHeightForWidth())
        self.portLineEdit.setSizePolicy(sizePolicy)
        self.portLineEdit.setMaximumSize(QSize(100, 16777215))
        self.portLineEdit.setFont(font2)
        self.portLineEdit.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.portLineEdit)

        self.feedbackLabel = QLabel(self.portFrame)
        self.feedbackLabel.setObjectName(u"feedbackLabel")
        self.feedbackLabel.setMaximumSize(QSize(50, 48))
        self.feedbackLabel.setPixmap(QPixmap(u":/Labels/red.png"))
        self.feedbackLabel.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.feedbackLabel)


        self.verticalLayout_6.addWidget(self.portFrame, 0, Qt.AlignmentFlag.AlignLeft)

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
        sizePolicy.setHeightForWidth(self.startComButton.sizePolicy().hasHeightForWidth())
        self.startComButton.setSizePolicy(sizePolicy)
        self.startComButton.setMinimumSize(QSize(100, 35))
        self.startComButton.setFont(font4)
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
        sizePolicy.setHeightForWidth(self.endComButton.sizePolicy().hasHeightForWidth())
        self.endComButton.setSizePolicy(sizePolicy)
        self.endComButton.setMinimumSize(QSize(100, 35))
        self.endComButton.setFont(font4)
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


        self.verticalLayout.addWidget(self.bottomFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(Inmoov)

        QMetaObject.connectSlotsByName(Inmoov)
    # setupUi

    def retranslateUi(self, Inmoov):
        Inmoov.setWindowTitle(QCoreApplication.translate("Inmoov", u"Inmoov Humanoid", None))
        self.manualRadio.setText(QCoreApplication.translate("Inmoov", u"Manual Mode", None))
        self.automaticRadio.setText(QCoreApplication.translate("Inmoov", u"Automatic Mode", None))
        self.firstRotateLeftButton.setText("")
        self.firstMirrorButton.setText("")
        self.firstRotateRightButton.setText("")
        self.firstToggleButton.setText("")
        self.firstCameraLabel.setText(QCoreApplication.translate("Inmoov", u"Cam 1\n"
"(No Link)", None))
        self.changeFirstUrlLabel.setText(QCoreApplication.translate("Inmoov", u"Camera 1 URL:", None))
        self.firstUrlLineEdit.setText(QCoreApplication.translate("Inmoov", u"0", None))
        self.firstUrlLineEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Change Camera URL", None))
        self.addButton.setText("")
        self.secondRotateLeftButton.setText("")
        self.secondMirrorButton.setText("")
        self.secondRotateRightButton.setText("")
        self.secondToggleButton.setText("")
        self.secondCameraLabel.setText(QCoreApplication.translate("Inmoov", u"Cam 2\n"
"(No Link)", None))
        self.changeSecondUrlLabel.setText(QCoreApplication.translate("Inmoov", u"Camera 2 URL:", None))
        self.secondUrlLineEdit.setText(QCoreApplication.translate("Inmoov", u"1", None))
        self.secondUrlLineEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Change Camera URL", None))
        self.removeButton.setText("")
        self.neckRadio.setText(QCoreApplication.translate("Inmoov", u"Neck", None))
        self.jawRadio.setText(QCoreApplication.translate("Inmoov", u"Jaw", None))
        self.eyesRadio.setText(QCoreApplication.translate("Inmoov", u"Eyes", None))
        self.lidRadio.setText(QCoreApplication.translate("Inmoov", u"Lid", None))
        self.rightButton.setText(QCoreApplication.translate("Inmoov", u"Right", None))
        self.leftButton.setText(QCoreApplication.translate("Inmoov", u"Left", None))
        self.upButton.setText(QCoreApplication.translate("Inmoov", u"Up", None))
        self.downButton.setText(QCoreApplication.translate("Inmoov", u"Down", None))
        self.textToSpeechEdit.setDocumentTitle("")
        self.textToSpeechEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Inmoov will say what you type here", None))
#if QT_CONFIG(tooltip)
        self.voiceCheck.setToolTip(QCoreApplication.translate("Inmoov", u"Speech Voice", None))
#endif // QT_CONFIG(tooltip)
        self.voiceCheck.setText("")
        self.speakButton.setText(QCoreApplication.translate("Inmoov", u"Speak", None))
#if QT_CONFIG(tooltip)
        self.rateSpin.setToolTip(QCoreApplication.translate("Inmoov", u"Speech Rate", None))
#endif // QT_CONFIG(tooltip)
        self.comLabel.setText(QCoreApplication.translate("Inmoov", u"COM:", None))
        self.portLineEdit.setInputMask("")
        self.portLineEdit.setText("")
        self.portLineEdit.setPlaceholderText(QCoreApplication.translate("Inmoov", u"Ex: 9", None))
        self.feedbackLabel.setText("")
        self.startComButton.setText(QCoreApplication.translate("Inmoov", u"Start Comm", None))
        self.endComButton.setText(QCoreApplication.translate("Inmoov", u"End Comm", None))
    # retranslateUi

