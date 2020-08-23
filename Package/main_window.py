# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hyperlink.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(856, 522)
        self.window_obj = MainWindow
        MainWindow.setMinimumSize(QtCore.QSize(856, 522))
        MainWindow.setStyleSheet("#centralwidget{\n"
"border-image: url(:/image/web_hyperlink.jpg);\n"
"/*border-position: center;\n"
"border-repeat: no-repeat;\n"
"border-origin: padding;*/\n"
"border: 10px solid white;\n"
"border-width: 50px;\n"
"}\n"
"\n"
"QPushButton { background-color: rgba(0,0,0,150); \n"
"border: 4px solid white;\n"
"padding: 10px 10px;\n"
"font: 13pt \"Rage Italic\";\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
" background-color: rgba(0,0,0,150); \n"
"border: 6px solid blue;\n"
"padding: 5px 5px;\n"
"font: 20pt \"Rage Italic\";\n"
"}\n"
"QPushButton:!pressed:hover\n"
"{\n"
" background-color: rgba(255, 228, 75, 150);\n"
"border: 6px solid blue;\n"
"padding: 5px 5px;\n"
"font: 20pt \"Rage Italic\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setObjectName("button_close")
        self.gridLayout.addWidget(self.button_close, 2, 5, 1, 1)
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setObjectName("button_add")
        self.gridLayout.addWidget(self.button_add, 2, 6, 1, 1)
        self.links_list = QtWidgets.QListWidget(self.centralwidget)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 131, 255, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 131, 255, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 0.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(0, 0, 0, 129))
        gradient.setColorAt(0.05, QtGui.QColor(14, 8, 73))
        gradient.setColorAt(0.36, QtGui.QColor(28, 17, 145, 164))
        gradient.setColorAt(0.6, QtGui.QColor(126, 14, 81))
        gradient.setColorAt(0.75, QtGui.QColor(234, 11, 11, 178))
        gradient.setColorAt(0.79, QtGui.QColor(244, 70, 5, 173))
        gradient.setColorAt(0.86, QtGui.QColor(255, 136, 0, 182))
        gradient.setColorAt(0.935, QtGui.QColor(239, 236, 55, 124))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 131, 255, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.links_list.setPalette(palette)
        self.links_list.setAutoFillBackground(False)
        self.links_list.setStyleSheet("border: 2px solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 129), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 164), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 178), stop:0.79 rgba(244, 70, 5, 173), stop:0.86 rgba(255, 136, 0, 182), stop:0.935 rgba(239, 236, 55, 124));\n"
"alternate-background-color: rgba(29, 131, 255,100);\n"
"font: 8pt \"MS Reference Sans Serif\";")
        self.links_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.links_list.setLineWidth(2)
        self.links_list.setMidLineWidth(3)
        self.links_list.setAutoScrollMargin(100)
        self.links_list.setAlternatingRowColors(True)
        self.links_list.setUniformItemSizes(True)
        self.links_list.setObjectName("links_list")
        self.gridLayout.addWidget(self.links_list, 1, 0, 1, 7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_close.setText(_translate("MainWindow", "CLOSE"))
        self.button_add.setText(_translate("MainWindow", "ADD"))
from . import app_background
