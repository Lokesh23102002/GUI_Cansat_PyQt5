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
        self.csv_file = None
        self.data_updated.connect(self.update_csv)
        self.datat = []
        if(port != "Test"):
            self.device = XBeeDevice(port,baud_rate)
            self.device.add_data_received_callback(self.recieve)
        else:
            self.device = "Test"
            with open("Data.csv", 'r') as file:
                reader = csv.reader(file)
                self.datat = list(reader)
            self.rowno = 2000
            
        

    def connect(self,port,baud_rate):
        self.device = XBeeDevice(port,baud_rate)
        self.device.open()
        self.device.add_data_received_callback(self.recieve)
        
    def recieve(self,xbee_message):
        
        self.data_updated.emit(xbee_message.data.decode("utf8").split(","))

    def run(self):
        while True:
            # data,length = self.read_csv()
            self.data_updated.emit(self.datat[self.rowno])
            
            self.rowno += 1

            def random_sleep():
            
                time.sleep(0.2)  # Convert milliseconds to seconds
                # Or you can use time.sleep(sleep_time / 1000.0) for floating-point division

            random_sleep()

    def stop(self):
        self.terminate()
        self.wait()

    def update_csv(self,data):
        if self.csv_file is not None:
            with open(self.csv_file, 'a') as file:
                writer = csv.writer(file)
                writer.writerow(data)
            
       
        
    # def read_csv(self):
    #     data = []
    #     with open(self.Data.csv, 'r') as file:
    #         reader = csv.reader(file)
    #         for i,row in enumerate(reader):
    #             data.append(row)
    #     time.sleep(1)
    #     return data,len(self.datat)
    
       