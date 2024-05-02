numero = int(input('Insira um numero inteiro e eu somarei seus digitos'))
stringado = str(numero)
tamanho = len(str(numero))
tabela = []
for i in range(0,tamanho):
    tabela.append(int(stringado[i]))
print(sum(tabela))
