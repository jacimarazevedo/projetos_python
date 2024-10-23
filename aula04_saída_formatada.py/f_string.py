import os

import datetime


# limpar o terminal
os.system('cls')

print('-'*70)
print('ENTRADA DE DADOS EM PYTHON')
print('=')

#Entrada
nome = input('Entre com um nome:')
peso = input('Entre com o peso:')
altura = input("Entre com a altura:")

# Entrada com Casting 
nascimento = int(input('Ano de nascimento: '))
cep = int(input('Entre com o seu CEP: '))
bairro = str(input('Entre com Bairro: '))
rua = str(input('Nome da rua: '))
numero = int(input('Entre com o numero: '))

# Processamento: Pegando o ano corrente

ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento 


# saída 
print('-'*70)
print('SAÍDA DE DADOS')
print('='*70)
print('Nome.............: ', nome)
print('Ano de nascimento: ', nascimento)
print('Peso.............: ', peso)
print('Altura..........: ', altura)

# saída interpolada 
print(f'{nome}, voce tem {idade} anos!')
print(f'CEP............:{cep}')
print(f'Bairro...........:{bairro}')
print(f'rua.............:{rua}')
print(f'Numero.............:{numero}')
print('-'*70)
print('')

