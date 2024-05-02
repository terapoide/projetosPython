import time
tempotriste = float(input('Insira o tempo em minutos (x.x)'))
tempofeliz = tempotriste*60
for i in range(0, int(tempofeliz)+1,1):

    time.sleep(1)
    seconds = i
    if seconds > 59:
        seconds= seconds - 60
    print(f'{i//60}:{seconds}')
    if i == tempofeliz:
        print('acabou')
