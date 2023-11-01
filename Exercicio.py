class banco:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0
        self.saldo = 0
        self.deposito = False
        self.sacar = 0
        self.saldoAtual = False
        self.desativar = False
        self.ativar = False

    def ativarConta(self):
        if self.status == False:
            print(f"A conta {self.numero} foi ativada")
            self.status = True
        else:
            print(f"A conta {self.numero} já está ativada")
    def depositar(self, valor):
        if self.status == True:
            self.saldo = self.saldo + valor
            print("Deposito realizado com sucesso")
        else:
            print("A conta encontra-se desativada, procure uma agencia para ativar.")
    def retirada(self, saque):
        if self.status == True:
            if self.saldo > 0:
                self.saldo = self.saldo - saque
                print("Saque realizado com sucesso")
            else:
                print("A conta não possui saldo !")
        else:
            print("A conta encontra-se desativada, procure uma agencia para ativar")
    def cancelar(self):
        if self.status == True:
            if self.saldo == 0:
                print("A conta foi cancelada")
            else:
                print("A conta possui saldo, não e possivel cancelar")
        else:
            print("A conta já está cancelada")
    def verificarSaldo(self):
        if self.status == True:
            print(f"O Saldo atual é {self.saldo}")
        else:
            print("A conta encontra-se desativada, procure uma agencia para ativar")
    def credito(self):
        if self.status == True:
            if self.ativar == False:
                self.limite = 1000
                print("A conta de credito foi liberada, e recebeu 1000,00 de limite! ")
                self.ativar = True
            else:
                print("O Credito não foi liberado !")
        else:
            print("A conta encontra-se desativada, procure uma agencia para ativar")
    def saqueLimite(self, saque):
        if self.status == True:
            if self.sacar > self.saldo:
                saque = self.saldo - self.sacar
                self.limite = self.limite - saque
                print(f"O S")
            else:
                saque = self.saldo - self.sacar
                print(f"O Saque de {saque} foi realizado com sucesso !")
        else:
            print("A conta encontra-se desativada, procure uma agencia para ativar")