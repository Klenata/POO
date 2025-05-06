from biblioteca import Pessoa

aluno01 = Pessoa("Kleber", 21, 110.8)
aluno02 = Pessoa("Guilherme", 21, 82)
aluno03 = Pessoa("Victor", 20, 76)

print(aluno01.name)
print(aluno01.age)
print(aluno01.weight)
print(aluno01.comendo)
aluno01.comer("Pipoca")
print(aluno01.comendo)