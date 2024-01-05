# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NEXTJS.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from AnimatedGraph import QtGraph,qtmap
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
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.toolBox = QtWidgets.QToolBox(self.tab)
        self.toolBox.setObjectName("toolBox")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.page_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.frame_9 = QtWidgets.QFrame(self.page_3)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_8.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(self.page_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8.addWidget(self.frame_8)
        self.toolBox.addItem(self.page_3, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.page_5.setObjectName("page_5")
        self.toolBox.addItem(self.page_5, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 683, 314))
        self.page_4.setObjectName("page_4")
        self.toolBox.addItem(self.page_4, "")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.horizontalLayout_7.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
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
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NEXTJS)
        
        

   
            

    def retranslateUi(self, NEXTJS):
        _translate = QtCore.QCoreApplication.translate
        NEXTJS.setWindowTitle(_translate("NEXTJS", "NEXTJS"))
        self.Xbee_controll.setTitle(_translate("NEXTJS", "Xbee controller and opened file"))
        self.label.setText(_translate("NEXTJS", "PORT :- "))
        for i,port in enumerate(self.detect_serial_ports()):
            self.comboBox.addItem(port)
        self.label_2.setText(_translate("NEXTJS", "BAUD RATE :- "))
        self.pushButton.setText(_translate("NEXTJS", "Connect"))
        self.pushButton_2.setText(_translate("NEXTJS", "Pause"))
        self.label_3.setText(_translate("NEXTJS", "Data1.csv"))
        self.pushButton_3.setText(_translate("NEXTJS", "Save"))
        self.pushButton_4.setText(_translate("NEXTJS", "Close"))
        self.Graphs.setTitle(_translate("NEXTJS", "GroupBox"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("NEXTJS", "All acceleration"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("NEXTJS", "Acceleration X"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("NEXTJS", "Acceleration Y"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("NEXTJS", "Acceleration Z"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("NEXTJS", "Acceleration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("NEXTJS", "Altitude"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("NEXTJS", "Gyroscope"))
        self.menuFile.setTitle(_translate("NEXTJS", "File"))
        self.menuAbout.setTitle(_translate("NEXTJS", "About"))
        self.actionAbout.setText(_translate("NEXTJS", "Open"))
        self.actionCREATE.setText(_translate("NEXTJS", "CREATE"))


        # custom code not generate by the qt designer
        self.graph = QtGraph(self.tab_2)
        self.graph2 = QtGraph(self.page_5)
        self.graph3 = QtGraph(self.page_4)
        self.graph4 = QtGraph(self.frame_7)
        self.graph5 = QtGraph(self.frame_8)
        self.graph6 = QtGraph(self.frame_9)
        self.pushButton_2.setEnabled(False)
        self.map = qtmap(self.tab_3)
        self.reader = LiveDataReader('DATA.csv',"Test",9600)
        self.reader.data_updated.connect(self.printdata)
        self.actionAbout.triggered.connect(self.file_open)
        self.pushButton.clicked.connect(self.connect)
        self.pushButton_2.clicked.connect(self.disconnect)
    
    # It starts the data recieving
    def connect(self):
        ## connect to the xbee
        # port = self.comboBox.currentText()
        # baud_rate = self.spinBox.value()
        # self.reader.connect(port,baud_rate)
        # self.reader.start()
        self.reader.start()
        self.pushButton.setEnabled(False)
        self.pushButton.setText("Connected")
        self.pushButton_2.setEnabled(True)

    # It stops the data recieving
    def disconnect(self):
        self.reader.terminate()
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

    
    # update the data to the GUI
    def printdata(self,text):
        self.graph.x_data.append(float(text[0]))
        self.graph.y_data.append(float(text[-5]))
        self.graph4.x_data.append(float(text[0]))
        self.graph4.y_data.append(float(text[-11]))
        self.graph5.x_data.append(float(text[0]))
        self.graph5.y_data.append(float(text[-9]))
        self.graph6.x_data.append(float(text[0]))
        self.graph6.y_data.append(float(text[-10]))
        self.map.update_location(text[-3],text[-4])
    
        

    # It detects the available serial ports
    def detect_serial_ports(self):
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        return port_list+['Test']

    def withoutth(self):
        while True:
            print("hello")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NEXTJS = QtWidgets.QMainWindow()
    ui = Ui_NEXTJS()
    ui.setupUi(NEXTJS)
    NEXTJS.show()
    sys.exit(app.exec_())





