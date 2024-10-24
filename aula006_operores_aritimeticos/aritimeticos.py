# imports 
import os 

# Limpa o terminal
os.system('cls')

print('-'*70)
print(' OPERADORES ARITIMÉTICOS')
print('-'*70)


# Entrada de Dados
print('--- SOMA')
print('-'*70)
parcela_1 = float(input('Entre com a 1° parcela:'))
parcela_2 = float(input('Entre coma 2° parcela: '))

print()
print('--- SUBTRAÇÃO')
print('-'*70)
minuendo = float(input('Entre com o minuendo:'))
subtraendo = float(input('Entre com a subtraendo:'))

print()
print('--- PRODUTO')
print('-'*70)
multiplicando = float(input('Entre com o multiplicando:'))
multiplicador = float(input('Entr com o multiplicador:'))

print()
print('----DIVISÃO')
print('-'*70)
dividendo = float(input('Entre com o dividendo:'))
divisor = float(input('Entre com o divisor:'))

print()
print('--- RAIZ QUADRADA')
print('-'*70)
valor = float(input('Entre com o valor da raiz quadrada:'))


print()
print('--- RAIZ CUBICA')
print('-'*70)
valor2 = float(input('Entre com o valor da raiz cubica:'))


# Processamento
soma = parcela_1 + parcela_2
diferenca = minuendo - subtraendo
produto = multiplicando * multiplicador
quociente = dividendo / divisor
raiz_quadrada = valor **(1/2)
raiz_cubica = valor2 **(1/3)


# Saída 
print('='*70)
print('RESULTADOS')
print('-'*70)
print(f'A soma de {parcela_1} = {parcela_2} é:{soma}')
print(f'A subtração de {minuendo} - {subtraendo} é: {diferenca}')
print(f'A multiplicação de {multiplicando} * {multiplicador} é: {produto}')
print(f'A divisão de {dividendo} / {divisor} é: {quociente}')
print(f'A raiz quadrada de {valor} é: {raiz_quadrada}')
print(f'A raiz cubica de {valor2} é: {raiz_cubica}')


