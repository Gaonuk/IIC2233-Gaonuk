class Piloto:
    def __init__(self, nombre, saldo, personalidad, contextura ,
         equilibrio, experiencia, equipo):
        self._nombre = nombre
        self._saldo = saldo
        self._personalidad = personalidad
        self._experiencia = experiencia
        self._contextura = contextura
        self._equilibrio = equilibrio
        self._equipo = equipo


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def set_saldo(self, saldo):
        self.saldo = saldo

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
            '.format(self._nombre, self.saldo, 
            self._personalidad, self.contextura, 
            self._equilibrio, self.experiencia, 
            self._equipo)