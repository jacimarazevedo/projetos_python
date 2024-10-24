


import os



os.system('cls')

print('='*70)
print('CADASTRO DADOS')
print('='*70)

# Entrada com Casting 
usuario = str(input('usuário:'))
cpf = int(input('cpf:'))
nome = str(input('nome completo:'))
nome_mae = str(input('nome da mãe:'))

# Saída 
print(f'usuário{usuario}')
print(f'cpf{cpf}')
print(f'nome{nome}')
print(f'nome_mãe{nome_mae}')
print('-'*70)