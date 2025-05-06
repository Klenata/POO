class Pessoa():
    def __init__(self, nome, idade, peso):
        self.name=nome
        self.age=idade
        self.weight=peso
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self):
        if self.dormindo == False and self.comendo == False:
            self.falando = True
            print(f"{self.name} começou a falar.")
        else:
            print("Ele não pode falar, está ocupado.")


    def comer(self, comida):
        if self.dormindo == False and self.falando == False:
            self.comendo = True
            print(f"{self.name} começou a comer.")
        else:
            print("Ele não pode comer, está ocupado.")

    def dormir(self):
        if self.comendo == False and self.falando == False:
            self.dormindo = True
            print(f"{self.name} começou a dormir.")
        else:
            print("Ele não pode dormir, está ocupado.")