# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''vetor = []
for x in range(5):
    vetor.append(int(input('Digite o proximo numero: ')))
print([x for x in vetor])
'''
# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''vetor2 = []
for x in range(10):
    vetor2.append(float(input('Digite o proximo numero real: ')))
print(vetor2[::-1])
'''
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''from functools import reduce
notas = []
for i in range(4):
    notas.append(float(input('Digite a nota: ')))

notas = reduce(lambda x,y: x + y, notas) / len(notas)
print(f'Media: {notas}')
'''
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''caracteres = []
for i in range(10):
    caracteres.append(input('Digite um caracter: '))
consoantes = [x for x in caracteres if x not in('aeiou')]
print(f'Total de {len(consoantes)} consoantes = {consoantes} na lista {caracteres}')
'''
# Faça um Programa que leia 5 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''numeros = []
for x in range(5):
    numeros.append(int(input('Digite o proximo numero: ')))
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print(f'Numeros: {numeros}\nPares: {pares}\nImpares: {impares}')
'''
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
'''from functools import reduce

notas = []
medias = []
for i in range(2):
    notas.append([])
    for j in range(4):
        notas[i].append(float(input(f'Digite a nota {j + 1} do aluno {i + 1}: ')))

for aluno in notas:
    medias.append(reduce(lambda x,y: x+y, aluno))

aprovados = [media for media in medias if media / 4 >= 7]
print(f'Total de alunos com média acima ou igual a 7.0: {len(aprovados)}')
'''
# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''from functools import reduce

vetor = [1,2,3,4,5]
soma = reduce(lambda x, y : x + y, vetor)
multi = reduce(lambda x, y : x * y, vetor)
print(f'Soma: {soma} - Multiplicacao: {multi} - Numeros: {vetor}')
'''
# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação. Imprima a idade e a altura na ordem inversa a ordem lida.
'''dados = []
for i in range(2):
    dados.append([])
    for j in range(2):
        dados[i].append([])
        if j % 2 == 0:
            dados[i][j].append(input('Nome: '))
        else:
            dados[i][j].append(input('Idade: '))
print(dados[::-1])
'''