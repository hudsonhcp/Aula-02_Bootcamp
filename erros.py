#%%
try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    divisao = num1 / num2
    print(f'A divisão de {num1} por {num2} é igual a {divisao}.')
except: ## Captura qualquer tipo de erro, porém o mais adequado é capturar o erro específico, como ValueError ou ZeroDivisionError.
    print('Erro: Digite valores válidos.')
else: ## Se o try for executado sem erros, o bloco else é executado. Se ocorrer um erro, o bloco else é ignorado. O bloco else é opcional e pode ser omitido se não for necessário. Ele é útil para executar código que deve ser executado apenas quando o try for bem-sucedido, como imprimir uma mensagem de sucesso ou realizar ações adicionais.
    print('Divisão realizada com sucesso.')
finally: ## O bloco finally é sempre executado, independentemente de ocorrer um erro ou não. Ele é útil para garantir que certas ações sejam realizadas, como fechar arquivos, liberar recursos ou imprimir mensagens de encerramento. O bloco finally é opcional e pode ser omitido se não for necessário.
    print('Fim do programa.')

#%%
numero = int(input('Digite um número: '))

if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")

#%%
# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print(f'A temperatura em Fahrenheit é {fahrenheit:.2f}.')
except ValueError:
    print('Erro: Valor digitado não é numérico.')
else:
    print('Conversão realizada com sucesso.')
finally:
    print('Fim do programa.'),

#%%
#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

try:
    valor = input('Digite uma palavra ou frase: ')
    if isinstance(valor, str):
        valor_junto = valor.replace(" ", "").lower()
        if valor_junto == valor_junto[-1::-1]:
            print('A palavra ou frase é um palíndromo.')
        else:
            print('A palavra ou frase não é um palíndromo.')
except:
    print('Erro: Valor digitado não é uma string.')
else:
    print('Verificação realizada com sucesso.')
#%%
# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    operacao = input('Digite a operação (+, -, *, /): ')
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    else:
        print('Operação inválida.')
        resultado = None
except ZeroDivisionError:
    print('Divisão por zero não é permitida.')
except ValueError:
    print('Pelo menos uma das entradas não é numérica.')
else:
    if resultado is not None:
        print(f'O resultado de {num1} {operacao} {num2} é igual a {resultado:.2f}.')
finally:
    print('Fim do programa.')



#%%
# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

#%%
# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.