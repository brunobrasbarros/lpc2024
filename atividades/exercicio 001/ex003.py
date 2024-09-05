PrimeiraParte = input("insira os 3 primeiros digitos do cpf: ")
SegundaParte = input("insira mais 3 digitos: ")
TerceiraParte = input("insira mais 3 digitos: ")
QuartaParte = input("insira os ultimos 2 digitos: ")

CpfCompleto = PrimeiraParte+"."+SegundaParte+"."+TerceiraParte+"-"+QuartaParte


for digito in CpfCompleto:
    digito  # type: ignore

if len(CpfCompleto) != 14:
        print("CPF INVALIDO POR QUANTIDADE DE CARACTERES")

if digito.isdigit() == True:
        print("letras são inválidas na verificação de Cpf")

if len(CpfCompleto) == 14 and digito.isdigit == False:
    print(f"o Cpf ficou {PrimeiraParte}.{SegundaParte}.{TerceiraParte}-"
          f"{QuartaParte}")