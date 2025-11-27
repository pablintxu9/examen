class cuenta(self, titular, iban, saldo=0.0):
    self.titular=titular
    self.iban=iban
    self.saldo=saldo

    def ingresar(self, saldo):
        super().__init__(saldo)
        self.saldo += saldo
    def retirar(self, saldo):
        super().__init__(saldo)
        if self.saldo >= saldo:
            self.saldo -= saldo
        else:
            print("Fondos insuficientes")
    def __str__ (self):
        return f"Titular: {self.titular} IBAN: {self.iban} Saldo: {self.saldo}€"

class banco(self, cuentas):
    self.cuentas=[cuenta]
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    def buscar_cuenta(self, iban):
        for cuenta in self.cuentas:
            if cuenta.iban == iban:
                return cuenta
            else: 
                print("Cuenta no encontrada")
    def realizar_tranferencia(self, iban1, iban2, cantidad):
        cuenta1 = self.buscar_cuenta(iban1)
        cuenta2 = self.buscar_cuenta(iban2)
        if cuenta1 and cuenta2:
            if cuenta1.saldo>=cantidad
                cuenta1.retirar(cantidad)
                cuenta2.ingresar(cantidad)
            else:
                print("Fondos insuficientes para la transferencia")

    