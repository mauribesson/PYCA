# -*- coding: utf-8 -*-
"""
By: Mauricio Besson  


Pendintes:
- Leer ruta Por interfaz opernFile (HECHO)    
 
- Leer XML de install.config

- Ver posibilidad de usar un Subproceso (Por ahora no es nesesario) 

- Parseo de barras en PATH -> (HECHO) 

- Agregar Archivo de log VER: https://msdn.microsoft.com/es-es/library/50614e95(v=vs.110).aspx  

- Agregar espesificacion de Frmework para instalar 

- AGREGAR COMILLAS PARA PATH CON ESPACIO -> (HECHO)  

- Parametrizar Vercion del Framework, Radiobutton       

- Ver configuracion de PUERTOS de e-flow  

"""

import os
import sys
#xml
import xml.etree.ElementTree as ET

#PyQt5
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog

#================================#
#          Logica                #
#================================#

DEBUG = True

class Installer:    
    def __init__(self): 
        self. space = ' '   
        pass
        
    def install(self):         
        os.system('CD "C:\\"')
        os.system(str(self.fwPath) + str(self.space) + str(self.command) + str(self.space) + "\"" + str(self.middlewareServicePath) + "\"")
        os.system(str(self.fwPath) + str(self.space) + str(self.command) + str(self.space) + "\"" + str(self.middlewareNodeServicePath) + "\"")             
        pass    
       
    
    #getter y setter  
    @property 
    def fwPath(self):
        return self.__fwPath 
         
    @fwPath.setter
    def fwPath(self, pPath):
        self.__fwPath  = pPath  
        
    @property
    def command(self):
        return self.__command
    
    @command.setter
    def command(self, pCommand):
        self.__command = pCommand
        
    @property
    def middlewareNodeServicePath(self):
        return self.__middlewareNodeServicePath
        
    @middlewareNodeServicePath.setter
    def middlewareNodeServicePath(self, pPath):
        self.__middlewareNodeServicePath = pPath
        
    @property
    def pathMiddlewareConfigInstallFile(self):
        return self.__pathMiddlewareCofigInstallFile
        
    @pathMiddlewareConfigInstallFile.setter
    def pathMiddlewareCofigInstallFile(self, pPath):
        self.__pathMiddlewareCofigInstallFile = pPath            
        
    @property
    def pathMiddlewareNodeConfigInstallFile(self):
        return self.__pathMiddlewareNodeCofigInstallFile
        
    @pathMiddlewareNodeConfigInstallFile.setter
    def pathMiddlewareNodeCofigInstallFile(self, pPath):
        self.__pathMiddlewareNodeCofigInstallFile = pPath       
     
        

"""Parseo de XML servicios (NO ESTA IMPLENTADO) """      
class XmlServises:
    def __init__(self):
        self.path = ""
        self.file = ""
        pass    
        
    def readXmL(self, path):
        #agregar la lectura del archivo
        tree = ET.parse(self.path)
        root = tree.getroot()      
        pass    
   
    def updateXml(self):
        #self.pathMiddlewareCofigInstallFile = 'D:/CODE/Proyectos/Tools/pyServicesInstall/TEST/Sidesys.Services.ApplicationService.Install.config'
        tree = ET.parse(self.pathMiddlewareConfigInstallFile)
        root = tree.getroot()
        #              desplay           service
        #print(str(root[0][0].text), str(root[0][1].text))
        #desplay
        root[0][0].text = self.newDisplayName
        root[0][0].set('updated', 'yes')
        #service
        root[0][1].text = self.newServiceName
        root[0][1].set('updated', 'yes')
        tree.write(self.pathMiddlewareConfigInstallFile)
        pass
    
    @property
    def path(self):
        return self.__path
    
    @path.setter
    def path(self, pPath):
        self.__path = pPath
    
    @property
    def newDisplayName(self):
        return self.__newDisplayName
    
    @newDisplayName.setter
    def newDisplayName(self, pNewDisplayName):
        self.__newDisplayName = pNewDisplayName   
        
    @property
    def newServiceName(self):
        return self.__newServiceName
    
    @newServiceName.setter
    def newServiceName(self, pNewServiceName):
        self.__newServiceName = pNewServiceName 
                
        
'''============================================================'''              


#================================#
#             UI                 #
#================================# 

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__() 
        self.initUI()
             
    def initUI(self):
        self.ui = uic.loadUi('main.ui', self) 
        self.ui.setWindowIcon(QIcon('img.ico'))
        self.ui.setWindowTitle('Instalar servicios e-Flow')   
        self.ui.show()        
        self.ui.ButtonInstall.clicked.connect(self.InstallEvent)
        self.ui.ButtonUnInstall.clicked.connect(self.UnInstallEvent)
        self.ui.ButtonOpenFileMiddleware.clicked.connect(self.showOpenFileMiddleware)
        self.ui.ButtonOpenFileMiddlewareNode.clicked.connect(self.showOpenFileMiddlewareNode)
        pass
        
    def InstallEvent(self):
        i = Installer()
        i.fwPath = 'C:\\Windows\Microsoft.NET\\Framework\\v4.0.30319\\installUtil.exe' 
        i.command = '-i'
        #getText
        i.middlewareServicePath = self.ui.lineEditMwPath.text().replace("\\", "\\\\")#Se agrego el parseo de PATH          
        if DEBUG :  
            print('SE LEYO LA RUTA DEL MIDDLEWARE: ' + i.middlewareServicePath)
        #i.middlewareServicePath = 'D:\\CODE\\Proyectos\\Tools\\pyServicesInstall\\TEST\\Middleware\\STE\\bin\\Sidesys.Services.ApplicationService.exe'
        i.middlewareNodeServicePath = self.ui.lineEditMwnPath.text().replace("\\", "\\\\")
        if DEBUG :  
            print('SE LEYO LA RUTA DEL MIDDLEWARENODE: ' + i.middlewareNodeServicePath)
        
        i.install()  
        pass
        
    def UnInstallEvent(self):
        u = Installer()
        u.fwPath = 'C:\\Windows\Microsoft.NET\\Framework\\v4.0.30319\\installUtil.exe' 
        u.command = '-u'
        #getText
        u.middlewareServicePath = self.ui.lineEditMwPath.text().replace("\\", "\\\\")#Se agrego el parseo de PATH          
        if DEBUG :  
            print('SE LEYO LA RUTA DEL MIDDLEWARE: ' + u.middlewareServicePath)
        #i.middlewareServicePath = 'D:\\CODE\\Proyectos\\Tools\\pyServicesInstall\\TEST\\Middleware\\STE\\bin\\Sidesys.Services.ApplicationService.exe'
        u.middlewareNodeServicePath = self.ui.lineEditMwnPath.text().replace("\\", "\\\\")
        if DEBUG :  
            print('SE LEYO LA RUTA DEL MIDDLEWARENODE: ' + u.middlewareNodeServicePath)
        
        u.install()
        pass
        
        
    def showOpenFileMiddleware(self):
        fname = QFileDialog.getOpenFileName(self, 'Abrir Middleware Service')      
        self.ui.lineEditMwPath.setText(fname[0])         
        pass
    
    def showOpenFileMiddlewareNode(self):
        fname = QFileDialog.getOpenFileName(self, 'Abrir MiddlewareNode Service')              
        self.ui.lineEditMwnPath.setText(fname[0])         
        pass
        
        
        
'''===============================================''' 
     
              
def runApp():
    app = QApplication(sys.argv)
    mainWin = MainWindow()       
    sys.exit(app.exec_())
    print('App run!')  
  
    

if __name__ == '__main__':
    runApp()

 