# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percent_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.percentButton())
        self.percent_button.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percent_button.setFont(font)
        self.percent_button.setObjectName("percent_button")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(187, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.c_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("C"))
        self.c_button.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.c_button.setFont(font)
        self.c_button.setObjectName("c_button")
        self.arrow_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.removeChar())
        self.arrow_button.setGeometry(QtCore.QRect(187, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arrow_button.setFont(font)
        self.arrow_button.setObjectName("arrow_button")
        self.divide_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("/"))
        self.divide_button.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divide_button.setFont(font)
        self.divide_button.setObjectName("divide_button")
        self.seven_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("7"))
        self.seven_button.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.seven_button.setFont(font)
        self.seven_button.setObjectName("seven_button")
        self.nine_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("9"))
        self.nine_button.setGeometry(QtCore.QRect(187, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nine_button.setFont(font)
        self.nine_button.setObjectName("nine_button")
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("*"))
        self.multiply_button.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiply_button.setFont(font)
        self.multiply_button.setObjectName("multiply_button")
        self.eight_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("8"))
        self.eight_button.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eight_button.setFont(font)
        self.eight_button.setObjectName("eight_button")
        self.four_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("4"))
        self.four_button.setGeometry(QtCore.QRect(10, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.four_button.setFont(font)
        self.four_button.setObjectName("four_button")
        self.six_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("6"))
        self.six_button.setGeometry(QtCore.QRect(187, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.six_button.setFont(font)
        self.six_button.setObjectName("six_button")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("-"))
        self.minus_button.setGeometry(QtCore.QRect(275, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minus_button.setFont(font)
        self.minus_button.setObjectName("minus_button")
        self.five_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("5"))
        self.five_button.setGeometry(QtCore.QRect(100, 280, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.five_button.setFont(font)
        self.five_button.setObjectName("five_button")
        self.one_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("1"))
        self.one_button.setGeometry(QtCore.QRect(10, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.one_button.setFont(font)
        self.one_button.setObjectName("one_button")
        self.three_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("3"))
        self.three_button.setGeometry(QtCore.QRect(187, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.three_button.setFont(font)
        self.three_button.setObjectName("three_button")
        self.plus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("+"))
        self.plus_button.setGeometry(QtCore.QRect(275, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plus_button.setFont(font)
        self.plus_button.setObjectName("plus_button")
        self.two_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("2"))
        self.two_button.setGeometry(QtCore.QRect(100, 370, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.two_button.setFont(font)
        self.two_button.setObjectName("two_button")
        self.plus_minus_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plusMinusButton())
        self.plus_minus_button.setGeometry(QtCore.QRect(10, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plus_minus_button.setFont(font)
        self.plus_minus_button.setObjectName("plus_minus_button")
        self.decimal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.decimalButton())
        self.decimal_button.setGeometry(QtCore.QRect(187, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.decimal_button.setFont(font)
        self.decimal_button.setObjectName("decimal_button")
        self.equal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.equalButton())
        self.equal_button.setGeometry(QtCore.QRect(275, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")
        self.zero_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.pressButton("0"))
        self.zero_button.setGeometry(QtCore.QRect(100, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zero_button.setFont(font)
        self.zero_button.setObjectName("zero_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def percentButton(self):
        outputScreen = self.outputLabel.text()
        try:
            result = eval(outputScreen) / 100
            self.outputLabel.setText(str(result))
        except:
            self.outputLabel.setText("Error")

    def equalButton(self):
        outputScreen = self.outputLabel.text()
        try:
            result = eval(outputScreen)
            # Format the result to a string with a maximum of 7 digits
            formatted_result = "{:.7g}".format(result)
            self.outputLabel.setText(formatted_result)
        except:
            self.outputLabel.setText("Error")
    def plusMinusButton(self):
        outputScreen = self.outputLabel.text()
        if outputScreen[0] == "-":
            self.outputLabel.setText(outputScreen[1:])
        else:
            self.outputLabel.setText(f'-{outputScreen}')
    def decimalButton(self):
        outputScreen = self.outputLabel.text()
        if "." not in outputScreen:
            self.outputLabel.setText(f'{outputScreen}.')

    def removeChar(self):
        outputScreen = self.outputLabel.text()
        self.outputLabel.setText(outputScreen[:-1])
    def pressButton(self, button):
        if button == "C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{button}')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percent_button.setText(_translate("MainWindow", "%"))
        self.pushButton_2.setText(_translate("MainWindow", "X"))
        self.pushButton_3.setText(_translate("MainWindow", "X"))
        self.pushButton_4.setText(_translate("MainWindow", "X"))
        self.c_button.setText(_translate("MainWindow", "C"))
        self.arrow_button.setText(_translate("MainWindow", "<<"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.seven_button.setText(_translate("MainWindow", "7"))
        self.nine_button.setText(_translate("MainWindow", "9"))
        self.multiply_button.setText(_translate("MainWindow", "X"))
        self.eight_button.setText(_translate("MainWindow", "8"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.six_button.setText(_translate("MainWindow", "6"))
        self.minus_button.setText(_translate("MainWindow", "-"))
        self.five_button.setText(_translate("MainWindow", "5"))
        self.one_button.setText(_translate("MainWindow", "1"))
        self.three_button.setText(_translate("MainWindow", "3"))
        self.plus_button.setText(_translate("MainWindow", "+"))
        self.two_button.setText(_translate("MainWindow", "2"))
        self.plus_minus_button.setText(_translate("MainWindow", "+/-"))
        self.decimal_button.setText(_translate("MainWindow", "."))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.zero_button.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
