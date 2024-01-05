import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt,QObject,pyqtSlot,QUrl
import range_slider
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import datetime
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

# Reference of below time axis code:
# https://gist.github.com/iverasp/9349dffa42aeffb32e48a0868edfa32d
class TimeAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setLabel(text='Time', units=None)
        self.enableAutoSIPrefix(False)

    def tickStrings(self, values, scale, spacing):
        return [datetime.datetime.fromtimestamp(value).strftime("%I:%M:%S.%f")[:-4] for value in values]



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
    <div id="map" style="height: 100vh;"></div>

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="qrc:///qtwebchannel/qwebchannel.js"></script> <!-- Include QtWebChannel.js -->

    <script>
        var updateMarker;
        var marker;
        var trace = [];
        var traceLayer;
        var map;
        document.addEventListener('DOMContentLoaded', function () {
            map = L.map('map').setView([0, 0], 2);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            marker = L.marker([0, 0]).addTo(map);
        });

        updateMarker = function (lat, lon) {
            // Update the marker position
            marker.setLatLng([lat, lon]);

            // Add the updated position to the trace
            trace.push([lat, lon]);

            // Remove the existing trace layer and add a new one
            if (traceLayer) {
                map.removeLayer(traceLayer);
            }

            traceLayer = L.polyline(trace, {
                color: 'blue'
            });

            // Add the new trace layer to the map
            traceLayer.addTo(map);

            // Update the map view to fit the updated marker and trace
            var bounds = L.latLngBounds(trace);
            map.fitBounds(bounds);
        }
    </script>
</body>

</html>

'''

class qtmap():
    def __init__(self,main_widget):
        layout = QVBoxLayout(main_widget)
        self.webEngineView = QWebEngineView()
        self.webEngineView.settings().setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        # local_html_url = QUrl.fromLocalFile("/asset/openstreetmap.html") 
        # self.webEngineView.setUrl(local_html_url)
        self.webEngineView.setHtml(HTML)
        layout.addWidget(self.webEngineView)
        self.lat = 28.04376082583056
        self.long = 73.28773858890536


    def update_location(self,lat,long):
        self.webEngineView.page().runJavaScript("updateMarker({},{});".format(self.lat,self.long))
        self.lat = self.lat+0.01
        self.long = self.long+0.01
        
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AnimatedGraph()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    sys.exit(app.exec_())

