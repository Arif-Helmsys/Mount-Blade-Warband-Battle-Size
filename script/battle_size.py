# -*- coding: utf-8 -*-

from getpass import getuser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import platform

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(707, 249)
        Form.setMinimumSize(QtCore.QSize(707, 249))
        Form.setMaximumSize(QtCore.QSize(707, 249))
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\"+getuser()+"\\Desktop\\Coding\\../icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 101, 511, 16))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setSliderPosition(0)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 81, 41))
        self.groupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(234, 120, 255, 31))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(620, 120, 55, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.horizontalSlider.valueChanged.connect(self.updateLCD)
        self.pushButton.clicked.connect(self.wbFile)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Battle Size for M&B"))
        self.pushButton.setText(_translate("Form", "Apply"))
        self.label.setText(_translate("Form", "BATTLE-SIZE"))
        self.groupBox.setTitle(_translate("Form", "CODER"))
        self.label_2.setText(_translate("Form", "HΞLMSУS"))
        self.label_3.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "100"))

    def updateLCD(self,x):
        self.lcdNumber.display(x)
    
    def wbFile(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"Battle size set to {self.horizontalSlider.value()}")
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Succes")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

        file = "C:\\Users\\"+getuser()+"\\Documents\\Mount&Blade Warband\\rgl_config.txt"
        with open(file,"r") as f:
            ff=f.readlines()
        ff[120] = f"battle_size = {self.horizontalSlider.value()}.0000\n"
        with open(file,"w") as g:
            g.writelines(ff)

if __name__ == "__main__":
    import sys
    if platform.system() == "Windows":
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
