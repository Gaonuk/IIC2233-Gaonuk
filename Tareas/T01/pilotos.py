from abstracts import Persona



class Piloto(Persona):
    def __init__(self, nombre, dinero, 
        personalidad, contextura, equilibrio, 
        experiencia, equipo):
        super().__init__(nombre, personalidad, 
            contextura, equilibrio, experiencia, equipo)
        self._dinero = dinero


    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, dinero):
        self._dinero = dinero
    

    def __str__(self):
        impresion = 'Piloto {0}\n'.format(self._nombre)
        impresion += '- Dinero: {0}\n'.format(self.dinero)
        impresion += '- Personalidad: {0}\n'.format(self._personalidad) 
        impresion += '- Contextura: {0}\n'.format(self.contextura)
        impresion += '- Equilibro: {0}\n'.format(self._equilibrio)
        impresion += '- Experiencia: {0}\n'.format(self.experiencia)
        impresion += '- Equipo: {0}\n'.format(self._equipo)
        return impresion
            




class Contrincante(Persona):
    def __init__(self, nombre, nivel, 
            personalidad, contextura, 
            equilibrio, experiencia, equipo):
        super().__init__(nombre, personalidad, 
            contextura, equilibrio, experiencia, equipo)
        self._nivel = nivel
        