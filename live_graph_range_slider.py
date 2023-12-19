import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QSizePolicy
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class RangeSlider(QSlider):
    def __init__(self):
        super(RangeSlider, self).__init__(Qt.Horizontal)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.start = 0
        self.end = 100

    def setValues(self, start, end):
        self.start = start
        self.end = end
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        tick_space = 20
        available_width = self.width() - 2 * tick_space
        rect = self.contentsRect()

        # Draw groove
        groove = QRect(rect.x() + tick_space, rect.y() + rect.height() // 2 - 2, available_width, 4)
        painter.fillRect(groove, self.palette().color(QPalette.Shadow))

        # Draw selected range
        selected_range = QRect(rect.x() + tick_space + (self.start / 100) * available_width,
                               rect.y() + rect.height() // 2 - 2,
                               ((self.end - self.start) / 100) * available_width, 4)
        painter.fillRect(selected_range, self.palette().color(QPalette.Highlight))

        # Draw handles
        for value in (self.start, self.end):
            handle = QRect(rect.x() + tick_space + (value / 100) * available_width - 5,
                           rect.y(), 10, rect.height())
            painter.drawEllipse(handle.topLeft(), handle.width(), handle.height())

    def mousePressEvent(self, event):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        rect = self.contentsRect()

        # Calculate handle positions
        handle_start = rect.x() + (self.start / 100) * rect.width()
        handle_end = rect.x() + (self.end / 100) * rect.width()

        if event.button() == Qt.LeftButton:
            if event.x() <= handle_start or handle_end <= event.x():
                self.start = int((event.x() - rect.x()) / rect.width() * 100)
                self.end = self.start
            else:
                self.offset = event.x() - handle_start

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            rect = self.contentsRect()
            new_value = int((event.x() - self.offset - rect.x()) / rect.width() * 100)

            if 0 <= new_value <= 100:
                if event.x() <= rect.x():
                    self.start = 0
                    self.end = new_value
                elif event.x() >= rect.x() + rect.width():
                    self.start = new_value
                    self.end = 100
                else:
                    self.start = min(new_value, 100 - self.end)
                    self.end = max(new_value, 100 - self.start)

            self.update()
            self.valueChanged.emit(self.start, self.end)

class LiveGraphWidget(QMainWindow):
    def __init__(self):
        super(LiveGraphWidget, self).__init__()

        self.setWindowTitle('Live Graph with PyQt5, Matplotlib, and Range Slider')

        # Create the main widget and set it as the central widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create a vertical layout for the main widget
        layout = QVBoxLayout(main_widget)

        # Create a Matplotlib figure and canvas
        self.figure, self.ax = Figure(), None
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Create a navigation toolbar
        self.nav_toolbar = NavigationToolbar(self.canvas, self)
        layout.addWidget(self.nav_toolbar)

        # Create a range slider for controlling the x-axis range
        self.range_slider = RangeSlider()
        self.range_slider.setValues(0, 50)
        self.range_slider.valueChanged.connect(self.update_x_range)
        layout.addWidget(self.range_slider)

        # Initialize data
        self.x_data = np.linspace(0, 100, 100)
        self.y_data = np.sin(self.x_data)

        # Plot initial data
        self.plot_data()

    def update_x_range(self, start, end):
        self.ax.set_xlim(start, end)
        self.canvas.draw
