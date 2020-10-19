import socket
import json
import pickle

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        self.host = socket.gethostname()
        self.port = 9000
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.
            self.socket_cliente.connect((self.host, self.port))
            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        largo = int.from_bytes(self.socket_cliente.recv(4), byteorder='big')
        bytes_recibidos = self.socket_cliente.recv(largo) 

        # Debe haber un string para imprimirse
        pakete = pickle.loads(bytes_recibidos)
        # Debe haber un boolean para saber si continuar funcionando

        mensaje = pakete['mensaje']
        continuar = pakete['continuar']

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar

        if input_usuario in ['\juego_nuevo', '\salir']:
            return {'tipo': input_usuario, 'jugada': None}

        if ' ' in input_usuario:
            jugada, columna = input_usuario.split(' ')
            if columna.isnumeric() and jugada == '\jugada':
                return {'tipo': jugada,'jugada': int(columna)}
            
            return None

        return None

        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje
        # print(accion)
        mensaje_codificado = json.dumps(accion)
        largo = len(mensaje_codificado)
        self.socket_cliente.sendall(largo.to_bytes(4, byteorder='big'))
        bytes_mensaje = mensaje_codificado.encode('utf-8')
        # print(mensaje_codificado)
        # print(bytes_mensaje)
        self.socket_cliente.sendall(bytes_mensaje)

        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
