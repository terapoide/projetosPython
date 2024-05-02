while True:
    contador = 0
    obj = int(input('Insira o numero Inteiro positivo\n'))
    for i in range(1, obj):
        if i % 2 == 0:
            contador += i
    print(contador)
    continue
