import json
from Page1.funcoes import (
    registrar_horas,
    registrar_bateria_de_estudos,
    registrar_nota_redacao,
    mostrar_total_horas
)

# ==============================
# CARREGAR DADOS
# ==============================

try:
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except FileNotFoundError:
    dados = {
        "Matemática": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Linguagens": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "História": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Geografia": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Sociologia": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Filosofia": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Biologia": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Quimica": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Física": {"Horas de Estudo": 0, "Acertos/Total da Bateria de Questões": []},
        "Redacao": {"Horas de Estudo": 0, "Resultado": []}
    }

# ==============================
# FUNÇÃO PARA SALVAR
# ==============================

def salvar_dados():
    print("SALVANDO DADOS...")
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# ==============================
# MENU
# ==============================

def mostrar_menu():
    print("\n=== MENU ===")
    print("1. Registrar horas de estudo")
    print("2. Registrar bateria de questões")
    print("3. Registrar nota Redação")
    print("4. Total de horas de estudo")
    print("5. Sair")

# ==============================
# LOOP PRINCIPAL
# ==============================

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_horas(dados)
        salvar_dados()

    elif opcao == "2":
        registrar_bateria_de_estudos(dados)
        salvar_dados()

    elif opcao == "3":
        registrar_nota_redacao(dados)
        salvar_dados()

    elif opcao == "4":
        mostrar_total_horas(dados)

    elif opcao == "5":
        salvar_dados()
        print("Dados salvos. Saindo...")
        break

    else:
        print("Opção inválida!")

