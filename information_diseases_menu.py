# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information_diseases.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Information_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")


        self.astigmatism_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.astigmatism_info_btn.sizePolicy().hasHeightForWidth())
        self.astigmatism_info_btn.setSizePolicy(sizePolicy)
        self.astigmatism_info_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.astigmatism_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.astigmatism_info_btn.clicked.connect(self.astigmatism_information)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.astigmatism_info_btn.setFont(font)
        self.astigmatism_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.astigmatism_info_btn.setObjectName("astigmatism_info_btn")
        self.gridLayout_2.addWidget(self.astigmatism_info_btn, 0, 0, 1, 1)


        self.color_blnd_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_blnd_info_btn.sizePolicy().hasHeightForWidth())
        self.color_blnd_info_btn.setSizePolicy(sizePolicy)
        self.color_blnd_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.color_blnd_info_btn.clicked.connect(self.color_blnd_information)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.color_blnd_info_btn.setFont(font)
        self.color_blnd_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.color_blnd_info_btn.setObjectName("color_blnd_info_btn")
        self.gridLayout_2.addWidget(self.color_blnd_info_btn, 1, 0, 1, 1)


        self.macular_deg_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macular_deg_info_btn.sizePolicy().hasHeightForWidth())
        self.macular_deg_info_btn.setSizePolicy(sizePolicy)
        self.macular_deg_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.macular_deg_info_btn.clicked.connect(self.macular_degeneration_information)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.macular_deg_info_btn.setFont(font)
        self.macular_deg_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.macular_deg_info_btn.setObjectName("macular_deg_info_btn")
        self.gridLayout_2.addWidget(self.macular_deg_info_btn, 2, 0, 1, 1)


        self.dry_eye_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dry_eye_info_btn.sizePolicy().hasHeightForWidth())
        self.dry_eye_info_btn.setSizePolicy(sizePolicy)
        self.dry_eye_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.dry_eye_info_btn.clicked.connect(self.dry_eye_information)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dry_eye_info_btn.setFont(font)
        self.dry_eye_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dry_eye_info_btn.setObjectName("dry_eye_info_btn")
        self.gridLayout_2.addWidget(self.dry_eye_info_btn, 3, 0, 1, 1)


        self.accomodation_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.accomodation_info_btn.sizePolicy().hasHeightForWidth())
        self.accomodation_info_btn.setSizePolicy(sizePolicy)
        self.accomodation_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.accomodation_info_btn.clicked.connect(self.eye_accomodation_information)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accomodation_info_btn.setFont(font)
        self.accomodation_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accomodation_info_btn.setObjectName("accomodation_info_btn")
        self.gridLayout_2.addWidget(self.accomodation_info_btn, 4, 0, 1, 1)


        self.return_info_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.return_info_btn.sizePolicy().hasHeightForWidth())
        self.return_info_btn.setSizePolicy(sizePolicy)
        self.return_info_btn.setMaximumSize(QtCore.QSize(350, 50))
        self.return_info_btn.clicked.connect(self.return_fun)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.return_info_btn.setFont(font)
        self.return_info_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_info_btn.setObjectName("return_info_btn")
        self.gridLayout_2.addWidget(self.return_info_btn, 5, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Information about diseases"))
        self.astigmatism_info_btn.setText(_translate("MainWindow", "Astigmatism"))
        self.color_blnd_info_btn.setText(_translate("MainWindow", "Color Blindness"))
        self.macular_deg_info_btn.setText(_translate("MainWindow", "Macular Degeneration"))
        self.dry_eye_info_btn.setText(_translate("MainWindow", "Dry Eye"))
        self.accomodation_info_btn.setText(_translate("MainWindow", "Eye Accommodation"))
        self.return_info_btn.setText(_translate("MainWindow", "Return"))

       

         
