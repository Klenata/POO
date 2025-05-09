class Banco():
    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self.valor = 0
        self.status = False

    def ativarConta(self):
        if  not self.status:
            self.status = True
            print("Conta ativada com sucesso!")
        else:
            print("Conta já estava ativada")

    def deposito(self, deposito):
        if self.status:
            self.valor = deposito + self.valor
            print(f"Depósito de R${deposito:.2f} Realizado com sucesso.")
        else:
            print("Sua conta está desativada")

    def saque(self, saque):
        if self.status:
            if saque > self.valor:
                print(f"Você só tem R${self.valor} na conta")
            else:
                self.valor = self.valor - saque
        else:
            print("Sua conta está desativada")

    def saldo(self):
        if self.status:
            saldo = self.valor
            print(f"R${saldo:.2f}")
        else:
            print("Sua conta está desativada")

    def desativarConta(self):
        if self.valor == 0:
            self.status = False
            print("Conta desativada, com sucesso.")
        else:
            print("Conta não pode ser desativada")

    #def limite(self):
