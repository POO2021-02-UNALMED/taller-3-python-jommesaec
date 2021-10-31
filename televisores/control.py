
class Control:
    
    def __init__(self):
        pass
        
    def enlazar(self, TV):
        self.tv = TV
        self.tv.setControl(self)

    def turnOn(self):
        if self.tv.estado != "on": 
            self.tv.estado = "on"

    def turnOff(self):
        if self.tv.estado != "off": 
            self.tv.estado = "off"

    def getEstado(self):
        return self.tv.estado 

    def canalUp(self):
        if self.canal >= 1 and self.canal < 125:
            self.canal += 1

    def canalDown(self):
        if self.canal <= 125 and self.canal > 1:
            self.canal -= 1
    
    def volumenUp(self):
        if self.getEstado() == "on":
            if self.tv.volumen >= 0 and self.tv.volumen < 7:
                self.tv.volumen += 1

    def volumenDown(self):
        if self.getEstado() == "on":
            if self.volumen <= 7 and self.volumen > 0:
                self.volumen -= 1

    def setCanal(self, canal):
        self.canal = canal

 

    def getTV(self):
        return self.tv

    def setTV(self, TV):
        self.tv = TV