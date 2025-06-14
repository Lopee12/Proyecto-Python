class Cliente:
    def __init__(self, id_cliente, nombre, correo, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.saldo = saldo

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.id_cliente}"
    
    def actualizar_correo(self, nuevo_correo):
        # Actualiza el correo electrónico del cliente.

        if not nuevo_correo or "@" not in nuevo_correo:
            print("❌ Correo inválido. Asegúrese de que contenga '@'.")
            return

        if self.correo == nuevo_correo:
            print("ℹ️ El correo ya está actualizado.")
            return

        print(f"🔄 Actualizando correo de {self.correo} a {nuevo_correo}...")
        self.correo = nuevo_correo
        print(f"📧 Correo actualizado a: {self.correo}")

    def agregar_saldo(self, monto):
        #Agrega saldo a la cuenta del cliente.
        
        if not isinstance(monto, (int, float)):
            print("❌ El monto debe ser un número.")
            return

        if monto > 0:
            self.saldo += monto
            print(f"💰 Se agregaron ${monto:.2f}. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("❌ El monto debe ser positivo.")

    