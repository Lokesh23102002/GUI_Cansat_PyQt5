# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEXTJS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AnimatedGraph import QtGraph,qtmap,openGLWidget
import serial.tools.list_ports
from PyQt5.QtCore import QThread, pyqtSignal
import time
from reciever import LiveDataReader

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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Xbee_controll = QtWidgets.QGroupBox(self.frame)
        self.Xbee_controll.setMinimumSize(QtCore.QSize(0, 100))
        self.Xbee_controll.setFlat(False)
        self.Xbee_controll.setCheckable(False)
        self.Xbee_controll.setObjectName("Xbee_controll")
        self.gridLayout = QtWidgets.QGridLayout(self.Xbee_controll)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_6 = QtWidgets.QFrame(self.Xbee_controll)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 135))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_6)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_4 = QtWidgets.QFrame(self.frame_6)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setMinimum(100)
        self.spinBox.setMaximum(50000)
        self.spinBox.setProperty("value", 9600)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.Xbee_controll)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Xbee_controll)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.xbeecontrolldatasave = QtWidgets.QFrame(self.Xbee_controll)
        self.xbeecontrolldatasave.setMaximumSize(QtCore.QSize(16777215, 50))
        self.xbeecontrolldatasave.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.xbeecontrolldatasave.setFrameShadow(QtWidgets.QFrame.Raised)
        self.xbeecontrolldatasave.setObjectName("xbeecontrolldatasave")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.xbeecontrolldatasave)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.xbeecontrolldatasave)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.xbeecontrolldatasave)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.gridLayout.addWidget(self.xbeecontrolldatasave, 3, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.Xbee_controll, 0, QtCore.Qt.AlignTop)
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
        self.widget.setMinimumSize(QtCore.QSize(701, 80))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab = QtWidgets.QTabWidget(self.widget)
        self.tab.setEnabled(True)
        self.tab.setObjectName("tab")
        self.Acceleration = QtWidgets.QWidget()
        self.Acceleration.setObjectName("Acceleration")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Acceleration)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.allacc = QtWidgets.QToolBox(self.Acceleration)
        self.allacc.setObjectName("allacc")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.accx = QtWidgets.QFrame(self.page_3)
        self.accx.setStyleSheet("")
        self.accx.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accx.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accx.setObjectName("accx")
        self.horizontalLayout_8.addWidget(self.accx)
        self.accy = QtWidgets.QFrame(self.page_3)
        self.accy.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accy.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accy.setObjectName("accy")
        self.horizontalLayout_8.addWidget(self.accy)
        self.accz = QtWidgets.QFrame(self.page_3)
        self.accz.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accz.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accz.setObjectName("accz")
        self.horizontalLayout_8.addWidget(self.accz)
        self.allacc.addItem(self.page_3, "")
        self.acc_x = QtWidgets.QWidget()
        self.acc_x.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.acc_x.setObjectName("acc_x")
        self.allacc.addItem(self.acc_x, "")
        self.acc_y = QtWidgets.QWidget()
        self.acc_y.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.acc_y.setObjectName("acc_y")
        self.allacc.addItem(self.acc_y, "")
        self.acc_z = QtWidgets.QWidget()
        self.acc_z.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.acc_z.setObjectName("acc_z")
        self.allacc.addItem(self.acc_z, "")
        self.horizontalLayout_7.addWidget(self.allacc)
        self.tab.addTab(self.Acceleration, "")
        self.Attitude = QtWidgets.QWidget()
        self.Attitude.setObjectName("Attitude")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Attitude)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.allatt_2 = QtWidgets.QToolBox(self.Attitude)
        self.allatt_2.setObjectName("allatt_2")
        self.alltt = QtWidgets.QWidget()
        self.alltt.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.alltt.setObjectName("alltt")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.alltt)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.attx = QtWidgets.QFrame(self.alltt)
        self.attx.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.attx.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attx.setObjectName("attx")
        self.horizontalLayout_9.addWidget(self.attx)
        self.atty = QtWidgets.QFrame(self.alltt)
        self.atty.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.atty.setFrameShadow(QtWidgets.QFrame.Raised)
        self.atty.setObjectName("atty")
        self.horizontalLayout_9.addWidget(self.atty)
        self.attz = QtWidgets.QFrame(self.alltt)
        self.attz.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.attz.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attz.setObjectName("attz")
        self.horizontalLayout_9.addWidget(self.attz)
        self.allatt_2.addItem(self.alltt, "")
        self.roll = QtWidgets.QWidget()
        self.roll.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.roll.setObjectName("roll")
        self.allatt_2.addItem(self.roll, "")
        self.yaw = QtWidgets.QWidget()
        self.yaw.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.yaw.setObjectName("yaw")
        self.allatt_2.addItem(self.yaw, "")
        self.pitch = QtWidgets.QWidget()
        self.pitch.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.pitch.setObjectName("pitch")
        self.allatt_2.addItem(self.pitch, "")
        self.horizontalLayout_10.addWidget(self.allatt_2)
        self.tab.addTab(self.Attitude, "")
        self.Altitude = QtWidgets.QWidget()
        self.Altitude.setObjectName("Altitude")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.Altitude)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.toolBox_3 = QtWidgets.QToolBox(self.Altitude)
        self.toolBox_3.setObjectName("toolBox_3")
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.page_9)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.faltitude = QtWidgets.QFrame(self.page_9)
        self.faltitude.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.faltitude.setFrameShadow(QtWidgets.QFrame.Raised)
        self.faltitude.setObjectName("faltitude")
        self.horizontalLayout_11.addWidget(self.faltitude)
        self.ftemp = QtWidgets.QFrame(self.page_9)
        self.ftemp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ftemp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ftemp.setObjectName("ftemp")
        self.horizontalLayout_11.addWidget(self.ftemp)
        self.fpress = QtWidgets.QFrame(self.page_9)
        self.fpress.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fpress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fpress.setObjectName("fpress")
        self.horizontalLayout_11.addWidget(self.fpress)
        self.toolBox_3.addItem(self.page_9, "")
        self.altitude = QtWidgets.QWidget()
        self.altitude.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.altitude.setObjectName("altitude")
        self.toolBox_3.addItem(self.altitude, "")
        self.temp = QtWidgets.QWidget()
        self.temp.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.temp.setObjectName("temp")
        self.toolBox_3.addItem(self.temp, "")
        self.press = QtWidgets.QWidget()
        self.press.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.press.setObjectName("press")
        self.toolBox_3.addItem(self.press, "")
        self.horizontalLayout_12.addWidget(self.toolBox_3)
        self.tab.addTab(self.Altitude, "")
        self.Map = QtWidgets.QWidget()
        self.Map.setObjectName("Map")
        self.tab.addTab(self.Map, "")
        self.Orientation = QtWidgets.QWidget()
        self.Orientation.setObjectName("Orientation")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Orientation)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.openGLWidget = openGLWidget(self.Orientation)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout_2.addWidget(self.openGLWidget, 0, 0, 1, 1)
        self.tab.addTab(self.Orientation, "")
        self.horizontalLayout_2.addWidget(self.tab)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.Graphs)
        self.widget_2.setMinimumSize(QtCore.QSize(701, 80))
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
        self.tab.setCurrentIndex(1)
        self.allacc.setCurrentIndex(0)
        self.allatt_2.setCurrentIndex(0)
        self.toolBox_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NEXTJS)

    def retranslateUi(self, NEXTJS):
        _translate = QtCore.QCoreApplication.translate
        NEXTJS.setWindowTitle(_translate("NEXTJS", "NEXTJS"))
        self.Xbee_controll.setTitle(_translate("NEXTJS", "Xbee controller and opened file"))
        self.label.setText(_translate("NEXTJS", "PORT :- "))
       
        self.label_2.setText(_translate("NEXTJS", "BAUD RATE :- "))
        self.pushButton.setText(_translate("NEXTJS", "Connect"))
        self.pushButton_2.setText(_translate("NEXTJS", "Pause"))
        self.label_3.setText(_translate("NEXTJS", "Data1.csv"))
        self.pushButton_3.setText(_translate("NEXTJS", "Save"))
        self.pushButton_4.setText(_translate("NEXTJS", "Close"))
        self.Graphs.setTitle(_translate("NEXTJS", "Data"))
        self.allacc.setItemText(self.allacc.indexOf(self.page_3), _translate("NEXTJS", "All acceleration"))
        self.allacc.setItemText(self.allacc.indexOf(self.acc_x), _translate("NEXTJS", "Acceleration X"))
        self.allacc.setItemText(self.allacc.indexOf(self.acc_y), _translate("NEXTJS", "Acceleration Y"))
        self.allacc.setItemText(self.allacc.indexOf(self.acc_z), _translate("NEXTJS", "Acceleration Z"))
        self.tab.setTabText(self.tab.indexOf(self.Acceleration), _translate("NEXTJS", "Acceleration"))
        self.allatt_2.setItemText(self.allatt_2.indexOf(self.alltt), _translate("NEXTJS", "All attitude"))
        self.allatt_2.setItemText(self.allatt_2.indexOf(self.roll), _translate("NEXTJS", "Roll"))
        self.allatt_2.setItemText(self.allatt_2.indexOf(self.yaw), _translate("NEXTJS", "Yaw"))
        self.allatt_2.setItemText(self.allatt_2.indexOf(self.pitch), _translate("NEXTJS", "Pitch"))
        self.tab.setTabText(self.tab.indexOf(self.Attitude), _translate("NEXTJS", "Attitude"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.page_9), _translate("NEXTJS", "BMP Data"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.altitude), _translate("NEXTJS", "Altitude"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.temp), _translate("NEXTJS", "Temperature"))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.press), _translate("NEXTJS", "pressure"))
        self.tab.setTabText(self.tab.indexOf(self.Altitude), _translate("NEXTJS", "Altitude"))
        self.tab.setTabText(self.tab.indexOf(self.Map), _translate("NEXTJS", "Map"))
        self.tab.setTabText(self.tab.indexOf(self.Orientation), _translate("NEXTJS", "3D_orientation"))
        self.menuFile.setTitle(_translate("NEXTJS", "File"))
        self.menuAbout.setTitle(_translate("NEXTJS", "About"))
        self.actionAbout.setText(_translate("NEXTJS", "Open"))
        self.actionCREATE.setText(_translate("NEXTJS", "CREATE"))

        #Updating comboBox with available serial ports
        

        for i,port in enumerate(self.detect_serial_ports()):
            self.comboBox.addItem(port)

        # graph
        self.fgaccx = QtGraph(self.accx)
        self.fgaccy = QtGraph(self.accy)
        self.fgaccz = QtGraph(self.accz)
        self.fgalt = QtGraph(self.faltitude)
        self.fgtemp = QtGraph(self.ftemp)
        self.fgpress = QtGraph(self.fpress)
        self.fgattx = QtGraph(self.attx)
        self.fgatty = QtGraph(self.atty)
        self.fgattz = QtGraph(self.attz)
        self.groll = QtGraph(self.roll)
        self.gyaw = QtGraph(self.yaw)
        self.gpitch = QtGraph(self.pitch)
        self.galt = QtGraph(self.altitude)
        self.gtemp = QtGraph(self.temp)
        self.gpress = QtGraph(self.press)       
        self.gaccx = QtGraph(self.acc_x)
        self.gaccy = QtGraph(self.acc_y)
        self.gaccz = QtGraph(self.acc_z)


        #orientation

        
        #map
        self.map = qtmap(self.Map)
        #opening a file where to save data

        self.actionAbout.triggered.connect(self.file_open)
        self.pushButton.clicked.connect(self.connect)
        self.pushButton_2.clicked.connect(self.disconnect)
        # data reader
        self.pushButton_2.setEnabled(False)
        self.reader = LiveDataReader('DATA.csv',"Test",9600)
        self.reader.data_updated.connect(self.printdata)
    


    def connect(self):
        ## connect to the xbee
        # port = self.comboBox.currentText()
        # baud_rate = self.spinBox.value()
        # self.reader.connect(port,baud_rate)
        # self.reader.start()
        if self.comboBox.currentText() == "Test":
            self.reader.data_updated.connect(self.printdata)
            self.reader.start()
            self.pushButton.setEnabled(False)
            self.pushButton.setText("Connected")
            self.pushButton_2.setEnabled(True)
        else:
            port = self.comboBox.currentText()
            baud_rate = self.spinBox.value()
            self.reader.connect(port,baud_rate)
            self.pushButton.setEnabled(False)
            self.pushButton.setText("Connected")
            self.pushButton_2.setEnabled(True)

    # It stops the data recieving
    def disconnect(self):
        if self.reader.device == "Test":
            self.reader.terminate()
            self.pushButton.setEnabled(True)
            self.pushButton.setText("Connect")
            self.pushButton_2.setEnabled(False)
        else:
            self.reader.device.del_data_received_callback(self.reader.recieve)
            self.reader.device.close()
            self.pushButton.setEnabled(True)
            self.pushButton.setText("Connect")
            self.pushButton_2.setEnabled(False)
    
    # It opens the file in which recieved data is saved
    def file_open(self):
        
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, 'Open file', 
         'D:\cansat\Test data\\',"CSV files (*.csv)")
        print(fname)
        if fname[0] != '':
            self.label_3.setText(QtCore.QCoreApplication.translate("NEXTJS", fname[0]))
            self.reader.csv_file = fname[0]
    
    
    def lowpassfilter(self,old,new):
            if len(old) == 0:
                return new
            return old[-1]*0.95+new*0.05
    # It updates the data in the graphs
    def printdata(self,text):
        if self.reader.device != "Test":
            text.append(time.time())
            text.append("end")
            text[0] = text[-2]
        for i in range(len(text)-2):
            text[i] = float(text[i])
        
        self.fgaccx.update_plot(text[0],self.lowpassfilter(self.fgaccx.y_data,text[-11]))
        self.fgaccy.update_plot(text[0],self.lowpassfilter(self.fgaccy.y_data,text[-10]))
        self.fgaccz.update_plot(text[0],self.lowpassfilter(self.fgaccz.y_data,text[-9]))
        # self.fgattx.update_plot(text[0],self.lowpassfilter(self.fgattx.y_data,text[15]))
        self.fgattx.update_plot(text[0],text[15])
        self.fgatty.update_plot(text[0],self.lowpassfilter(self.fgaccy.y_data,text[16]))
        self.fgattz.update_plot(text[0],self.lowpassfilter(self.fgaccz.y_data,text[17]))
        self.fgalt.update_plot(text[0],self.lowpassfilter(self.fgalt.y_data,text[-5]))
        self.fgtemp.update_plot(text[0],self.lowpassfilter(self.fgtemp.y_data,text[-4]))
        self.fgpress.update_plot(text[0],self.lowpassfilter(self.fgpress.y_data,text[-3]))
        self.gaccx.update_plot(text[0],self.lowpassfilter(self.gaccx.y_data,text[-11]))
        self.gaccy.update_plot(text[0],self.lowpassfilter(self.gaccy.y_data,text[-10]))
        self.gaccz.update_plot(text[0],self.lowpassfilter(self.gaccz.y_data,text[-9]))
        self.groll.update_plot(text[0],self.lowpassfilter(self.groll.y_data,text[15]))
        self.gyaw.update_plot(text[0],self.lowpassfilter(self.gyaw.y_data,text[16]))
        self.gpitch.update_plot(text[0],self.lowpassfilter(self.gpitch.y_data,text[17]))
        self.galt.update_plot(text[0],self.lowpassfilter(self.galt.y_data,text[-5]))
        self.gtemp.update_plot(text[0],self.lowpassfilter(self.gtemp.y_data,text[-4]))
        self.gpress.update_plot(text[0],self.lowpassfilter(self.gpress.y_data,text[-3]))
        self.map.update_location(text[0],text[-4])
        self.openGLWidget.x = text[10]
        self.openGLWidget.y = text[11]
        self.openGLWidget.z = -text[9]
        print(text)
    
    # It detects the available serial ports
    def detect_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        return port_list+['Test']


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEXTJS = QtWidgets.QMainWindow()
    ui = Ui_NEXTJS()
    ui.setupUi(NEXTJS)
    NEXTJS.show()
    sys.exit(app.exec_())
