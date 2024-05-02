import time
tempo = int(input('insira os minutos em numero inteiro'))
temposegundos = tempo*60
for i in range(temposegundos, 0,-1):
    time.sleep(1)
    seconds = i
    if seconds > 59:
        seconds= seconds - 60
    print(f'{i//60}:{seconds}')
    if i == 0:
        print('acabou')
