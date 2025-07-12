# ==================================================
# BLOCO 1: ARQUIVOS TXT (15 exercícios)
# ==================================================

# --- Introdução ---
# Para arquivos TXT, usamos funções nativas do Python: open(), read(), write(), close()

# Exercício 1.1 (Resolvido)
# Crie um arquivo 'diario.txt' e registre uma entrada de diário sobre seu dia.
with open('diario.txt', 'w', encoding = 'utf-8') as file:
    file.write("Hoje aprendi a manipular arquivos em Python!\n")

# Exercício 1.2
# Crie um arquivo 'tarefas.txt' e adicione 3 tarefas diárias.

with open('tarefas.txt', 'w', encoding = 'utf-8') as file:
    file.write(" ajudar minha mae\n")
    file.write(' comemorar meu aniversario\n')
    file.write('cantar meu parabens!\n')

# Exercício 1.3
# Crie um arquivo 'metas.txt' registrando 2 metas pessoais para o ano.

with open('metas.txt', 'w', encoding = 'utf-8') as file:
    file.write("começar a trabalhar\n")
    file.write('viajar para fora do país\n')

# Exercício 1.4 (Resolvido)
# Leia o conteúdo do arquivo 'diario.txt' e imprima na tela.

with open('diario.txt', 'r', encoding = 'utf-8') as file:
    conteudo = file.read()
    print(conteudo)

# Exercício 1.5
# Leia o arquivo 'tarefas.txt' e mostre cada tarefa com um número de prefixo.

with open('tarefas.txt', 'r', encoding = 'utf-8') as file:
    i = 0
    for line in file:
        i = i + 1
        print(str(i) + '. ' + line.strip())

# Exercício 1.6
# Leia 'metas.txt' e formate a saída com bordas decorativas.

with open('metas.txt', 'r', encoding = 'utf-8') as file:
    conteudo3 = file.read()
    for line in conteudo3:
        print("- " + conteudo3)

# Exercício 1.7 (Resolvido)
# Adicione uma nova linha ao final do 'diario.txt' sem apagar o conteúdo existente.
with open('diario.txt', 'a') as file:
    file.write("Agora estou praticando escrita de arquivos!\n")

# Exercício 1.8
# Adicione uma nova tarefa ao 'tarefas.txt' sem apagar as existentes.

with open('tarefas.txt', 'a', encoding = 'utf-8') as file:
    file.write('comer meu bolo de aniversário\n')

# Exercício 1.9
# Registre o progresso de uma meta no 'metas.txt'.

meta = 'viajar para fora do país'
progresso = 20
data = "07/07/2025"

with open('metas.txt', 'a', encoding = 'utf-8') as file:
    file.write(f"[{data}] Meta: {meta}\n")
    file.write(f"Concluído: {progresso}%\n")

# Exercício 1.10 (Resolvido)
# Conte quantas linhas existem no arquivo 'diario.txt'.
with open('diario.txt', 'r', encoding = 'utf-8') as file:
    linhas = file.readlines()
    print(f"Total de entradas no diário: {len(linhas)}")

# Exercício 1.11
# Conte quantas tarefas estão registradas em 'tarefas.txt'.

with open('tarefas.txt', 'r', encoding='utf-8') as file:
    tarefas = file.readlines()
    print(f"Total de tarefas: {len(tarefas)}")

# Exercício 1.12
# Verifique se a palavra "urgente" aparece em qualquer tarefa.

