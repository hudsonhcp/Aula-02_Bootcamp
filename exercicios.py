#%%
## Divisão
print(5 / 4)

#%%
## Divisão Inteira
print(5 // 4)

#%%
## Resto da Divisão
print(5 % 4)

#%%
nome_aluno = "Hudson"

print(type(nome_aluno))

print(type("Hudson"))

#%%
## Exercícios Inteiros (int)
#%%
# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num1 = int(input('Digite um número: '))

num2 = int(input('Digite outro número: '))

soma = num1 + num2

print(f'A soma de {num1} e {num2} é igual a {soma}.')

#%%
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

num = int(input('Digite um número: '))

resto_divisao = num % 5

print(f'O resto da divisão de {num} por 5 é igual a {resto_divisao}.')

#%%
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

multiplicacao = num1 * num2

print(f'A multiplicação de {num1} por {num2} é igual a {multiplicacao}.')

#%%
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

divisao_inteira = num1 // num2

print(f'A divisão inteira de {num1} por {num2} é igual a {divisao_inteira}.')

#%%
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

num = int(input('Digite um número: '))
quadrado = pow(num, 2)

print(f'O quadrado de {num} é igual a {quadrado}.')

#%%
##Números de Ponto Flutuante (float)
# 1. Escreva um programa que receba dois números flutuantes e realize sua adição.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
soma = num1 + num2

print(f'A soma de {num1} e {num2} é igual a {soma:.2f}.')

#%%
# 2. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

media = (num1 + num2) / 2

print(f'A média de {num1} e {num2} é igual a {media:.2f}.')

#%%
# 3. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))

potencia = pow(base, expoente)

print(f'{base} elevado a {expoente} é igual a {potencia:.2f}.')

#%%
# 4. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))

fahrenheit = (celsius * 9/5) + 32

print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}.')

#%%
# 5. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math

num_pi = math.pi

raio = float(input('Digite o raio do círculo: '))

area_circulo = num_pi * (pow(raio, 2))

print(f'A área do círculo com raio {raio} é igual a {area_circulo:.2f}.')


#%%
## Strings (str)
# 1. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input('Digite uma frase: ')
texto_maiusculo = texto.upper()

print(f'A frase em maiúsculas é: {texto_maiusculo}')

#%%
# 2. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_completo = input('Digite seu nome completo: ')
nome_minusculo = nome_completo.lower()

print(f'Seu nome em minúsculas é: {nome_minusculo}')

#%%
# 3. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase = input('Digite uma frase: ')
frase_sem_espacos = frase.strip()

print(f'A frase sem espaços em branco é: {frase_sem_espacos}')

#%%
# 4. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

data = input('Digite uma data no formato dd/mm/aaaa: ')

dia, mes, ano = data.split('/')

print(f'Dia: {dia}\nMês: {mes}\nAno: {ano}')

#%%
# 5. Escreva um programa que concatene duas strings fornecidas pelo usuário.

nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')

nome_completo = nome + ' ' + sobrenome

print(f'Seu nome completo é: {nome_completo}')

#%%
## Booleanos (bool)
# 1. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expressao1 = input('Digite a primeira expressão booleana (True/False): ')
expressao2 = input('Digite a segunda expressão booleana (True/False): ')

print(f'O resultado da operação AND entre {expressao1} e {expressao2} é: {expressao1 and expressao2}.')

#%%
# 2. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

expressao1 = input('Digite a primeira expressão booleana (True/False): ')
expressao2 = input('Digite a segunda expressão booleana (True/False): ')

print(f'O resultado da operação OR entre {expressao1} e {expressao2} é: {expressao1 or expressao2}.')

#%%
# 3. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor_booleano = input('Digite um valor booleano (True/False): ')

if valor_booleano == 'True':
    valor_invertido = False
elif valor_booleano == 'False':
    valor_invertido = True

print(f'O valor invertido de {valor_booleano} é: {valor_invertido}.')

#%%
# 4. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(f'Os números {num1} e {num2} são iguais? {num1 == num2}.')

#%%
# 5. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print(f'Os números {num1} e {num2} são diferentes? {num1 != num2}.')
