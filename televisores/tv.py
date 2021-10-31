
#
class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = True
        self.volumen = 1
        self.numTV += 1

    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca

    def getControl(self):
        return self.control
    
    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self, volumen):
        self.volumen = volumen

    def getCanal(self):
        return self.canal
    
    def setCanal(self, canal):
        self.canal = canal

    def getNumTV(self):
        return self.numTV

    def turnOn(self):
        if self.estado != "on": 
            self.estado = "on"

    def turnOff(self):
        if self.estado != "off": 
            self.estado = "off"

    def getEstado(self):
        return self.estado 

    def canalUp(self):
        if self.canal >= 1 and self.canal < 125:
            self.canal += 1

    def canalDown(self):
        if self.canal <= 125 and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.getEstado() == "on":
            if self.volumen >= 0 and self.volumen < 7:
                self.volumen += 1

    def volumenDown(self):
        if self.getEstado() == "on":
            if self.volumen <= 7 and self.volumen > 0:
                self.volumen -= 1