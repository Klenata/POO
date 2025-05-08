class Banco():
    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self.saldo = 0
        self.status = False

    def ativarConta(self):
        if self.status == False:
            self.status = True
            print("Conta ativada com sucesso!")
        else:
            print("Conta já estava ativada")

    def deposito(self, deposito):
        if self.status:
            self.saldo = deposito + self.saldo
            print(f"Seu saldo atual é de R${self.saldo:.f}")
        else:
            print("Sua conta está desativada")

    def saque(self):

    def saldo(self):
        print(self.saldo)

    def desativarConta(self):
        if self.saldo == 0:
            self.status = False
            print("Conta desativada, com sucesso.")
        else:
            print("Conta não pode ser desativada")

    def limite(self):
