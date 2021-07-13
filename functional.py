from functools import reduce

lista = [1,2,3,4,5]

soma = reduce(lambda x, y: x + y, lista)
fatorial = reduce(lambda x,y: x * y, lista)

print(f'Soma de {lista} = {soma}')
print(f'Fatorial de {lista} = {fatorial}')

numerosPares = [x for x in lista if x % 2 == 0]
print(f'Numeros pares na lista: {numerosPares}')

numImpares = list(filter(lambda x: x % 2 != 0, lista))
print(f'Numeros impares {numImpares}')

numMulti = list(map(lambda x: x * 2, lista))
print(f'Numeros {lista} em dobro {numMulti}')


idades = [7, 8, 8, 7]

novo = min(idades)
velho = max(idades)
media = sum(idades) / len(idades)
media2 = lambda x,y : x / y

print(novo)
print(velho)
print(media)
print(media2(reduce(lambda x,y : x + y, idades), len(idades)))
