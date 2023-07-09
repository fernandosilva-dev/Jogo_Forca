import os 
import random

nome = input("digite seu nome: ")
print (f'Olá seja bem vindo {nome} ! Vamos começar a jogar?')
input('\nPressione enter para começar')
os.system('cls')

lista_de_palavras = ['cachorro', 'javascript', 'python', 'uniasselvi', 'humanidade', 'refrigerante'] 
palavra_selecionada = random.choice(lista_de_palavras).upper()
tamanho_palavra = len(palavra_selecionada)
palavra_codificada = ['_']*tamanho_palavra 
quantidade_de_erros = 0

while '_' in palavra_codificada and quantidade_de_erros < 6:
    print(f'\nSua palavra possui {tamanho_palavra} letras!')
    print(f'Erros: {quantidade_de_erros} de 6!')
    for letra in palavra_codificada:
        print(letra, end = ' ')
    print()
    
    letra_escolhida = input('digite alguma letra: ').upper()
    acertou = False
    for i in range(len(palavra_selecionada)):
        if letra_escolhida == palavra_selecionada[i]:
            palavra_codificada [i] = letra_escolhida
            acertou = True
            
    if acertou == True:
        print('parabéns! Acertou. ')
        
    else:
        print('Errou, essa letra não existe na palavra! ')
        quantidade_de_erros = quantidade_de_erros + 1
        
        
if quantidade_de_erros == 6:
    print('voceê perdeu! ')
else: print('parabéns! você venceu')

print(f'A palavra era: {palavra_selecionada}')