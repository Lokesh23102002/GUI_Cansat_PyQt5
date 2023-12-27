import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt,QObject,pyqtSlot,QUrl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import range_slider
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import datetime
import folium
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

# Reference of below time axis code:
# https://gist.github.com/iverasp/9349dffa42aeffb32e48a0868edfa32d
class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%I:%M:%S.%f")[:-4] for value in values]

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
        
        self.GraphWidget = pg.PlotWidget(axisItems={'bottom': TimeAxisItem(orientation='bottom')})
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
        
class FoliumMap():
    def __init__(self,main_widget):
        layout = QVBoxLayout(main_widget)
        self.map_view = QWebEngineView()
        layout.addWidget(self.map_view)
        self.latitudes = [28.04376082583056]
        self.longitudes = [73.28773858890536]
        self.display_map()

    def display_map(self,):
        # Create a Folium map
        self.m = folium.Map(location=[28.04376082583056, 73.28773858890536], zoom_start=15,control_scale=True,prefer_canvas=True)
        print(self.m._repr_html_())
        folium.Marker(location=[28.04376082583056, 73.28773858890536], popup='Marker').add_to(self.m)
        # Save the map as HTML
        map_html = self.m._repr_html_()

        # Load the HTML into the QWebEngineView
        self.map_view.setHtml(map_html)
    def update_plot(self):
        self.latitudes.append(self.latitudes[-1]+0.0001)
        self.longitudes.append(self.longitudes[-1]+0.0001)

HTML = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenStreetMap Example</title>
    <!-- Include Leaflet from CDN without integrity attribute -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css">
</head>

<body>
    <div id="map" style="height: 400px;"></div>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="qrc:///qtwebchannel/qwebchannel.js"></script> <!-- Include QtWebChannel.js -->

    <script>
        var updateMarker;
        var marker;

        document.addEventListener('DOMContentLoaded', function () {
            var map = L.map('map').setView([0, 0], 2);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            marker = L.marker([0, 0]).addTo(map);

            ;
        });

        updateMarker = function (lat, lon) {
            marker.setLatLng([lat, lon]).update();

        }
    </script>
</body>

</html>'''

class qtmap():
    def __init__(self,main_widget):
        layout = QVBoxLayout(main_widget)
        self.webEngineView = QWebEngineView()
        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        local_html_url = QUrl.fromLocalFile("/asset/openstreetmap.html") 
        # self.webEngineView.setUrl(local_html_url)
        self.webEngineView.setHtml(HTML)
        layout.addWidget(self.webEngineView)
        self.lat = 28.04376082583056
        self.long = 73.28773858890536


    def update_location(self,lat,long):
        self.webEngineView.page().runJavaScript("updateMarker({},{});".format(self.lat,self.long))
        self.lat = self.lat+0.0001
        self.long = self.long+0.0001
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AnimatedGraph()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    sys.exit(app.exec_())

