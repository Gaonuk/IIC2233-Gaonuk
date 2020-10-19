from abstracts import Pista

class PistaHielo(Pista):
    def __init__(self, hielo=0, **kwargs):
        super().__init__(**kwargs)
        self._hielo = hielo

    def get_tipo(self):
        return 'pista hielo'

    
class PistaRocosa(Pista):
    def __init__(self,rocas=0, **kwargs):
        super().__init__(**kwargs)
        self._rocas = rocas

    def get_tipo(self):
        return 'pista rocosa'


class PistaSuprema(PistaHielo, PistaRocosa):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def get_tipo(self):
        return 'pista suprema'

if __name__ == "__main__":
    p1 = PistaRocosa(nombre='wea',rocas=20,dificultad=750,vueltas=2,contrincantes=['Pepe', 'Juan'], largo=30)
    p3 = PistaSuprema(nombre='wea',hielo=1,rocas=20,dificultad=750,
        vueltas=2,contrincantes=['Pepe', 'Juan'], largo=30)  

    print(p1._rocas)
    print(p3._rocas)
    print(p3._hielo)