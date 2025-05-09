from biblioteca_2 import Banco

usuario1 = Banco("Kleber", "0001")
usuario2 = Banco("Guilherme", "0002")

usuario1.ativarConta()
usuario1.deposito(float(input("Valor a depositar: ")))
usuario1.deposito(float(input("Valor a depositar: ")))
usuario1.deposito(float(input("Valor a depositar: ")))
usuario1.saldo()