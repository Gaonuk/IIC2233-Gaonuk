from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        super().__init__(id_cliente, nombre, contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.saldo

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        '''
        Completar: Recuerda que si el saldo es menor a 0, entonces este cliente
        si tiene un fraude
        '''
        if nuevo_saldo < 0:
            self.saldo = nuevo_saldo
            self.tiene_fraude = True
        else:
            self.saldo = nuevo_saldo
            self.tiene_fraude =  False

    def deposito_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        self.depositar(dinero)
        self.saldo_actual = self.saldo_actual
        # Asumi que no hay que actualizar el saldo_actual dado que
        # en la funcion depositar heredada de la clase Cliente
        # ya se actualiza el saldo del Cliente

        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            transaccion = str(self.id_cliente) + ', ' + 'depositar' + ', ' + str(dinero)
            archivo.write(transaccion)
            

    def retiro_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''

        if not self.tiene_fraude:
            # Aqui pongo un pass dado que no se indica nada que hacer en caso 
            # de que el Cliente sea fraudulento
            pass
        else:
            self.retirar(dinero)
            self.saldo_actual = self.saldo_actual
            ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
            with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
                retiro = str(self.id_cliente) + ', retiro, ' + str(dinero)
                archivo.write(retiro)



class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        super().__init__()
        

    def cargar_clientes(self, ruta):
        with open(ruta, 'r', encoding="utf-8") as file:
            for line in file:
                    id_cliente, nombre, saldo, contrasena = line.strip().split(",")

                    instancia_cliente = ClienteSeguro(id_cliente, nombre, contrasena)
                    instancia_cliente.saldo = saldo
                    self.clientes.append(instancia_cliente)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        cliente = self.buscar_cliente(id_cliente)
        if not cliente == None:
            if accion == 'depositar':
                cliente.deposito_seguro(dinero)
            elif accion == 'retirar':
                cliente.retiro_seguro(dinero)

        else:
            pass

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        for transaccion in historial:
            for cliente in self.clientes:
                id_cliente, accion, monto = transaccion.split(',')
                if id_cliente == cliente.id_cliente:
                    if monto > cliente.saldo_actual and accion == 'retirar':
                        cliente.tiene_fraude = True
        

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        
