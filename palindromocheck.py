frase = input('insert palindromo').lower()
tamanho = len(frase)
fake = []
x = -1
for i in range(0,tamanho):
    fake.append(frase[i])
for i in range(tamanho-1,-1,-1):


    x += 1
    print(frase[i], fake[x])
    if frase[i] == fake[x]:
        z = True

    else:
        print('Não é um palindromo')
        z = False
        break
if z == True:
    print('é um palindromo')

