SentencaDoPalindromo = input("escreva algo para saber se é palindromo ou não:")

SentençaLimpa = ''.join(caracteres for caracteres 
                        in SentencaDoPalindromo.lower().strip() 
                        if caracteres.isalnum())

InversoSentenca = SentençaLimpa[::-1]

if SentençaLimpa == InversoSentenca:
    print("é palindromo")

elif SentençaLimpa != InversoSentenca:
    print("não é palindromo")