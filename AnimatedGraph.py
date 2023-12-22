import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import range_slider
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
class Graph():
    def __init__(self,main_widget):
        layout = QVBoxLayout(main_widget)
        self.slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setLow(15)
        self.slider.setHigh(35)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.sliderMoved.connect(self.update_x_range)
        layout.addWidget(self.slider)

        self.label = QLabel(f'Selected Range: {self.slider._low} - {self.slider._high}')
        layout.addWidget(self.label)

        self.figure, self.ax = Figure([4,9]), None
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.x_data = np.linspace(0, 100, 1000)
        self.y_data = np.sin(self.x_data)
        self.ax = self.figure.add_subplot(1,1,1)
        self.line, = self.ax.plot(self.x_data, self.y_data)
        self.ax.set_xlim(self.slider._low, self.slider._high)
        self.animation = FuncAnimation(self.figure, self.update_plot, frames=np.linspace(0, 10, 100), interval=100, repeat=True)

    def update_x_range(self):
        min_value = self.slider.low()
        max_value = self.slider.high()

        self.label.setText(f'Selected Range: {min_value} - {max_value}')
        self.ax.set_xlim(min_value, max_value)

    def update_plot(self, frame):
        # Example animation: sine wave
        self.x_data = np.linspace(0, 100, 1000)
        self.y_data = np.sin(self.x_data + frame)
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.canvas.draw()

class QtGraph():
    def __init__(self,main_widget):
        layout = QVBoxLayout(main_widget)
        
        ### from here we are using pyqtgraph
        
        self.GraphWidget = pg.PlotWidget()
        layout.addWidget(self.GraphWidget)
        self.GraphWidget.setBackground('w')

        self.x_data = []
        self.y_data = []

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.GraphWidget.plot(self.x_data,self.y_data,pen = pen)
        self.frame = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(255)
        self.slider.setLow(15)
        self.slider.setHigh(35)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.sliderMoved.connect(self.update_x_range)
        layout.addWidget(self.slider)
        
        self.label = QLabel(f'Selected Range: {self.slider._low} - {self.slider._high}')
        layout.addWidget(self.label)

    def update_x_range(self):
        min_value = self.slider.low()
        max_value = self.slider.high()

        self.label.setText(f'Selected Range: {min_value} - {max_value}')

    def update_plot(self):
        # Example animation: sine wave
        self.data_line.setData(self.x_data,self.y_data)

class AnimatedGraph(QMainWindow):
    def __init__(self):
        super(AnimatedGraph, self).__init__()

        self.setWindowTitle('Animated Graph with Range Sliders')

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        self.graph = Graph(main_widget,self)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AnimatedGraph()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    sys.exit(app.exec_())

