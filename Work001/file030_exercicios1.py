"""
pasta 7 pdf 1





# 01

A = [1, 0, 5, -2, -5, 7]
print(A)

soma_especifica = A[0] + A[1] + A[5]
print(soma_especifica)

A[4] = 100
print('---------------')

for cada in A:
    print(cada)

print('---------------\n')

# 04

quantidade = 8
valores = []
x = 0
y = 0

for indice in range(8):
    cada = int(input(f'{indice + 1}º valor: '))
    valores.append(cada)

print(valores)

x = int(input('posicao indice x: '))
y = int(input('posicao indice y: '))

try:
    if 0 <= x or y <= 8:
        print(f'valores[x]: {valores[x]}, valores[y]: {valores[y]}')
        print(f'soma: {valores[x] + valores[y]}')
    else:
        print('pelo menos um indice está fora do intervalo')
except:
    print('pelo menos um indice está fora do intervalo')


#05

valores = []
pares = []

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)

for cada in valores:
    if cada % 2 == 0:
        pares.append(cada)

print(f'pares: {pares} || quantos: {len(pares)}')


# 07

print('digite 10 números inteiros: ')
valores = []

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(valores)
print(f'maior: {max(valores)}, seu indice: {valores.index(max(valores))}')

#08

valores = []

for indice in range(6):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

print(f'ordem inversa {valores[::-1]}')


#11
valores = []
contar_negativo = 0
soma_positivos = 0

for indice in range(10):
    valor = int(input(f'{indice+1}º valor: '))
    valores.append(valor)

for cada in valores:
    if cada < 0:
        contar_negativo += 1
    else:
        soma_positivos += cada

print(f'quantidade de negativos: {contar_negativo}')
print(f'soma dos positivos: {soma_positivos}')





"""





#14












