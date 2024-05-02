while True:
    numero = int(input(f'Insira o numero que deseja verificar \n'))
    x = 0
    for i in range(1, numero+1):
        if numero % i == False:
            x +=1
    if x == 2:
        print('Numero Primo!!')
    else:
        print('not primo')
    continue
