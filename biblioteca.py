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
            