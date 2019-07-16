class Temporizador:

    def __init__(self):
        self.hora=Hora()
        self.minuto=Minuto()
        self.segundo=Segundo()


    def retroceder(self): #sincroniza un retroceso con las unidades de tiempo#
        self.segundo.retroceder()
        if (self.segundo.valor == self.segundo.tope): #pregunta"
            self.minuto.retroceder()
            if (self.minuto.retroceder.valor == self.minuto.tope): #los parentesis no son necesarios#
                self.hora.retroceder ()
                if (self.hora.retroceder.valor == self.hora.tope):


class UnidadTiempo:
    def __int__(self):
        self.valor= 0
        self.tope= 0

    
        



 
    
