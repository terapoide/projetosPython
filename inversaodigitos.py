digitos = int(input('insira um numero de 4 digitos'))
stringado = str(digitos)
tamanho = len(stringado)
tabela = []
for i in range(tamanho-1, -1,-1):
    tabela.append(int(stringado[i]))
x = ''.join(map(str,tabela))
print(x)
C:\Users\logonrmlocal\PycharmProjects\pythonProject\temporizador decrescente.py
