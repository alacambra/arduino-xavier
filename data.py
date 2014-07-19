#!/usr/bin/python
# -*- coding=UTF-8 -*-

""" Programa que envía por el puerto serie información a una Arduino para cambiar el color de una led """

import sys, serial, time
from PyQt4 import QtGui, QtCore

# Importamos lo necesario para la GUI
from ledcoloresGUI import Ui_MainWindow

class Principal(QtGui.QMainWindow):
    # Definimos el constructor de la clase __init__
    def __init__(self):
        # Se llama al constructor de la clase padre
        QtGui.QMainWindow.__init__(self)

        # Se crea la instancia de Ui_MainWindow
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        #variables para los colores
        self.rojo = 255
        self.verde = 255
        self.azul = 255
        
        # Se conectan las señales con los slots
        self.connect(self.ventana.pushButton, QtCore.SIGNAL("clicked()"), self.enviarDatos) # Para cuando haga clic en el botón
        self.connect(self.ventana.dialRojo, QtCore.SIGNAL("valueChanged(int)"), self.valorRojo) # Para cuando varíe el valor del dialRojo
        self.connect(self.ventana.dialVerde, QtCore.SIGNAL("valueChanged(int)"), self.valorVerde) # Para cuando varíe el valor del dialVerde
        self.connect(self.ventana.dialAzul, QtCore.SIGNAL("valueChanged(int)"), self.valorAzul) # Para cuando varíe el valor del dialAzul
    
    # Ha variado el valor del dialRojo, lo mostramos en labelRojo y guardamos el nuevo valor en la variable rojo
    def valorRojo(self, value):
        self.ventana.labelRojo.setText(str(value))
        self.rojo = value   
        # pintamos la muestra
        p = self.palette() # creamos un objeto paleta
        p.setColor(QtGui.QPalette.Window, QtGui.QColor(self.rojo, self.verde, self.azul)) # cambiamos el color Window del palette
        self.ventana.frameColor.setPalette(p) # aplicamos el palette al frameColor (la muestra)       
 
    # Ha variado el valor del dialVerde, lo mostramos en labelVerde y guardamos el nuevo valor en la variable verde
    def valorVerde(self, value):
        self.ventana.labelVerde.setText(str(value))
        self.verde = value    
        # pintamos la muestra
        p = self.palette() # creamos un objeto paleta
        p.setColor(QtGui.QPalette.Window, QtGui.QColor(self.rojo, self.verde, self.azul)) # cambiamos el color Window del palette
        self.ventana.frameColor.setPalette(p) # aplicamos el palette al frameColor (la muestra)          

    # Ha variado el valor del dialAzul, lo mostramos en labelAzul y guardamos el nuevo valor en la variable azul    
    def valorAzul(self, value):
        self.ventana.labelAzul.setText(str(value))
        self.azul = value
        # pintamos la muestra
        p = self.palette() # creamos un objeto paleta
        p.setColor(QtGui.QPalette.Window, QtGui.QColor(self.rojo, self.verde, self.azul)) # cambiamos el color Window del palette
        self.ventana.frameColor.setPalette(p) # aplicamos el palette al frameColor (la muestra)            
        
    def enviarDatos(self):
        # /dev/ttyACM0 = Arduino Uno en Linux
        # /dev/ttyUSB0 = Arduino Duemilanove en Linux
        # ante la duda, abrir el IDE de Arduino y lo vemos en Herramientas > Puerto Serial
        
        try:
             # creamos un objeto para acceder al puerto serie
             arduino = serial.Serial("/dev/ttyACM0", 9600 , timeout = 1) # 9600 es la velocidad del puerto serie
             time.sleep(2) # esperamos a que la arduino esté lista
        except serial.SerialException:
	     print "Error al abrir el puerto /dev/ttyACM0" # si hemos abierto por consola el programa, veremos el error
	     return False
             #time.sleep(2) #esperamos a la inicialización...
        
        # enviamos los colores en formato R,G,B donde R,G y B son enteros entre 0 y 255. 
        # El último caracter es para distinguir dónde termina la cadena
        colorLed = str(self.rojo) + ',' + str(self.verde) + ',' + str(self.azul) + '\n'
        arduino.write(colorLed.encode('ascii'))
        
        #finalizamos la conexión con la arduino
        arduino.close() 
                    
# Esta línea es obligatoria en todas las aplicaciones PyQt
app = QtGui.QApplication(sys.argv)

# Se crea una instancia de la clase
ventanita = Principal()
#mostramos la ventana
ventanita.show()
# Se ejecuta y espera a que termine la aplicación
sys.exit(app.exec_())