with open('tarefas.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()
    encontrou = False
    for linha in linhas:
        if "urgente" in linha.lower():
            print("Tarefa urgente encontrada:", linha.strip())
            encontrou = True

    if not encontrou:
        print("Nenhuma tarefa urgente encontrada.")

# Exercício 1.13 (Resolvido)
# Crie um backup do diário chamado 'diario_backup.txt'.
with open('diario.txt', 'r') as origem, open('diario_backup.txt', 'w') as destino:
    destino.write(origem.read())

# Exercício 1.14
# Crie um backup das tarefas com data no nome do arquivo.

# Exercício 1.15
# Transforme todas as metas em maiúsculas em um novo arquivo 'metas_prioridade.txt'.

with open('metas.txt', 'r', encoding='utf-8') as file:
    metas = file.readlines()

with open('metas_prioridade.txt', 'w', encoding='utf-8') as file:
    for meta in metas:
        file.write(meta.upper())

# ==================================================
# BLOCO 2: ARQUIVOS CSV (15 exercícios)
# ==================================================

# --- Introdução ---
import csv

# Exercício 2.1 (Resolvido)
# Crie um arquivo 'contatos.csv' com cabeçalhos: nome,email,telefone
cabecalhos = ['nome', 'email', 'telefone']
contatos = [
    ['Ana Silva', 'ana@email.com', '(11) 91234-5678'],
    ['Carlos Oliveira', 'carlos@empresa.com', '(21) 99876-5432']
]

with open('contatos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecalhos)
    writer.writerows(contatos)

# Exercício 2.2
# Crie um CSV 'produtos.csv' com campos: id,nome,preço,estoque

produtos = ['id','nome','preço','estoque']
campos = [['1234', 'ipad', 'R$: 3.000', '27'], ['3459', 'iphone', 'R$: 7.000', '700']]
with open('produtos.csv', newline='', encoding = 'utf-8') as file:


# Exercício 2.3
# Crie um CSV 'eventos.csv' para registrar shows: artista,local,data,ingressos

eventos = ['artista','local','data','ingressos']
shows = [['Demi lovato', 'Arena Pernambuco', '07/07/2026', '3.000'], ['Taylor Swift', 'classic Hall', '23/04/2026', '5.000']]
with open('eventos.csv',newline='') as file:

# Exercício 2.4 (Resolvido)
# Leia 'contatos.csv' e mostre os dados em formato de tabela
with open('contatos.csv', newline='') as file:
    reader = csv.reader(file)
    for linha in reader:
        print(f"{linha[0]:<20} | {linha[1]:<20} | {linha[2]}")

# Exercício 2.5
# Leia 'produtos.csv' e calcule o valor total do estoque

with open('produtos.csv', newline='') as file:
    reader = csv.DictReader(file)
    total = 0
    for produto in reader:
        preco = float(produto['preco'])
        quantidade = int(produto['quantidade'])
        total += preco * quantidade

print(f"Valor total do estoque: R$ {total:.2f}")

# Exercício 2.6
# Leia 'eventos.csv' e mostre apenas eventos com ingressos disponíveis

with open('eventos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for evento in reader:
        if int(evento['ingressos_disponiveis']) > 0:
            print(f"Evento: {evento['nome']} - Ingressos: {evento['ingressos_disponiveis']}")

# Exercício 2.7 (Resolvido)
# Adicione um novo contato ao 'contatos.csv'
novo_contato = ['Maria Santos', 'maria@tech.com', '(31) 94567-1234']
with open('contatos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_contato)

# Exercício 2.8
# Adicione 3 novos produtos ao 'produtos.csv'

novos_produtos = [
    ['P005', 'Teclado Gamer', '149.90', '30'],
    ['P006', 'Mouse sem Fio', '89.90', '50'],
    ['P007', 'Monitor 24"', '799.90', '15']
]

with open('produtos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(novos_produtos)

# Exercício 2.9
# Registre um novo show no 'eventos.csv'

novo_evento = ['Show Rock Nacional', '2025-09-20', '100']

with open('eventos.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(novo_evento)

# Exercício 2.10 (Resolvido)
# Converta o CSV para dicionário e encontre contatos com domínio específico
with open('contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if 'empresa.com' in contato['email']:
            print(f"Contato corporativo: {contato['nome']}")

# Exercício 2.11
# Calcule a média de preços dos produtos usando dicionários

with open('produtos.csv', newline='') as file:
    reader = csv.DictReader(file)
    soma = 0
    count = 0
    for produto in reader:
        soma += float(produto['preco'])
        count += 1

media = soma / count if count else 0
print(f"Média de preços: R$ {media:.2f}")

# Exercício 2.12
# Atualize a quantidade de ingressos para um evento específico

evento_alvo = 'Rock in Rio'
nova_quantidade = 80

eventos_atualizados = []

with open('eventos.csv', newline='') as file:
    reader = csv.DictReader(file)
    eventos = list(reader)
    for evento in eventos:
        if evento['nome'] == evento_alvo:
            evento['ingressos_disponiveis'] = str(nova_quantidade)
        eventos_atualizados.append(evento)

with open('eventos.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=eventos[0].keys())
    writer.writeheader()
    writer.writerows(eventos_atualizados)


# Exercício 2.13 (Resolvido)
# Valide telefones no formato (XX) XXXXX-XXXX
import re
with open('contatos.csv', newline='') as file:
    reader = csv.DictReader(file)
    for contato in reader:
        if not re.match(r'\(\d{2}\) \d{5}-\d{4}', contato['telefone']):
            print(f"Telefone inválido: {contato['nome']}")

# Exercício 2.14
# Valide se todos os IDs de produtos são únicos

with open('produtos.csv', newline='') as file:
    reader = csv.DictReader(file)
    ids = set()
    duplicados = False
    for produto in reader:
        if produto['id'] in ids:
            print(f"ID duplicado encontrado: {produto['id']}")
            duplicados = True
        else:
            ids.add(produto['id'])

if not duplicados:
    print("Todos os IDs são únicos.")

# Exercício 2.15
# Crie um sistema de busca por artista no 'eventos.csv'

artista = input("Digite o nome do artista: ").lower()

with open('eventos.csv', newline='') as file:
    reader = csv.DictReader(file)
    encontrados = False
    for evento in reader:
        if artista in evento['nome'].lower():
            print(f"Evento encontrado: {evento['nome']} - Data: {evento['data']}")
            encontrados = True

if not encontrados:
    print("Nenhum evento encontrado para esse artista.")

# ==================================================
# ==================================================
# BLOCO 3: ARQUIVOS JSON (15 exercícios) - TEMA: JOGOS E REDES SOCIAIS
# ==================================================

# --- Introdução ---
import json

# Exercício 3.1 (Resolvido)
# Salve os dados de um personagem de RPG em 'personagem.json': nome, nível, pontos de vida, habilidades e equipamentos
personagem = {
    "nome": "Arya Stark",
    "nivel": 15,
    "hp": 320,
    "habilidades": ["Agilidade", "Furtividade", "Disfarces"],
    "equipamentos": {
        "arma": "Agulha",
        "armadura": "Couro",
        "anel": "Nenhum"
    }
}

with open('personagem.json', 'w') as file:
    json.dump(personagem, file, indent=4)

# Exercício 3.2
# Crie um arquivo 'perfil_instagram.json' com dados de um influenciador: username, seguidores, seguindo, posts e biografia

perfil = {
    "username": "tech_influencer",
    "seguidores": 12500,
    "seguindo": 340,
    "posts": [
        {"data": "2025-07-10", "likes": 120},
        {"data": "2025-07-11", "likes": 85}
    ],
    "biografia": "Dicas de tecnologia e reviews semanais."
}

with open('perfil_instagram.json', 'w') as file:
    json.dump(perfil, file, indent=4)

# Exercício 3.3
# Armazene os dados de um monstro em 'monstro.json': nome, tipo, nível, pontos_ataque e recompensas

monstro = {
    "nome": "Dragão de Gelo",
    "tipo": "Dragão",
    "nível": 25,
    "pontos_ataque": 180,
    "recompensas": {
        "ouro": 300,
        "gema rara": 1,
        "experiência": 5000
    }
}

with open('monstro.json', 'w') as file:
    json.dump(monstro, file, indent=4)

# Exercício 3.4 (Resolvido)
# Leia 'personagem.json' e mostre as habilidades do personagem
with open('personagem.json') as file:
    dados = json.load(file)
    print("Habilidades:", ", ".join(dados['habilidades']))

# Exercício 3.5
# Leia 'perfil_instagram.json' e calcule a taxa de engajamento (média de likes por post)

with open('perfil_instagram.json') as file:
    perfil = json.load(file)

total_likes = sum(post['likes'] for post in perfil['posts'])
media_likes = total_likes / len(perfil['posts'])
engajamento = media_likes / perfil['seguidores'] * 100

print(f"Taxa de engajamento: {engajamento:.2f}%")

# Exercício 3.6
# Leia 'monstro.json' e mostre a recompensa mais valiosa

with open('monstro.json') as file:
    monstro = json.load(file)

mais_valiosa = max(monstro['recompensas'].items(), key=lambda x: x[1])
print(f"Recompensa mais valiosa: {mais_valiosa[0]} - {mais_valiosa[1]}")

# Exercício 3.7 (Resolvido)
# Atualize o nível do personagem para 16 e salve no arquivo
with open('personagem.json') as file:
    dados = json.load(file)
    
dados['nivel'] = 16

with open('personagem.json', 'w') as file:
    json.dump(dados, file, indent=4)

# Exercício 3.8
# Adicione um novo post ao perfil do Instagram com data e likes

novo_post = {"data": "2025-07-12", "likes": 142}

with open('perfil_instagram.json') as file:
    perfil = json.load(file)

perfil['posts'].append(novo_post)

with open('perfil_instagram.json', 'w') as file:
    json.dump(perfil, file, indent=4)

# Exercício 3.9
# Atualize os pontos de ataque do monstro após uma evolução

with open('monstro.json') as file:
    monstro = json.load(file)

monstro['pontos_ataque'] += 50

with open('monstro.json', 'w') as file:
    json.dump(monstro, file, indent=4)

# Exercício 3.10 (Resolvido)
# Valide se o personagem tem equipamento de arma
with open('personagem.json') as file:
    dados = json.load(file)
    if "arma" in dados['equipamentos'] and dados['equipamentos']['arma']:
        print("Personagem está armado!")
    else:
        print("Personagem desarmado!")

# Exercício 3.11
# Verifique se o perfil do Instagram tem mais de 10.000 seguidores

with open('perfil_instagram.json') as file:
    perfil = json.load(file)

if perfil['seguidores'] > 10000:
    print("Perfil é popular!")
else:
    print("Perfil ainda em crescimento.")

# Exercício 3.12
# Calcule o valor total das recompensas do monstro

with open('monstro.json') as file:
    monstro = json.load(file)

total = sum(valor for valor in monstro['recompensas'].values() if isinstance(valor, (int, float)))
print(f"Valor total das recompensas: {total}")


# Exercício 3.13 (Resolvido)
# Converta os dados do personagem para string JSON e salve em formato minificado
personagem_str = json.dumps(personagem, separators=(',', ':'))
with open('personagem_min.json', 'w') as file:
    file.write(personagem_str)

# Exercício 3.14
# Crie um backup do perfil do Instagram com a data atual no nome do arquivo

# Exercício 3.15
# Combine dados de múltiplos personagens em um arquivo 'grupo.json'

personagens = [
    {"nome": "Arya", "nivel": 16},
    {"nome": "Jon Snow", "nivel": 18},
    {"nome": "Daenerys", "nivel": 20}
]

with open('grupo.json', 'w') as file:
    json.dump(personagens, file, indent=4)

# ==================================================
# BLOCO 4: EXERCÍCIOS MISTOS (5 exercícios)
# ==================================================

# Exercício 4.1 (Resolvido)
# Converta dados de personagens de JSON para CSV
def json_para_csv(origem, destino):
    with open(origem) as json_file:
        dados = json.load(json_file)
    
    with open(destino, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(dados.keys())
        writer.writerow(dados.values())

# Teste:
json_para_csv('personagem.json', 'personagem.csv')

# Exercício 4.2
# Crie um sistema de inventário que salva itens coletados em TXT, CSV e JSON

import csv
import json

inventario = [
    {"item": "Espada de Aço", "quantidade": 1, "durabilidade": 85},
    {"item": "Poção de Vida", "quantidade": 5, "durabilidade": 100},
    {"item": "Escudo de Ferro", "quantidade": 1, "durabilidade": 60}
]

# Salvar em TXT
with open('inventario.txt', 'w') as file:
    for item in inventario:
        file.write(f"{item['item']} - Quantidade: {item['quantidade']} - Durabilidade: {item['durabilidade']}%\n")

# Salvar em CSV
with open('inventario.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=inventario[0].keys())
    writer.writeheader()
    writer.writerows(inventario)

# Salvar em JSON
with open('inventario.json', 'w') as file:
    json.dump(inventario, file, indent=4)

# Exercício 4.3
# Desenvolva um feed de notícias de jogo que salva em JSON e exporta para TXT

feed = [
    {"data": "2025-07-07", "titulo": "Novo boss apareceu!", "descricao": "Dragão Branco de olhos azuis é invocado."},
    {"data": "2025-07-19", "titulo": "Evento especial", "descricao": "XP em dobro durante o fim de semana."}
]

# Salvar em JSON
with open('feed_jogo.json', 'w') as file:
    json.dump(feed, file, indent=4)

# Exportar para TXT
with open('feed_jogo.txt', 'w') as file:
    for noticia in feed:
        file.write(f"{noticia['data']} - {noticia['titulo']}\n{noticia['descricao']}\n\n")


# Exercício 4.4
# Crie um analisador de perfil social que lê JSON e gera relatório em CSV

# Exemplo de perfil JSON
perfil_social = {
    "username": "player_master",
    "seguidores": 8700,
    "seguindo": 420,
    "biografia": "Jogador de MMORPGs e speedruns.",
    "posts": [
        {"data": "2025-07-01", "likes": 130},
        {"data": "2025-07-02", "likes": 210},
        {"data": "2025-07-03", "likes": 95}
    ]
}

# Salvar JSON de exemplo
with open('perfil_social.json', 'w') as file:
    json.dump(perfil_social, file, indent=4)

# Gerar relatório CSV com os posts
with open('perfil_social.json') as file:
    perfil = json.load(file)

with open('relatorio_perfil.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['data_postagem', 'likes', 'username', 'seguidores', 'seguindo'])
    for post in perfil['posts']:
        writer.writerow([
            post['data'],
            post['likes'],
            perfil['username'],
            perfil['seguidores'],
            perfil['seguindo']
        ])

# Exercício 4.5
# Implemente um sistema de save game que compacta dados em ZIP

import zipfile

# Dados de save
save_game = {
    "jogador": "Artemis",
    "nivel": 22,
    "local": "Floresta Sombria",
    "inventario": ["Espada", "Poção", "Mapa"]
}

# Salvar o save em JSON
with open('savegame.json', 'w') as file:
    json.dump(save_game, file, indent=4)

# Compactar o save em ZIP
with zipfile.ZipFile('savegame.zip', 'w') as zipf:
    zipf.write('savegame.json')

# (Opcional) Remover o JSON original se desejar apenas o ZIP
# os.remove('savegame.json')
