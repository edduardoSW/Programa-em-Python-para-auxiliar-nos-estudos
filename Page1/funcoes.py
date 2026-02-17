def registrar_horas(dados):
    print("\nMatérias disponíveis: ")
    for materia in dados:
        print("-", materia)

    materia = input("\nDigite a matéria: ")

    if materia in dados:
        try:
            horas = float(input("Quantos horas estudadndo?"))
            dados[materia]["Horas de Estudo"] += horas
            print("Horas registradas com sucesso!")
        except:
            print("Digite um número válido.")
    else:
        print("Matéria não encontrada.")

def registrar_bateria_de_estudos(dados):
    materia = input("Digite a matéria: ")
    if materia in dados:
        try:
            acertos = int(input("Quantos acertos?"))
            total = int(input("Total de questões?"))
            dados[materia]["Acertos/Total da Bateria de Questões"].append((acertos, total))
            print("Bateria registrada com sucesso!")
        except ValueError:
            print("Digite apenas números.")
    else:
        print("Matéria não encontrada.")

def registrar_nota_redacao(dados):
    try:
        nota = int(input("Qual a sua nota? "))

        if nota % 20 == 0 and 0 <= nota <= 1000:
            dados["Redacao"]["Resultado"].append(nota)
            print("Sua nota da redação foi registrada com sucesso!")
        else:
            print("A nota deve ser múltipla de 20 e entre 0 e 1000.")

    except ValueError:
        print("Digite um número válido.")

def mostrar_total_horas(dados):
    total_geral = 0

    print("\n=== Relatório de Horas ===")

    for materia in dados:
        horas = dados[materia]["Horas de Estudo"]
        print(f"{materia}: {horas} horas")
        total_geral += horas

    print(f"\nTotal geral: {total_geral} horas")

