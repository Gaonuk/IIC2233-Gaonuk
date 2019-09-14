from abstracts import Persona



class Piloto(Persona):
    def __init__(self, nombre, dinero, personalidad, contextura, equilibrio, experiencia, equipo):
        super().__init__(nombre, personalidad, contextura, equilibrio, experiencia, equipo)
        self._dinero = dinero


    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def set_dinero(self, dinero):
        self.dinero = dinero

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def set_experiencia(self, exp):
        self.experiencia = exp

    @property
    def contextura(self):
        return self._contextura
    
    @contextura.setter
    def set_contextura(self, cont):
        self.contextura = cont
    

    def __str__(self):
        return \
        'Piloto {0}\n \
- Dinero: {1}\n \
- Personalidad: {2}\n \
- Contextura: {3}\n \
- Equilibro: {4}\n \
- Experiencia: {5}\n \
- Equipo: {6}\n \
            '.format(self._nombre, self.dinero, 
            self._personalidad, self.contextura, 
            self._equilibrio, self.experiencia, 
            self._equipo)




class Contrincante(Persona):
    def __init__(self, nombre, nivel, personalidad, contextura, equilibrio, experiencia, equipo):
        super().__init__(nombre, personalidad, contextura, equilibrio, experiencia, equipo)
        self._nivel = nivel
        