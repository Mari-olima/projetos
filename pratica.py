# Parte 1: Tuplas
# 1.1 Crie uma tupla para armazenar os códigos de cor RGB (Vermelho, Verde, Azul), usando os valores 255 para vermelho, 102 para verde e 0 para azul.

cor = (255, 102, 0)

# 1.2 Crie uma tupla para as coordenadas geográficas, usando -8.0578 para latitude e -34.8829 para longitude.

coordenada = (-8.0578, -34.8829)

# 1.3 Crie uma tupla para armazenar as informações básicas e imutáveis de um usuário, contendo o ID 101, o username 'ana_silva' e a data de criação '2023-01-15'.

informaçao_basica = (101, 'ana_silva', '2023-01-15')

# 1.4 Dada a tupla de cores RGB (255, 102, 0), acesse e imprima o valor do componente 'Verde' (o segundo elemento, de índice 1).

print(cor[1])

# 1.5 Dada a tupla de coordenadas (-8.0578, -34.8829), desempacote-a em duas variáveis separadas chamadas latitude e longitude.

#pode ser feito assim tambem:
latitude, longitude = coordenada

latitude = coordenada[0]
longitude = coordenada[1]

print(latitude)
print(longitude)

# 1.6 A partir da tupla de usuário (205, 'Carlos Pereira', 'carlos.p@email.com'), que representa (id, nome, email), desempacote-a em variáveis e use a variável do nome para imprimir uma saudação.

usuario_6 = (205, 'Carlos Pereira', 'carlos.p@email.com')

#pode ser feito dos dois jeitos porem o prof prefere da primeira forma 

ID, nome, email = usuario_6 

ID = 205
nome = 'Carlos Pereira'
email = 'carlos.p@email.com'

print(f'Saudações {nome}.')

# 1.7 Dada a tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'), itere sobre ela e imprima cada papel.

administrador = ('moderador', 'editor', 'sysadmin')

for papel in administrador:
    print(papel)

# 1.8 Dada a tupla dados dos usuários acima, itere sobre elas e imprima cada dado.

for dado in usuario_6:
    print(dado)

# 1.9 Dada a tupla de cores RGB acima, itere sobre ela e imprima cada parte da cor, R, G e B.

for componente in cor:
    print(componente)

# 1.10 Escreva uma função que verifique se um papel de usuário existe em uma tupla de papéis de administrador ('moderador', 'editor', 'sysadmin'). Teste a função com os papéis 'editor' e 'usuario_comum'.

def existe (papel):
    sim_ou_nao = False
    administrador = ('moderador', 'editor', 'sysadmin')
    for resposta in administrador:
        if papel == resposta:
            sim_ou_nao = True

    return sim_ou_nao
print(f' editor é adiministrador? {existe("editor")}')
print(f'usuario é adiministrador? {existe ("usuario")}')

# 1.11 Dada a tupla de atribuições das pessoas de um equipe ('editor', 'leitor', 'editor', 'comentarista', 'editor'), escreva uma função que conta o número de vezes em que um papel aparece, teste a função com os papíes 'editor', 'comentarista' e 'tradutor'.

def contar (papel):
    equipe = ('editor', 'leitor', 'editor', 'comentarista', 'editor')
    for algo in equipe:
        if papel == algo:
            quanto = equipe.count(algo)
        else:
            quanto = False

    return quanto

print(f'tradutor aparece na equipe? se sim quantas vezes? {contar("tradutor")}')
print(f'editor aparece na equipe? se sim quantas vezes? {contar("editor")}')
print(f'comentarista aparece na equipe? se sim quantas vezes? {contar("comentarista")}')

# Parte 2: Dicionários
# 2.1 Crie um dicionário para um usuário. Use a chave 'username' para o valor 'bia_costa', a chave 'email' para 'bia.costa@email.com', e a chave 'data_adesao' para '2024-05-21'.

