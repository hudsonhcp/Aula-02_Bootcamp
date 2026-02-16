#%%
# 1) Solicita ao usuário que digite seu nome
try:
    nome = input('Digite seu nome: ')
    if nome.isdigit():
        print('Você digitou seu nome errado.')
    if nome.isspace():
        print('Você digitou somente espaço.')
    if len(nome) == 0:
        print('Você não digitou nada.')
    else:
        print(f'Olá, {nome}! Seu nome foi computado.')
except:
    print('Erro: Entrada inválida para o nome.')
#%%
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario = input('Digite o valor do seu salário: ')
    salario = float(salario)
except ValueError:
    print('Você digitou um valor inválido para o salário.')
    exit()
else:
    print('Entrada do salário processada com sucesso.')

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante


try:
    bonus = input('Digite o valor do bônus recebido (%): ')
    bonus = float(bonus)/100
except ValueError:
    print('Você digitou um valor inválido para o bônus.')
    exit()
else:
    print('Entrada do bônus processada com sucesso.')

# 4) Calcule o valor do bônus final

CONSTANTE = 1000

kpi_bonus = CONSTANTE + salario * bonus

# 5) Imprima cálculo do KPI para o usuário

print(f'{nome}, seu KPI Bônus é de R$ {kpi_bonus:.2f}.')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?