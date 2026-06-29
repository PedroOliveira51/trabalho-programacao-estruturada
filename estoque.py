def cadastrar_produtos():
    """Lê a quantidade de produtos e os cadastra, retornando uma lista."""
    while True:
        try:
            n = int(input("Quantos produtos deseja cadastrar? "))
            if n <= 0:
                print("  Informe um número maior que zero.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")
 
    produtos = []
    for i in range(1, n + 1):
        print(f"\n--- Produto {i} ---")
        nome = input("  Nome do produto: ").strip()
        while not nome:
            print("  O nome não pode ser vazio.")
            nome = input("  Nome do produto: ").strip()
 
        while True:
            try:
                quantidade = int(input("  Quantidade inicial em estoque: "))
                if quantidade < 0:
                    print("  A quantidade não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("  Entrada inválida. Digite um número inteiro.")
 
        while True:
            try:
                preco = float(input("  Preço unitário (R$): "))
                if preco < 0:
                    print("  O preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("  Entrada inválida. Digite um número decimal (ex.: 12.50).")
 
        produtos.append({
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        })
        print(f"  ✔ '{nome}' cadastrado com sucesso.")
 
    return produtos
 
 
def encontrar_produto(produtos, nome_busca):
    """Retorna o índice do produto pelo nome (case-insensitive) ou -1 se não encontrado."""
    nome_busca = nome_busca.strip().lower()
    for i, p in enumerate(produtos):
        if p["nome"].lower() == nome_busca:
            return i
    return -1
 
 
def adicionar_estoque(produtos):
    """Adiciona unidades ao estoque de um produto."""
    nome = input("  Nome do produto: ").strip()
    idx = encontrar_produto(produtos, nome)
    if idx == -1:
        print(f"  Produto '{nome}' não encontrado.")
        return
 
    while True:
        try:
            qtd = int(input("  Quantidade a adicionar: "))
            if qtd <= 0:
                print("  A quantidade deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")
 
    produtos[idx]["quantidade"] += qtd
    print(f"  ✔ Adicionado {qtd} unidade(s). "
          f"Novo estoque: {produtos[idx]['quantidade']} un.")
 
 
def retirar_estoque(produtos):
    """Retira unidades do estoque de um produto, validando disponibilidade."""
    nome = input("  Nome do produto: ").strip()
    idx = encontrar_produto(produtos, nome)
    if idx == -1:
        print(f"  Produto '{nome}' não encontrado.")
        return
 
    while True:
        try:
            qtd = int(input("  Quantidade a retirar: "))
            if qtd <= 0:
                print("  A quantidade deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")
 
    if qtd > produtos[idx]["quantidade"]:
        print(f"  ✘ Estoque insuficiente! "
              f"Disponível: {produtos[idx]['quantidade']} un.")
    else:
        produtos[idx]["quantidade"] -= qtd
        print(f"  ✔ Retirado {qtd} unidade(s). "
              f"Novo estoque: {produtos[idx]['quantidade']} un.")
 
 
def consultar_produto(produtos):
    """Exibe os dados de um produto específico."""
    nome = input("  Nome do produto: ").strip()
    idx = encontrar_produto(produtos, nome)
    if idx == -1:
        print(f"  Produto '{nome}' não encontrado.")
        return
 
    p = produtos[idx]
    valor_total = p["quantidade"] * p["preco"]
    print(f"\n  {'Produto':<20} {p['nome']}")
    print(f"  {'Quantidade':<20} {p['quantidade']} un.")
    print(f"  {'Preço unitário':<20} R$ {p['preco']:.2f}")
    print(f"  {'Valor total':<20} R$ {valor_total:.2f}")
 
 
def listar_produtos(produtos):
    """Lista todos os produtos com valor total em estoque."""
    if not produtos:
        print("  Nenhum produto cadastrado.")
        return
 
    col = "{:<4} {:<20} {:>10} {:>14} {:>14}"
    linha = "-" * 66
    print(f"\n{linha}")
    print(col.format("#", "Produto", "Qtd (un.)", "Preço unit.", "Valor total"))
    print(linha)
    for i, p in enumerate(produtos, start=1):
        valor_total = p["quantidade"] * p["preco"]
        print(col.format(
            i,
            p["nome"][:20],
            p["quantidade"],
            f"R$ {p['preco']:.2f}",
            f"R$ {valor_total:.2f}"
        ))
    print(linha)
 
    total_geral = sum(p["quantidade"] * p["preco"] for p in produtos)
    print(f"  Valor total do estoque: R$ {total_geral:.2f}\n")
 
 
def exibir_menu():
    """Exibe o menu principal."""
    print("\n========== MENU ==========")
    print("  (a) Adicionar unidades ao estoque")
    print("  (b) Retirar unidades do estoque")
    print("  (c) Consultar um produto")
    print("  (d) Listar todos os produtos")
    print("  (e) Encerrar o programa")
    print("===========================")
 
 
def main():
    print("╔══════════════════════════════════╗")
    print("║   CONTROLE DE ESTOQUE SIMPLES    ║")
    print("╚══════════════════════════════════╝\n")
 
    produtos = cadastrar_produtos()
 
    opcoes = {"a", "b", "c", "d", "e"}
 
    while True:
        exibir_menu()
        escolha = input("  Escolha uma opção: ").strip().lower()
 
        if escolha not in opcoes:
            print("  Opção inválida. Tente novamente.")
            continue
 
        print()
        if escolha == "a":
            adicionar_estoque(produtos)
        elif escolha == "b":
            retirar_estoque(produtos)
        elif escolha == "c":
            consultar_produto(produtos)
        elif escolha == "d":
            listar_produtos(produtos)
        elif escolha == "e":
            print("  Programa encerrado. Até logo!")
            break
 
 
if __name__ == "__main__":
    main()