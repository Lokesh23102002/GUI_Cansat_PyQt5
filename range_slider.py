import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

class Graph():
    def __init__(self,main_widget,parent):
        layout = QVBoxLayout(main_widget)

        self.min_slider = QSlider(Qt.Horizontal)
        self.min_slider.setRange(0, 100)
        self.min_slider.setPageStep(10)
        self.min_slider.setTickInterval(10)
        self.min_slider.setTickPosition(QSlider.TicksBelow)
        self.min_slider.valueChanged.connect(self.update_x_range)
        layout.addWidget(self.min_slider)

        self.max_slider = QSlider(Qt.Horizontal)
        self.max_slider.setRange(0, 100)
        self.max_slider.setPageStep(10)
        self.max_slider.setTickInterval(10)
        self.max_slider.setTickPosition(QSlider.TicksBelow)
        self.max_slider.valueChanged.connect(self.update_x_range)
        layout.addWidget(self.max_slider)

        self.label = QLabel('Selected Range: 0 - 0', parent)
        layout.addWidget(self.label)

        self.figure, self.ax = Figure([4,9]), None
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.x_data = np.linspace(0, 100, 1000)
        self.y_data = np.sin(self.x_data)
        self.ax = self.figure.add_subplot(1,1,1)
        self.line, = self.ax.plot(self.x_data, self.y_data)

        self.animation = FuncAnimation(self.figure, self.update_plot, interval=100)

    def update_x_range(self):
        min_value = self.min_slider.value()
        max_value = self.max_slider.value()

        if min_value >= max_value:
            # Ensure minimum is less than maximum
            min_value = max_value - 1
            self.min_slider.setValue(min_value)

        self.label.setText(f'Selected Range: {min_value} - {max_value}')
        self.ax.set_xlim(min_value, max_value)

    def update_plot(self, frame):
        # Example animation: sine wave
        self.x_data = np.linspace(0, 100, 1000)
        self.y_data = np.sin(self.x_data + frame / 10.0)
        self.line.set_xdata(self.x_data)
        self.line.set_ydata(self.y_data)
        self.canvas.draw()

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