import os
from API.cuenta import Cuenta

class UI:
    def __init__(self):
        self.cuenta_clientes = []
        self.archivo_datos = "cuentas.txt"
        self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            with open(self.archivo_datos, "r") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        datos = linea.split(",")
                        # Posiciones: 0=numero, 1=documento, 2=nombre, 3=saldo
                        cuenta_recuperada = Cuenta(int(datos[0]), int(datos[1]), datos[2], float(datos[3]))
                        self.cuenta_clientes.append(cuenta_recuperada)

    def guardar_datos(self):
        with open(self.archivo_datos, "w") as archivo:
            for cuenta in self.cuenta_clientes:
                linea = f"{cuenta.numero_cuenta},{cuenta.documento_identidad},{cuenta.nombre},{cuenta.saldo}\n"
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

    def crear_cuenta(self):
        print("\n--- REGISTRO DE CUENTA ---")
        numero = int(input("Ingrese el número de cuenta: "))
        doc = int(input("Ingrese el documento de identidad: "))
        nombre = input("Ingrese el nombre del titular: ")
        saldo = float(input("Ingrese el saldo inicial: "))
        
        nueva_cuenta = Cuenta(numero, doc, nombre, saldo)
        self.cuenta_clientes.append(nueva_cuenta)
        self.guardar_datos() # Guarda en el txt inmediatamente
        print("¡Cuenta creada y almacenada con éxito!")

    def buscar_cuenta(self, numero: int):
        for cuenta in self.cuenta_clientes:
            if cuenta.numero_cuenta == numero:
                return cuenta
        return None

    def depositar(self):
        numero = int(input("\nIngrese el número de cuenta para el depósito: "))
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            monto = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar_dinero(monto)
            self.guardar_datos()
        else:
            print("Cuenta no encontrada.")

    def retirar(self):
        numero = int(input("\nIngrese el número de cuenta para el retiro: "))
        cuenta = self.buscar_cuenta(numero)
        if cuenta:
            monto = float(input("Ingrese la cantidad a retirar: "))
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