import time
from data import *
from pessoa import *
from financa import *
from gastos import *

# missão 1

# parte feita pela aluna: Mariana Oliveira Lima

yellow = '\033[93m'
blue = '\033[94m'
verde = '\033[32m'
reset = '\033[0m'
whtblue = '\033[96m'

print(f'Oi, pode me chamar de {blue}Din{reset}!')
print('Sou um assistente financeiro')
print(f'e vou tentar te ajudar com as {whtblue}contas{reset} e os {reset}{whtblue}objetivos{reset}.')
print('')
print('[DADOS PESSOAIS]')
print('')
print('Primeiro, preciso de algumas informações')
seu_nome = input (f'Me diz teu {reset}{yellow}nome{reset}: ')
dia_nasceu = int(input(f'O {reset}{yellow}dia{reset} em que tu nasceu: '))
mes_nasceu = int(input(f'Agora o {reset}{yellow}mês{reset}: '))
ano_nasceu = int(input(f'E o {reset}{yellow}ano{reset}: '))
print('')
print('---')
print('')
print('Muito bem, então conferindo os seus dados, estou registrando aqui.')
print(f'{reset}{verde}{seu_nome}{reset}, nascimento em {reset}{verde}{dia_nasceu}/{mes_nasceu}/{ano_nasceu}{reset}')
print('')
print('[DADOS FINANCEIROS]')
print('')
print('Agora me informa por favor alguns dados financeiros')
patrimonio_total = float(input(f'Se você somar o dinheiro que tem guardado, me diz o total desse {reset}{yellow}patrimônio{reset}: R$ '))
salario_bruto = float(input(f'Me diz teu {reset}{yellow}salário{reset}: R$ '))
print('Sobre os seus gastos, me informa por partes por favor.')
G_aluguel = float(input(f'Quanto custa teu {reset}{yellow}aluguel{reset}, (incluindo condomínio e outras taxas): R$ '))
G_feira = float(input(f'Mais ou menos o quanto você gasta fazendo {reset}{yellow}feira{reset} todo o mêS: R$ '))
G_comida = float(input(f'E a {reset}{yellow}comida{reset} fora de casa, em média dá quanto: R$ '))
G_transporte = float(input(f'Na mobilidade, quanto que gasta com {reset}{yellow}transporte{reset}(ônibus, uber, gasolina, etc): R$ '))
G_outros = float(input(f'Pra terminar, quanto você gasta com {reset}{yellow}outros{reset}(lazer, roupas, etc): R$ '))
gastos_totais = G_aluguel + G_feira + G_comida + G_transporte +G_outros
print('')
print('---')
print('')
print(f'Obrigado {reset}{verde}{seu_nome}{reset}, resumindo as informações financeiras até agora.')
print('Os seus gastos discriminados são:')
print(f'{reset}{verde}Aluguel{reset}: R$ {G_aluguel:.2f}')
print(f'{reset}{verde}Feira{reset}: R$ {G_feira:.2f}')
print(f'{reset}{verde}Comida{reset}: R$ {G_comida:.2f}')
print(f'{reset}{verde}Transporte{reset}: R$ {G_transporte:.2f}')
print(f'{reset}{verde}Outros{reset}: R$ {G_outros:.2f}')
print(f'{reset}{verde}GASTOS TOTAIS{reset}: R$ {gastos_totais:.2f}')
print('')
print('---')
print('')
saldo_mensal = salario_bruto - gastos_totais
print('Pra terminar, calculando o seu saldo mensal, com base em todos os gastos')
print(f'e no teu salário, o valor resultante é de {reset}{verde}{saldo_mensal:.2f}{reset}')
print('Desse valor, considerando que qualquer investimento é valido,')
investimento_D = float(input(f'o quanto você conseguiria {reset}{yellow}investir{reset} todo mês: R$ '))
print(f'Ok, anotado, o valor do investimento mensal é {reset}{verde}R$ {investimento_D:.2f}{reset}')
print('Acredito que coletei todas as informações necessárias')

# missão 2 

# parte feita pela aluna: Mariana Oliveira Lima, e  aluno: João Lucas Cosme

nascimento = Data(dia_nasceu, mes_nasceu, ano_nasceu)
gastos = Gastos(G_aluguel, G_feira, G_comida, G_transporte, G_outros)
financa = Financa(patrimonio_total, salario_bruto, gastos, investimento_D)
antonieta = Pessoa(seu_nome, nascimento, financa)
gastos_totais2 = (
    antonieta.financa.gastos.aluguel +
    antonieta.financa.gastos.feira +
    antonieta.financa.gastos.comida +
    antonieta.financa.gastos.transporte +
    antonieta.financa.gastos.outros
)
print(f'\n---\n')

print(f'Agora organizei todos os seus dados de forma concentrada aqui no meu sistema')
print(f'Vou te mostra como ficou:')
print(f'{antonieta.nome}, nascimento em {antonieta.nascimento.dia}/{antonieta.nascimento.mes}/{antonieta.nascimento.ano}')
print(f'{antonieta.nome} tem {antonieta.financa.patrimonio} de patrimônio')
print(f'{antonieta.nome} tem {antonieta.financa.salario} de salário')
print(f'{antonieta.nome} tem {gastos_totais2} de gastos')
print(f'{antonieta.nome} tem {antonieta.financa.investimentos} de investimento')

# missão 3

# parte feita pelo aluno: João Lucas Cosme 

print('')
print('---')
print('')
print('Agora sim, vamos pensar no futuro! Você tem um próximo objetivo financeiro?')
print('Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?')
print('Exemplos de objetivos assim são:')
print('Comprar uma moto ou um carro, fazer uma viagem, comprar uma casa, fazer um curso, etc.')
objetivo_financeiro = input(f'Qual seria esse seu próximo {reset}{yellow}objetivo{reset} financeiro: ')
valor_objeto = float(input(f'Qual o valor do {reset}{yellow}objetivo{reset} financeiro: R$ '))
print('Em uma conta simples que fiz aqui, sem considerar rendimentos ou inflação,')
print(f'com base na sua capacidade de investimento mensal de {reset}{verde}R$ {investimento_D:.2f}{reset}')
print(f'e o seu patrimônio atual de {reset}{verde}R$ {patrimonio_total:.2f}{reset}')
print(f'Você conseguiria atingir o valor de {reset}{verde}R$ {valor_objeto:.2f}{reset} em:')
valor_atingido = (valor_objeto - patrimonio_total) / investimento_D
print(f'{valor_atingido:.2f} meses')
valor_anos = valor_atingido / 12
print(f'Ou {valor_anos} anos')
print('Por hora, é isso que tenho para te ajudar')
print('Espero que tenha sido útil')
