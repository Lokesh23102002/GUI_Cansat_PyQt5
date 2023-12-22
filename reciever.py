from digi.xbee.devices import XBeeDevice
import time
import csv
from PyQt5.QtCore import QThread, pyqtSignal
import random
import time

class Reciever:
    
    def __init__(self, port, baud_rate):
        if port != "Test":
            self.device = XBeeDevice(port, baud_rate)
            self.device.open()
            self.callback = self.device.add_data_received_callback(self.recieve)
        else:
            self.device = None
            self.callback = None
            
    def recieve(self,xbee_message):
        print(xbee_message.data.decode("utf8"))
        return xbee_message.data.decode("utf8")


class LiveDataReader(QThread):
    data_updated = pyqtSignal(list)

    def __init__(self, csv_file,port,baud_rate):
        super().__init__()
        self.csv_file = csv_file
        self.datat = []
        if(port != "Test"):
            self.device = XBeeDevice(port,baud_rate)
            self.device.add_data_received_callback(self.recieve)
        else:
            self.device = None
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                self.datat = list(reader)
            self.rowno = 2000
            
        

        
    def recieve(self,xbee_message):
        self.data_updated.emit(xbee_message.data.decode("utf8"))

    def run(self):
        while True:
            # data,length = self.read_csv()
            self.data_updated.emit(self.datat[self.rowno])
            self.rowno += 1
            
            def random_sleep():
            
                time.sleep(0.5)  # Convert milliseconds to seconds
                # Or you can use time.sleep(sleep_time / 1000.0) for floating-point division

            random_sleep()

    
    # def read_csv(self):
    #     data = []
    #     with open(self.csv_file, 'r') as file:
    #         reader = csv.reader(file)
    #         for i,row in enumerate(reader):
    #             data.append(row)
    #     time.sleep(1)
    #     return data,len(self.datat)
    
       