usuario_5 = { 'username': 'bia_costa','email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}

# 2.3 Crie um dicionário vazio chamado preferencias_usuario.

preferencias_usuario = {}

# 2.4 Dado o dicionário de produto {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}, acesse e imprima o preço original. Em seguida, atualize o preço para o valor promocional de 249.99.

produto = {'id_produto': 'XYZ-001', 'nome': 'Fone de Ouvido Sem Fio', 'preco': 299.90, 'estoque': 150}

print(f'Preço original: R${produto["preco"]}')
produto["preco"] = 249.99
print(f'Preço promocional: R${produto["preco"]}')

# 2.5 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}, adicione uma nova informação: a chave 'telefone' com o valor '98765-4321'.

usuario_4 = {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'data_adesao': '2024-05-21'}

usuario_4["telefone"] = '98765-4321'

# 2.6 Dado o perfil de usuário {'username': 'bia_costa'}, use o método .get() para tentar acessar o valor da chave 'ultimo_login'. Como a chave não existe, forneça o valor padrão 'Nunca logou'. Após a tentativa, bia fez o login, então atualize o dicionário para incluir a chave 'ultimo_login' com o valor '2024-05-22'.

usuario = {'username': 'bia_costa'}
ultimo_login = usuario.get('ultimo_login', 'Nunca logou')
print(ultimo_login)
usuario['ultimo_login'] = '2024-05-22'

# 2.7 Dado o perfil de usuário {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}, use a instrução del ou a função pop() para remover a chave 'telefone_fixo'.

usuario_3 = {'username': 'bia_costa', 'email': 'bia.costa@email.com', 'telefone_fixo': '3265-4321'}
del usuario_3['telefone_fixo']
# ou...
# usuario_3.pop("telefone_fixo")

# 2.8 Dado o catálogo de produtos {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}, use a instrução o método .pop() para remover o produto com a chave 'XYZ-001'. Armazene o valor retornado (o nome do produto) e imprima uma mensagem de confirmação.

produtos = {'XYZ-001': 'Fone de Ouvido Sem Fio', 'ABC-002': 'Teclado Mecânico'}
remover = produtos.pop("XYZ-001")
print(f"Produto removido: {remover}")

# 2.9 Dado o perfil de usuário {'username': 'bia_costa'}, tente remover a chave 'email' usando o método .pop(). Forneça o valor padrão 'Email não encontrado.' para evitar um erro.

usuario_2 = {'username': 'bia_costa'}
email_R = usuario_2.pop("email", "Email não encontrado.")
print(email_R)

# 2.10 Dado o catálogo de produtos {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço'.

produtos_1 = {'Fone de Ouvido': 249.99, 'Teclado Mecânico': 450.00, 'Mouse Gamer': 120.50}
for nome, preco in produtos_1.items():
    print(f"{nome}: R${preco}")

# 2.11 Dado a lista de compras da feira {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}, itere sobre seus itens e imprima o nome e o preço de cada um no formato 'Nome: R$Preço' e depois imprima o total.

feira = {'Tapioca': 18.99, 'Queijo Manteiga': 45.00, 'Ovos': 23.50}
total = 0
for item, preco in feira.items():
    print(f"{item}: R${preco}")
    total += preco
print(f"Total: R${total}")

# 2.12 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'endereco'. O valor associado a essa chave deve ser outro dicionário contendo: 'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo' e 'cep': '01000-000'.

usuario_7 = {'username': 'bia_costa'}
usuario_7["endereco"] = {'rua': 'Rua das Flores, 123', 'cidade': 'São Paulo', 'cep': '01000-000'}

# 2.13 Dado o perfil de usuário {'username': 'bia_costa'}, adicione uma nova chave 'profissao'. O valor associado a essa chave deve ser outro dicionário contendo: 'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'.

usuario_7["profissao"] = {'cargo': 'Desenvolvedora', 'empresa': 'Tech Solutions'}

# 2.14 A partir do perfil de usuário com endereço e profissão aninhados da questão anterior, acesse e imprima apenas o valor associado à chave 'cidade'.

print(usuario_7["endereco"]["cidade"])

# 2.15 Dado o perfil de usuário com endereço aninhado, atualize o valor da chave 'rua' para 'Avenida Principal, 456'.

usuario_7['endereco']["rua"] = "Avenida Principal, 456"

# 2.16 Crie um dicionário para mapear coordenadas para nomes de locais. Use a tupla (-8.0578, -34.8829) como chave para o valor 'Recife' e a tupla (-23.5505, -46.6333) como chave para o valor 'São Paulo'.

locais = {(8.0578, -34.8829): "Recife", (-23.5505, -46.6333): "São Paulo"}

# 2.17 A partir do dicionário da questão anterior, adicione um novo local. A chave deve ser a tupla (-22.9068, -43.1729) e o valor deve ser 'Rio de Janeiro'.

locais[(-22.9068, -43.1729)] = "Rio de Janeiro"

# 2.18 Escreva uma função que, dado um dicionário de locais, encontre o nome do local a partir de uma tupla de coordenadas. A função deve retornar uma mensagem padrão caso a coordenada não seja encontrada. Teste a função com as coordenadas (-23.5505, -46.6333) e (0, 0).

def google_maps(dicionario, coordenada):
    return dicionario.get (coordenada, "Local não encontrado.")

print(google_maps(locais, (-23.5505, -46.6333)))
print(google_maps(locais, (0, 0)))

# Parte 3: Vetores (Listas e NumPy)
# 3.1 Crie uma lista de hashtags (#) para redes sociais chamada tags_post com os valores ['#tecnologia', '#python', '#programacao']. Em seguida, adicione a tag '#dados' ao final da lista.

lista_hastag = ['#tecnologia', '#python', '#programacao']
lista_hastag.append("#dados")

# 3.2 Dada a lista de tags ['#tecnologia', '#python', '#programacao', '#dados'], remova o elemento '#programacao'.

lista_hastag = ['#tecnologia', '#python', '#programacao', '#dados']
lista_hastag.remove("#programacao")

# 3.3 Dada a lista de tags ['#tecnologia', '#python', '#dados'], verifique se a string '#importante' existe na lista.

lista_hastag = ['#tecnologia', '#python', '#dados']
existe_ou_nao = "#importante"
if existe_ou_nao in lista_hastag:
    print(f"O item {existe_ou_nao} está na lista.")
else:
    print(f"O item {existe_ou_nao} não está na lista.")

# 3.4 Importe a biblioteca numpy com o alias np. Crie um array NumPy a partir da lista de itens vendidos da semana, em que os itens são tuplas representando (produto, quantidade): [('camiseta', 10), ('calça', 5), ('sapato', 2)].

import numpy as np

vendido = [('camiseta', 10), ('calça', 5), ('sapato', 2)]
array_vendido = np.array(vendido, dtype=object)

# 3.5 Crie um array NumPy para armazenar as seguintes pontuações de um aluno: [0.85, 0.92, 0.78, 0.95, 0.88].

pontuacoes = np.array([0.85, 0.92, 0.78, 0.95, 0.88])

# 3.6 Crie um array NumPy para armazenar as temperaturas em Celsius: [45.5, 46.0, 45.8, 47.1, 46.5].

temp_celsius = [45.5, 46.0, 45.8, 47.1, 46.5]

# 3.7 Dado o array NumPy com tuplas de itens e preços precos = np.array([(Sapato, 100.0), (Calça, 250.0), (Camiseta, 80.0), (Tênis, 150.0)]), crie um novo array aplicando um desconto de 10% a todos os elementos (multiplicando por 0.9).

precos = np.array([('Sapato', 100.0), ('Calça', 250.0), ('Camiseta', 80.0), ('Tênis', 150.0)], dtype=object)
desconto = [(item, preco * 0.9) for item, preco in precos]

# 3.8 Modifique o desconto aplicado acima para ser de 15% e imprima todos os valores originais e com desconto no formato, o <item> custava <preco_original>, agora custa <preco_com_desconto>.

for item, preco in precos:
    preco_com_desconto = preco * 0.85
    print(f"O {item} custava {preco}, agora custa {preco_com_desconto:.2f}")

# 3.9 Dados o array de quantidades quantidades = np.array([1, 2, 3]) e o array de preços unitários precos_unitarios = np.array([15.0, 30.0, 22.5]), calcule o valor total por item multiplicando os dois arrays.

quantidades = np.array([1, 2, 3])
precos_unitarios = np.array([15.0, 30.0, 22.5])
total_por_item = quantidades * precos_unitarios

# 3.10 Dado o array de temperaturas em Celsius temperaturas_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5]), converta todas as temperaturas para Fahrenheit usando a fórmula F = C * 1.8 + 32.

temp_celsius = np.array([45.5, 46.0, 45.8, 47.1, 46.5])
F = temp_celsius * 1.8 + 32

# Parte 4: Matrizes (NumPy)
# 4.1 Crie e imprima uma matriz NumPy 3x4 (3 meses, 4 produtos) para representar as vendas com os dados: 
# [0, 1, 3]
# [9, 7, 4]
# [2, 6, 6]
# [3, 3, 3].

matriz = np.array([
    [0, 1, 3],
    [9, 7, 4],
    [2, 6, 6],
    [3, 3, 3]
])

# 4.2 Usando a matriz de vendas da questão anterior, imprima seu formato (atributo .shape) e sua transposta (atributo .T).

print(matriz.shape)
print(matriz.T)

# 4.3 Crie uma matriz NumPy 3x3 preenchida com zeros, com tipo de dado inteiro (dtype=int).

zeros = np.zeros((3, 3), dtype=int)

# 4.4 Dada a matriz de vendas da questão 4.1, extraia e imprima a linha completa de dados para o segundo produto (linha de índice 1).

print(matriz[1])

# 4.5 Usando a mesma matriz de vendas, extraia e imprima a coluna completa de dados para o terceiro mês (coluna de índice 2).

print(matriz[:, 2])

# 4.6 Ainda com a matriz de vendas, acesse e imprima o valor específico do produto 3 (linha 2) no mês 2 (coluna 1).

print(matriz[2][1])

# 4.7 Dada a matriz de preços matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]]), crie uma nova matriz com todos os preços aumentados em 5%.

matriz_precos = np.array([[10.00, 12.50], [25.00, 28.00]])
matriz_precos_aumento = matriz_precos * 1.05

# 4.8 Dadas as matrizes de vendas com a quantidade de vendas de 4 produtos nos primeiros 3 meses do ano, vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]]) e vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]]), some-as para criar uma matriz vendas_globais.

vendas_eua = np.array([[100, 150, 200], [80, 120, 160], [90, 110, 130], [70, 100, 140]])
vendas_europa = np.array([[90, 140, 190], [70, 110, 150], [80, 100, 120], [60, 90, 130]])
vendas_globais = vendas_eua + vendas_europa

# 4.9 Dada a matriz de vendas vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]]) (3 produtos x 2 meses) e o vetor de preços precos = np.array([4.99, 5.25, 2.19]), calcule a receita total por mês usando o produto escalar (np.dot).

vendas_unidades = np.array([[100, 150], [80, 120], [90, 110]])  # 3 produtos x 2 meses
precos = np.array([4.99, 5.25, 2.19])  # 3 produtos
receita_mensal = np.dot(precos, vendas_unidades)

# 4.10 Usando a matriz de vendas da questão 4.1, calcule o total de unidades vendidas em cada mês (soma ao longo do eixo 0).

total_mes = matriz.sum(axis=0)

# 4.11 Usando a mesma matriz de vendas, calcule a média de vendas para cada produto (média ao longo do eixo 1).

media = matriz.mean(axis=1)

# 4.12 A partir da matriz de vendas, encontre e imprima o valor máximo.

valor_max = matriz.max()

# Parte 5: Desafios Finais
# Crie uma lista chamada usuarios contendo um dicionário para um usuário. Este dicionário deve ter: a chave 'id_usuario' com valor 101; a chave 'perfil' com um dicionário aninhado {'nome': 'Ana Silva', 'email': 'ana.s@email.com'}; a chave 'permissoes' com a tupla ('leitura', 'escrita'); e a chave 'mapa_calor_logins' com uma matriz NumPy de 7x24 preenchida com zeros. Implemente uma função registrar_login(usuario) que incremente o contador no mapa de calor do usuário correspondente ao dia e hora atuais.

# Escreva uma função analisar_inventario(catalogo) que processe um dicionário de produtos. A função deve retornar uma tupla contendo: 1. O valor total do inventário (soma de preco * estoque), 2. O nome do produto mais caro, e 3. Uma lista de produtos sem estoque. Teste a função com o catálogo: {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': {'preco': 250.00, 'estoque': 0}}.

catalogo = {'Laptop Gamer': {'preco': 7500.00, 'estoque': 10}, 'Mouse Vertical': {'preco': 350.00, 'estoque': 50}, 'Monitor 4K': {'preco': 4200.00, 'estoque': 15}, 'Webcam HD': {'preco': 250.00, 'estoque': 0}}

def analisar_inventario(catalogo):
    total = 0
    mais_caro = ''
    maior_preco = 0
    sem_estoque = []

    for produto, dados in catalogo.items():
        preco = dados['preco']
        estoque = dados['estoque']
        total += preco * estoque

        if preco > maior_preco:
            maior_preco = preco
            mais_caro = produto

        if estoque == 0:
            sem_estoque.append(produto)

    return total, mais_caro, sem_estoque

print(analisar_inventario(catalogo))

# Projete uma classe SocialGraph para gerenciar amizades. O construtor deve inicializar um dicionário self.conexoes. Implemente os métodos adicionar_amizade(id1, id2) para criar uma amizade mútua e obter_amigos(id_usuario) para retornar a lista de amigos. Instancie a classe e adicione as seguintes amizades: (101, 205), (101, 308), (205, 400). Teste o método obter_amigos para os usuários 101, 205 e 999.

class SocialGraph:
    def __init__(self):
        self.conexoes = {}

    def adicionar_amizade(self, id1, id2):
        self.conexoes.setdefault(id1, []).append(id2)
        self.conexoes.setdefault(id2, []).append(id1)

    def obter_amigos(self, id_usuario):
        return self.conexoes.get(id_usuario, [])


grafo = SocialGraph()
grafo.adicionar_amizade(101, 205)
grafo.adicionar_amizade(101, 308)
grafo.adicionar_amizade(205, 400)

print(grafo.obter_amigos(101))  
print(grafo.obter_amigos(205))  
print(grafo.obter_amigos(999))  
