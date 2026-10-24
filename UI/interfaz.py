import os
from API.cuenta import Cuenta

class UI:
    def __init__(self):
        self.cuenta_clientes = []
        self.archivo_datos = "cuentas.txt"
        self.SEPARADOR = ","
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(self.SEPARADOR)
                        # Posiciones: 0=numero, 1=documento, 2=nombre, 3=saldo
                        cuenta_recuperada = Cuenta(int(datos[0]), int(datos[1]), datos[2], float(datos[3]))
                        self.cuenta_clientes.append(cuenta_recuperada)

    def guardar_datos(self):
        with open(self.archivo_datos, "w") as archivo:
            for cuenta in self.cuenta_clientes:
                linea = f"{cuenta.numero_cuenta}{self.SEPARADOR}{cuenta.documento_identidad}{self.SEPARADOR}{cuenta.nombre}{self.SEPARADOR}{cuenta.saldo}\n"
                archivo.write(linea)

    def iniciar(self):
        while True:
            print("\n--- MENÚ BANCARIO ---")
            print("1. Crear nueva cuenta")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Mostrar todas las cuentas")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_cuenta()
            elif opcion == "2":
                self.depositar()
            elif opcion == "3":
                self.retirar()
            elif opcion == "4":
                self.mostrar_todas_las_cuentas()
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    @staticmethod
    def leer_entero(mensaje: str):
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada inválida: debe ingresar un número entero.")
            return None

    @staticmethod
    def leer_decimal(mensaje: str):
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida: debe ingresar un número.")
            return None

    def crear_cuenta(self):
        print("\n--- REGISTRO DE CUENTA ---")
        numero = self.leer_entero("Ingrese el número de cuenta: ")
        if numero is None: return
        
        if self.buscar_cuenta(numero):
            print("Ya existe una cuenta con ese número.")
            return

        doc = self.leer_entero("Ingrese el documento de identidad: ")
        if doc is None: return

        nombre = input("Ingrese el nombre del titular: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        if self.SEPARADOR in nombre:
            print(f"El nombre no puede contener el carácter '{self.SEPARADOR}'.")
            return

        saldo = self.leer_decimal("Ingrese el saldo inicial: ")
        if saldo is None: return
        
        if saldo < 0:
            print("El saldo inicial no puede ser negativo.")
            return

        self.cuenta_clientes.append(Cuenta(numero, doc, nombre, saldo))
        self.guardar_datos()
        print("¡Cuenta creada y almacenada con éxito!")

    def buscar_cuenta(self, numero: int):
        for cuenta in self.cuenta_clientes:
            if cuenta.numero_cuenta == numero:
                return cuenta
        return None

    def depositar(self):
        numero = self.leer_entero("\nIngrese el número de cuenta para el depósito: ")
        if numero is None: return
        
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            monto = self.leer_decimal("Ingrese la cantidad a depositar: ")
            if monto is None: return
            cuenta.depositar_dinero(monto)
            self.guardar_datos()
        else:
            print("Cuenta no encontrada.")

    def retirar(self):
        numero = self.leer_entero("\nIngrese el número de cuenta para el retiro: ")
        if numero is None: return
        
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            monto = self.leer_decimal("Ingrese la cantidad a retirar: ")
            if monto is None: return
            cuenta.retirar_dinero(monto)
            self.guardar_datos()
        else:
            print("Cuenta no encontrada.")

    def mostrar_todas_las_cuentas(self):
        print("\n--- LISTADO DE CUENTAS ---")
        if not self.cuenta_clientes:
            print("No hay cuentas registradas en la lista.")
            return
            
        for cuenta in self.cuenta_clientes:
            print(cuenta.mostrar_datos())