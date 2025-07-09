import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_tabuleiro(tamanho):
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

def imprimir_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)
    print("  " + " ".join(str(i) for i in range(tamanho)))
    for i, linha in enumerate(tabuleiro):
        print(str(i) + " " + "|".join(linha))
        if i < tamanho - 1:
            print("  " + "-" * (2 * tamanho - 1))

def verificar_vitoria(tabuleiro, jogador, vencer_com):
    tamanho = len(tabuleiro)

    # Verificar linhas
    for linha in tabuleiro:
        for i in range(tamanho - vencer_com + 1):
            if all(c == jogador for c in linha[i:i+vencer_com]):
                return True

    # Verificar colunas
    for col in range(tamanho):
        for i in range(tamanho - vencer_com + 1):
            if all(tabuleiro[i + j][col] == jogador for j in range(vencer_com)):
                return True

    # Verificar diagonais (\)
    for i in range(tamanho - vencer_com + 1):
        for j in range(tamanho - vencer_com + 1):
            if all(tabuleiro[i + d][j + d] == jogador for d in range(vencer_com)):
                return True

    # Verificar diagonais (/)
    for i in range(vencer_com - 1, tamanho):
        for j in range(tamanho - vencer_com + 1):
            if all(tabuleiro[i - d][j + d] == jogador for d in range(vencer_com)):
                return True

    return False

# =========================
# VARIÁVEIS GLOBAIS
# =========================
tamanho_tabuleiro = 3
sequencia_para_vencer = 3
jogador_X = "Jogador X"
jogador_O = "Jogador O"
placar = { "X": 0, "O": 0 }

def iniciar_jogo():
    global placar
    tabuleiro = criar_tabuleiro(tamanho_tabuleiro)
    jogadores = ["X", "O"]
    nomes = {"X": jogador_X, "O": jogador_O}
    jogadas = 0
    max_jogadas = tamanho_tabuleiro * tamanho_tabuleiro

    while jogadas < max_jogadas:
        limpar_tela()
        imprimir_tabuleiro(tabuleiro)
        jogador_atual = jogadores[jogadas % 2]
        print(f"\nVez de {nomes[jogador_atual]} ({jogador_atual})")

        try:
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada. Pressione Enter para continuar.")
                input()
                continue
        except (ValueError, IndexError):
            print("Entrada inválida. Pressione Enter para continuar.")
            input()
            continue

        tabuleiro[linha][coluna] = jogador_atual
        jogadas += 1
        if verificar_vitoria(tabuleiro, jogador_atual, sequencia_para_vencer):
            limpar_tela()
            imprimir_tabuleiro(tabuleiro)
            print(f"\n{nomes[jogador_atual]} venceu!")
            placar[jogador_atual] += 1
            input("Pressione Enter para voltar ao menu.")
            return

    limpar_tela()
    imprimir_tabuleiro(tabuleiro)
    print("\nEmpate!")
    input("Pressione Enter para voltar ao menu.")

# =========================
# MENU PRINCIPAL
# =========================
def menu():
    global tamanho_tabuleiro, sequencia_para_vencer, jogador_X, jogador_O

    while True:
        limpar_tela()
        print("====== MENU ======")
        print("1. Definir jogador X (atual: {})".format(jogador_X))
        print("2. Definir jogador O (atual: {})".format(jogador_O))
        print("3. Definir tamanho do tabuleiro (atual: {}x{})".format(tamanho_tabuleiro, tamanho_tabuleiro))
        print("4. Definir tamanho da sequência para vencer (atual: {})".format(sequencia_para_vencer))
        print("5. Mostrar placar")
        print("6. Iniciar novo jogo")
        print("7. Sair do jogo")
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            jogador_X = input("Digite o nome do jogador X: ")
        elif escolha == "2":
            jogador_O = input("Digite o nome do jogador O: ")
        elif escolha == "3":
            try:
                novo_tamanho = int(input("Novo tamanho do tabuleiro: "))
                if novo_tamanho >= 3:
                    tamanho_tabuleiro = novo_tamanho
                else:
                    print("O tabuleiro deve ter pelo menos 3x3.")
                    input("Pressione Enter para continuar.")
            except ValueError:
                print("Valor inválido.")
                input("Pressione Enter para continuar.")
        elif escolha == "4":
            try:
                nova_seq = int(input("Novo tamanho da sequência para vencer: "))
                if 3 <= nova_seq <= tamanho_tabuleiro:
                    sequencia_para_vencer = nova_seq
                else:
                    print("A sequência deve ser entre 3 e o tamanho do tabuleiro.")
                    input("Pressione Enter para continuar.")
            except ValueError:
                print("Valor inválido.")
                input("Pressione Enter para continuar.")
        elif escolha == "5":
            print(f"\nPlacar:")
            print(f"{jogador_X} (X): {placar['X']} vitórias")
            print(f"{jogador_O} (O): {placar['O']} vitórias")
            input("\nPressione Enter para continuar.")
        elif escolha == "6":
            iniciar_jogo()
        elif escolha == "7":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Pressione Enter para tentar novamente.")
            input()

menu()