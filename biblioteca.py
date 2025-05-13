class Pessoa():
    def __init__(self, nome, idade, peso):
        self.name=nome
        self.age=idade
        self.weight=peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.falando == False:
            if self.dormindo == False and self.comendo == False:
                self.falando = True
                print(f"{self.name} começou a falar.")
            else:
                print(f"{self.name} não pode falar, está ocupado.")
        else:
            print(f"{self.name} já está falando")

    def pararFalar(self):
        if self.falando == True:
            self.falando = False
        print(f"{self.name} parou de falar")


    def comer(self):
        if self.comendo == False:
            if self.dormindo == False and self.falando == False:
                self.comendo = True
                print(f"{self.name} começou a comer.")
            else:
                print(f"{self.name} não pode comer, está ocupado.")
        else:
            print(f"{self.name} já está comendo")

    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.name} parou de comer")
        else:
            print(f"{self.name} não está comendo")

    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False and self.falando == False:
                self.dormindo = True
                print(f"{self.name} começou a dormir.")
            else:
                print(f"{self.name} não pode dormir, está ocupado.")
        else:
            print(f"{self.name} já está dormindo")

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.name} acordou")
        else:
            print(f"{self.name} está acordado")

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

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self, comida):
        print(f"O {self.nome} foi comer {comida}...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando (miau)...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} foi latindo (au-au)")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"A {self.nome} foi mugindo (muu-muu)")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def guinchar(self):
        print(f"O {self.nome} foi guinchando (iiii iiiiii)")


class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"O valor do ingresso está custando R${self.valor:.2f}")

class VIP(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)
        self.valor *= 1.5

    def valorVIP(self):
        print(f"O valor VIP de ingresso é R${self.valor:.2f}")

class Forma():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def areaTriangulo(self):
        areaT = self.base * self.altura / 2
        print(areaT)

    def perimetroTriangulo(self):
        perimetroT = self.base * self.base + self.altura * self.altura
        hipotenusa = perimetroT ** 0.5
        perimetroFinal = self.base + self.altura + hipotenusa
        print(f"{perimetroFinal:.2f}")


class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def areaRetangulo(self):
        areaR = self.base * self.altura
        print(areaR)

    def perimetroRetangulo(self):
        perimetroR = (self.base + self.altura)*2
        print(perimetroR)

class Atleta():
    def __init__(self):
        self.aposentado = False
        self.aquecido = False
    def aposentar(self):
        print("Aposentado")
        self.aposentado = True

    def aquecer(self):
        print("Aquecido")
        self.aquecido = True

class Corredor(Atleta):
    def __init__(self):
        super().__init__()

    def correr(self):
        if self.aposentado:
            print("Pode correr não, descansa.")
        else:
            if self.aquecer():
                print("Pode correr")
            else:
                print("Vá se aquecer primeiro")

class Nadador(Atleta):
    def __init__(self):
        super().__init__()

    def nadar(self):
        if self.aposentado:
            print("Pode nadar não, descansa.")
        else:
            if self.aquecer():
                print("Pode nadar")
            else:
                print("Vá se aquecer primeiro")

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()

    def pedalar(self):
        if self.aposentado:
            print("Pode nadar não, descansa.")
        else:
            if self.aquecer():
                print("Pode nadar")
            else:
                print("Vá se aquecer primeiro")


class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self):
        super().__init__()