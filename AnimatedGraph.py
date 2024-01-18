import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel,QOpenGLWidget
from PyQt5.QtCore import Qt,QObject,pyqtSlot,QUrl
import range_slider
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import datetime
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView,QWebEngineSettings

from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh

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
        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(50)
        # self.timer.timeout.connect(self.update_plot)
        # self.timer.start()

        self.slider = range_slider.RangeSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setLow(15)
        self.slider.setHigh(100)
        self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider.sliderMoved.connect(self.update_x_range)
        layout.addWidget(self.slider)
        
        self.label = QLabel(f'Selected Range: {self.slider._low} - {self.slider._high}')
        layout.addWidget(self.label)

    def update_x_range(self):
        min_value = self.slider.low()
        max_value = self.slider.high()
        self.label.setText(f'Selected Range: {min_value} - {max_value}')

    def update_plot(self,xd,yd):
        # Example animation: sine wave
        self.x_data.append(xd)
        self.y_data.append(yd)
        self.data_line.setData(self.x_data,self.y_data)
        min_value = self.slider.low()
        max_value = self.slider.high()
        self.GraphWidget.setXRange(self.x_data[int(len(self.x_data)*(min_value/100))],self.x_data[int(len(self.x_data)*(max_value/100))-1],padding=0)


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
            //map.fitBounds(bounds);
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
        
    
class openGLWidget(QOpenGLWidget):
    def __init__(self,parent=None):
        QOpenGLWidget.__init__(self,parent)
        self.x = 0
        self.y = 0
        self.z = 0
        self.start = 3319
        self.stl_path = '3d/assem.stl'
        self.stl_model = mesh.Mesh.from_file(self.stl_path)
        self.flat_vertices = np.array(self.stl_model.vectors).flatten()
        self.center = np.mean(self.stl_model.vectors.reshape((-1, 3)), axis=0)
        self.rotation_angle = 0.5
        gluPerspective(40, 1, 1, 1000)
       
        

    def initializeGL(self):
        
        
        glClearColor(0.0, 0.5, 0.5, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHT1)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        self.vbo =glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.flat_vertices, GL_STATIC_DRAW)
        glBindBuffer(GL_ARRAY_BUFFER, 0)
    
        # Set light position behind the camera

    def paintGL(self,xd=None,yd=None,zd=None):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  
        glTranslatef(0, 0, -400)# Push the current matrix onto the matrix stack

        # Apply rotation around the Y-axis
        
        glRotatef(self.x, 1, 0, 0)
        glRotatef(self.y,0 , 0, 1)
        glRotatef(self.z, 0, 1, 0)
       
        glLightfv(GL_LIGHT0, GL_POSITION, (100, 100, 100, 1))
        glLightfv(GL_LIGHT1, GL_POSITION, (-100, -100, 100, 1))
        # Translate to the object's center

        glTranslatef(-self.center[0], -self.center[1], -self.center[2])

        glEnableClientState(GL_VERTEX_ARRAY)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glVertexPointer(3, GL_FLOAT, 0, None)

        
        glColor3f(1, 1, 1)
        glDrawArrays(GL_TRIANGLES, 0, len(self.flat_vertices) // 3)

        # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        # glColor3f(0, 0, 0)
        # glDrawArrays(GL_TRIANGLES, 0, len(flat_vertices) // 3)
        # glDisableClientState(GL_VERTEX_ARRAY)

        glPopMatrix()
        self.update()


    
        

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(40, width / height, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = AnimatedGraph()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    sys.exit(app.exec_())

