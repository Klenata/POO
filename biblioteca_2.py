class Banco():
    def __init__(self, nome, conta):
        self.nome = nome
        self.conta = conta
        self.valor = 0
        self.status = False
        self.credito = 1000
        self.limiteCredito = 1000

    def ativarConta(self):
        if  not self.status:
            self.status = True
            print("Conta ativada com sucesso!")
            print("")
        else:
            print("Conta já estava ativada")
            print("")

    def tipoConta(self, tipo):
        if self.status:
            while 3 < tipo < 0:
                print("Opção invalida, tente novamente")
            else:
                if tipo == 1:
                    print("Conta Corrente")
                else:
                    print("Conta Poupança")
        else:
            print("Sua conta está desativada")


    def deposito(self, deposito):
        if self.status:
            if deposito <= 0:
                print("Depósito inválido")
            else:
                falta_credito = self.limiteCredito - self.credito
                if falta_credito > 0:
                    if deposito >= falta_credito:
                        self.credito = self.limiteCredito
                        self.valor += (deposito - falta_credito)
                    else:
                        self.credito += deposito
                else:
                    self.valor += deposito
                print(f"Depósito de R${deposito:.2f} realizado com sucesso.\n")
        else:
            print("Sua conta está desativada\n")

    def saque(self, saque):
        if self.status:
            total_disponivel = self.valor + self.credito
            if saque <= 0:
                print("Saque inválido\n")
            elif saque > total_disponivel:
                print(f"Saldo insuficiente. Disponível: R${total_disponivel:.2f}\n")
            else:
                if saque <= self.valor:
                    self.valor -= saque
                else:
                    diferenca = saque - self.valor
                    self.valor = 0
                    self.credito -= diferenca
                print(f"Saque de R${saque:.2f} realizado com sucesso\n")
        else:
            print("Sua conta está desativada\n")

    def saldo(self):
        if self.status:
            print(f"Saldo disponivel: R${self.valor:.2f}")
            print(f"Crédito disponivel: R${self.credito:.2f}")
            print("")
        else:
            print("Sua conta está desativada")
            print("")

    def desativarConta(self):
        if self.valor == 0 and self.credito == self.limiteCredito:
            self.status = False
            print("Conta desativada, com sucesso.")
            print("")
        else:
            print("Conta não pode ser desativada")
            print("")

    def limite(self):
        if self.status:
            print(f"R${self.credito:.2f}")
            print("")