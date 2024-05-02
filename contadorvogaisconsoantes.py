vogais = 'aeiouAEIOU'

while True:
    frase = str(input('insira a frase \n'))
    tamanho = len(frase)
    vogal = 0
    consoante = 0
    for i in range(0, tamanho):
        x = frase[i]
        if x in vogais:
            print(f'{x} é uma vogal \n')
            vogal +=1
        elif x != ' ':
            print(f'{x} é uma consoante')
            consoante +=1
    print(f'vogais = {vogal}, consoantes = {consoante}')
    continue


