import random

ListaLancamentos = []
QuantidadesNumeros1 = 0
QuantidadesNumeros2 = 0
QuantidadesNumeros3 = 0
QuantidadesNumeros4 = 0
QuantidadesNumeros5 = 0
QuantidadesNumeros6 = 0

for i in range(100):
    GeradorDeNumeros = random.randint(1, 6)
    ListaLancamentos.append(GeradorDeNumeros)


for J in ListaLancamentos:
    if J == 1:
            QuantidadesNumeros1 += 1
    if J == 2:
            QuantidadesNumeros2 += 1
    if J == 3:
            QuantidadesNumeros3 += 1
    if J == 4:
            QuantidadesNumeros4 += 1
    if J == 5:
            QuantidadesNumeros5 += 1
    if J == 6:
            QuantidadesNumeros6 += 1

print(ListaLancamentos)
print(f"o numero 1 aparece {QuantidadesNumeros1} vezes")
print(f"o numero 2 aparece {QuantidadesNumeros2} vezes")
print(f"o numero 3 aparece {QuantidadesNumeros3} vezes")
print(f"o numero 4 aparece {QuantidadesNumeros4} vezes")
print(f"o numero 5 aparece {QuantidadesNumeros5} vezes")
print(f"o numero 6 aparece {QuantidadesNumeros6} vezes")