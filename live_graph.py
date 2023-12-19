import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class LiveGraphWidget(QMainWindow):
    def __init__(self):
        super(LiveGraphWidget, self).__init__()

        self.setWindowTitle('Live Graph with PyQt5 and Matplotlib')

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

        # Create a slider for scaling the x-axis
        self.slider = QSlider()
        self.slider.setOrientation(1)  # Set orientation to horizontal
        self.slider.setMinimum(1)
        self.slider.setMaximum(10)
        self.slider.setValue(1)
        self.slider.valueChanged.connect(self.update_x_scale)
        layout.addWidget(self.slider)

        # Initialize data
        self.x_data = np.linspace(0, 10, 100)
        self.y_data = np.sin(self.x_data)

        # Plot initial data
        self.plot_data()

    def update_x_scale(self):
        scale_factor = self.slider.value()
        self.ax.set_xlim(0, 10 * scale_factor)
        self.canvas.draw()

    def plot_data(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, label='Live Data')
        self.ax.legend()
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LiveGraphWidget()
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())
