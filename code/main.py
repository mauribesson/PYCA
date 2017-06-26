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


#Puerto serial por defecto 
PORT = "COM5"

'''
arduinoSerial = serial.Serial(PORT,9600)

'''

#================================#
#             UI                 #
#================================# 

class MainWindow(QMainWindow):
    
    def __init__(self): 
      super(MainWindow, self).__init__() 
      self.ui = uic.loadUi("./ui/main.ui", self) 
      self.ui.setWindowIcon(QIcon("./ui/img.ico"))
      self.ui.setWindowTitle("PYCA © - Asistente de comercio")
      #lectura de arduino
      #agregar try para validar si esta conectado el arduino 
      '''try:
          self.arduinoSerial(serial.Serial(PORT,9600))
      except ValueError:
          print("El puerto "+ PORT + "No es correcto, verifique la conexion del Arduino.")    
       '''   
          
      #Lectura del puerto
      self.setDefaultPort()
      self.ui.BtnPortUpdate.clicked.connect(self.readPort)        
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
        
    #Actualizacion de puerto
    def readPort(self):
        print("Leer puerto")      
        PORT = self.ui.updatePortTextLine.text()  
        self.ui.updatePortTextLine.setText(PORT)
        self.arduinoSerial = serial.Serial(PORT,9600)
        pass
        
    def setDefaultPort(self):
        self.ui.updatePortTextLine.setText(PORT)
        pass 
        
    pass



''' INICIO DE APLICACION'''

print("Cargando Aplicacion...")

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec_()











