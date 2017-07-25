# -*- coding: utf-8 -*-
"""
 - Trabajo practico Arduino: PYCA© Sensor de moviminto luminocidad y temperatura. 

"""


import serial 
import sys
import time

#PyQt5
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog

'''
===============================================================
=========================================
|    Cofiguraciones por defecto         |
=========================================
'''
#Puerto serial por defecto 
PORT = "COM5"

#Distancia Minima -> tipo: FLOAT
MIN_DISTANCE = 1.0

#agregar como parametro
CONFIG = { 
            'PORT': "COM5",
            'MIN_DISTANCE': 1.0 
        }

'''
=========================================
|    /Cofiguraciones por defecto         |
=========================================
================================================================
'''



#==========================================
#arduinoSerial = serial.Serial(PORT,9600)


#================================#
#              UI                #
#================================# 

class MainWindow(QMainWindow):
    
    def __init__(self, pConfig): 
      super(MainWindow, self).__init__() 
      self.ui = uic.loadUi("./ui/main.ui", self) 
      self.ui.setWindowIcon(QIcon("./ui/img.ico"))
      self.ui.setWindowTitle("PYCA © - Asistente de comercio")
      
      #lectura de arduino
      #agregar try para validar si esta conectado el arduino 
      '''
      try:
          self.arduinoSerial(serial.Serial(PORT,9600))         
      except ValueError:
          print("El puerto "+ PORT + "No es correcto, verifique la conexion del Arduino.")  
      '''          
      #Lectura del puerto
      self.setDefaultPort()
      self.setDefaultMinDistance()
      self.ui.BtnPortUpdate.clicked.connect(self.readPort) 
      self.ui.BtnMinDistanceUpdate.clicked.connect(self.readMinDistance) 
      self.config = pConfig
      self.ui.show()       
      pass
  
    @property
    def port(self):
        return self.__port
    
    @port.setter
    def port(self, pPort):
        self.__port = pPort
        
    @property
    def arduinoSerial(self):
        return self.__arduinoSerial
    
    @port.setter
    def arduinoSerial(self, pArduinoSerial):
        self.__arduinoSerial = pArduinoSerial
        
    @property
    def config(self):
        return self.__config
    
    @port.setter
    def config(self, pConfig):
        self.__config = pConfig        
               
    #Actualizacion de puerto
    def readPort(self):           
        self.config()['PORT'] = self.ui.updatePortTextLine.text()  
        self.ui.updatePortTextLine.setText(self.config()['PORT'])
        self.arduinoSerial = serial.Serial(self.config()['PORT'], 9600)
        print("Lee puerto" + str(self.config()['PORT']))  
        pass
        
    def setDefaultPort(self):
        self.ui.updatePortTextLine.setText(self.config['PORT'])
        pass  
    
    def readMinDistance(self):            
        MIN_DISTANCE = self.ui.updateMinDistance.value()  
        self.ui.updateMinDistance.value(MIN_DISTANCE)
        print("Lee Distancia")         
        pass
    
    def setDefaultMinDistance(self):
        self.ui.updateMinDistance.setValue(MIN_DISTANCE)
        pass
        

'''=========================================================='''

''' INICIO DE APLICACION '''

print("Cargando Aplicacion...")

app = QApplication(sys.argv)
mainWindow = MainWindow(CONFIG)
mainWindow.show()
app.exec_()











