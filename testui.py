# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEXTJS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from range_slider import Graph

class Ui_NEXTJS(object):
    def setupUi(self, NEXTJS):
        NEXTJS.setObjectName("NEXTJS")
        NEXTJS.resize(1095, 735)
        NEXTJS.setMouseTracking(True)
        NEXTJS.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(NEXTJS)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(285, 0))
        self.frame.setMaximumSize(QtCore.QSize(285, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Xbee_controll = QtWidgets.QGroupBox(self.frame)
        self.Xbee_controll.setFlat(False)
        self.Xbee_controll.setCheckable(False)
        self.Xbee_controll.setObjectName("Xbee_controll")
        self.comboBox = QtWidgets.QComboBox(self.Xbee_controll)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 91, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.Xbee_controll)
        self.label.setGeometry(QtCore.QRect(10, 30, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Xbee_controll)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.Xbee_controll)
        self.spinBox.setGeometry(QtCore.QRect(150, 70, 91, 31))
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(50000)
        self.spinBox.setProperty("value", 9600)
        self.spinBox.setObjectName("spinBox")
        self.Xbee_connections = QtWidgets.QGroupBox(self.Xbee_controll)
        self.Xbee_connections.setGeometry(QtCore.QRect(20, 120, 221, 91))
        self.Xbee_connections.setObjectName("Xbee_connections")
        self.pushButton_2 = QtWidgets.QPushButton(self.Xbee_connections)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Xbee_connections)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.Xbee_controll)
        self.label_3.setGeometry(QtCore.QRect(20, 280, 221, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.Xbee_controll)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 330, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Xbee_controll)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 330, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lcdNumber = QtWidgets.QLCDNumber(self.Xbee_controll)
        self.lcdNumber.setGeometry(QtCore.QRect(20, 220, 221, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_2.addWidget(self.Xbee_controll)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Graphs = QtWidgets.QGroupBox(self.frame_2)
        self.Graphs.setMinimumSize(QtCore.QSize(741, 80))
        self.Graphs.setMaximumSize(QtCore.QSize(165777, 165777))
        self.Graphs.setObjectName("Graphs")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Graphs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.Graphs)
        self.widget.setMinimumSize(QtCore.QSize(701, 20))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.Graphs)
        self.widget_2.setMinimumSize(QtCore.QSize(701, 20))
        self.widget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_2.addWidget(self.Graphs)
        self.horizontalLayout.addWidget(self.frame_2)
        NEXTJS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NEXTJS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        NEXTJS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NEXTJS)
        self.statusbar.setObjectName("statusbar")
        NEXTJS.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(NEXTJS)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCREATE = QtWidgets.QAction(NEXTJS)
        self.actionCREATE.setEnabled(True)
        icon = QtGui.QIcon.fromTheme("jl")
        self.actionCREATE.setIcon(icon)
        self.actionCREATE.setObjectName("actionCREATE")
        self.menuFile.addAction(self.actionCREATE)
        self.menuFile.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(NEXTJS)
        QtCore.QMetaObject.connectSlotsByName(NEXTJS)

    def retranslateUi(self, NEXTJS):
        _translate = QtCore.QCoreApplication.translate
        NEXTJS.setWindowTitle(_translate("NEXTJS", "NEXTJS"))
        self.Xbee_controll.setTitle(_translate("NEXTJS", "Xbee controller and opened file"))
        self.comboBox.setItemText(0, _translate("NEXTJS", "COM1"))
        self.comboBox.setItemText(1, _translate("NEXTJS", "COM2"))
        self.comboBox.setItemText(2, _translate("NEXTJS", "COM3"))
        self.comboBox.setItemText(3, _translate("NEXTJS", "COM4"))
        self.comboBox.setItemText(4, _translate("NEXTJS", "COM5"))
        self.label.setText(_translate("NEXTJS", "PORT :- "))
        self.label_2.setText(_translate("NEXTJS", "BAUD RATE :- "))
        self.Xbee_connections.setTitle(_translate("NEXTJS", "GroupBox"))
        self.pushButton_2.setText(_translate("NEXTJS", "Pause"))
        self.pushButton.setText(_translate("NEXTJS", "Connect"))
        self.label_3.setText(_translate("NEXTJS", "Data1.csv"))
        self.pushButton_3.setText(_translate("NEXTJS", "Save"))
        self.pushButton_4.setText(_translate("NEXTJS", "Close"))
        self.Graphs.setTitle(_translate("NEXTJS", "GroupBox"))
        self.menuFile.setTitle(_translate("NEXTJS", "File"))
        self.menuAbout.setTitle(_translate("NEXTJS", "About"))
        self.actionAbout.setText(_translate("NEXTJS", "Open"))
        self.actionCREATE.setText(_translate("NEXTJS", "CREATE"))
        self.graph = Graph(self.widget,self.Graphs)
        self.graph = Graph(self.widget_2,self.Graphs)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEXTJS = QtWidgets.QMainWindow()
    ui = Ui_NEXTJS()
    ui.setupUi(NEXTJS)
    NEXTJS.show()
    sys.exit(app.exec_())
