
import random
import time

# Constantes
MAX_NUM = 10

def esperar(segundos):
    time.sleep(segundos)

def iniciar_jogo():
    input('Digite enter para iniciar o programa ')
    esperar(1)
    print('Iniciando...')
    esperar(2)
    print('.....')
    esperar(2)
    print('Bem-vindo ao jogo de adivinhação')
    esperar(2)

def adivinhar_numero():
    acertou = False
    tentativas = 0
    sorteio = random.randint(0, MAX_NUM)
    print(f'Foi gerado automaticamente um número de 0 a {MAX_NUM}')

    while not acertou:
        try:
            esperar(2)
            tentativas += 1
            numero = int(input(f'Digite um número de 0 a {MAX_NUM}: '))
            if numero == sorteio:
                print('Acertou')
                acertou = True
            elif numero < sorteio:
                esperar(1)
                print('Digite um número maior')
            else:
                esperar(1)
                print('Digite um número menor')
        except ValueError:
            print('Por favor, digite um número válido')

    print(f"Parabéns! Você acertou o número {sorteio} em {tentativas} tentativas.")

import random
import time

# Constantes
MAX_NUM = 10

def esperar(segundos):
    time.sleep(segundos)

def iniciar_jogo():
    input('Digite enter para iniciar o programa ')
    esperar(1)
    print('Iniciando...')
    esperar(2)
    print('.....')
    esperar(2)
    print('Bem-vindo ao jogo de adivinhação')
    esperar(2)

def adivinhar_numero():
    acertou = False
    tentativas = 0
    sorteio = random.randint(0, MAX_NUM)
    print(f'Foi gerado automaticamente um número de 0 a {MAX_NUM}')

    while not acertou:
        try:
            esperar(2)
            tentativas += 1
            numero = int(input(f'Digite um número de 0 a {MAX_NUM}: '))
            if numero == sorteio:
                print('Acertou')
                acertou = True
            elif numero < sorteio:
                esperar(1)
                print('Digite um número maior')
            else:
                esperar(1)
                print('Digite um número menor')
        except ValueError:
            print('Por favor, digite um número válido')

    print(f"Parabéns! Você acertou o número {sorteio} em {tentativas} tentativas.")


def escolha():
    while True:
        iniciar_jogo()
        adivinhar_numero()  
        desicao = input('Deseja continuar o jogo? Digite (sim) para continuar ou digite (nao) para encerrar  ').lower()
        if desicao == 'nao':
            print('OBRIGADO POR JOGAR, ATÉ A PROXIMA.')
            break

if __name__ == "__main__":    
    escolha()








