def ler_inteiro_positivo(mensagem):
    """Lê e retorna um inteiro maior que zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("  Informe um número maior que zero.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")
 
 
def ler_inteiro_nao_negativo(mensagem):
    """Lê e retorna um inteiro maior ou igual a zero."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("  A quantidade não pode ser negativa.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")
 
 
def ler_codigo(mensagem):
    """Lê e retorna um código de cliente não vazio."""
    while True:
        codigo = input(mensagem).strip()
        if codigo:
            return codigo
        print("  O código não pode ser vazio.")
 
 
def calcular_tempo_atendimento(itens):
    """Calcula o tempo de atendimento: 2 + 0,5 × itens (em minutos)."""
    return 2 + 0.5 * itens
 
 
def encontrar_caixa_menor_tempo(tempos_caixas):
    """
    Retorna o índice do caixa com menor tempo acumulado.
    Em caso de empate, escolhe o de menor número (menor índice).
    """
    idx_menor = 0
    for i in range(1, len(tempos_caixas)):
        if tempos_caixas[i] < tempos_caixas[idx_menor]:
            idx_menor = i
    return idx_menor
 
 
def alocar_cliente(caixas, tempos_caixas, cliente, tempo):
    """
    Aloca o cliente ao caixa com menor tempo acumulado e
    atualiza o tempo acumulado desse caixa.
    """
    idx = encontrar_caixa_menor_tempo(tempos_caixas)
    caixas[idx].append(cliente)
    tempos_caixas[idx] += tempo
    return idx
 
 
def exibir_resultado(caixas, tempos_caixas):
    """Exibe a fila de atendimento e o tempo total de cada caixa."""
    print("\n" + "═" * 50)
    print("  FILA DE ATENDIMENTO POR CAIXA")
    print("═" * 50)
    for i, (clientes, tempo) in enumerate(zip(caixas, tempos_caixas), start=1):
        codigos = ", ".join(c["codigo"] for c in clientes) if clientes else "—"
        print(f"\n  Caixa {i}:")
        print(f"    Clientes atendidos : {codigos}")
        print(f"    Tempo total        : {tempo:.1f} min")
 
 
def calcular_estatisticas(tempos_clientes, tempos_caixas):
    """Calcula e exibe as estatísticas gerais do sistema."""
    media_atendimento = sum(tempos_clientes) / len(tempos_clientes)
 
    idx_maior = tempos_caixas.index(max(tempos_caixas))
    idx_menor = 0
    for i in range(1, len(tempos_caixas)):
        if tempos_caixas[i] < tempos_caixas[idx_menor]:
            idx_menor = i
 
    tempo_total_sistema = max(tempos_caixas)
 
    print("\n" + "═" * 50)
    print("  ESTATÍSTICAS GERAIS")
    print("═" * 50)
    print(f"  Tempo médio de atendimento por cliente : {media_atendimento:.2f} min")
    print(f"  Caixa com maior tempo acumulado        : Caixa {idx_maior + 1} "
          f"({tempos_caixas[idx_maior]:.1f} min)")
    print(f"  Caixa com menor tempo acumulado        : Caixa {idx_menor + 1} "
          f"({tempos_caixas[idx_menor]:.1f} min)")
    print(f"  Tempo total para encerrar atendimentos : {tempo_total_sistema:.1f} min")
    print("═" * 50)
 
 
def cadastrar_clientes(n_clientes, caixas, tempos_caixas):
    """
    Lê os dados de cada cliente, calcula o tempo de atendimento,
    aloca ao caixa adequado e retorna a lista de tempos individuais.
    """
    tempos_clientes = []
 
    for i in range(1, n_clientes + 1):
        print(f"\n--- Cliente {i} ---")
        codigo = ler_codigo("  Código do cliente   : ")
        itens  = ler_inteiro_nao_negativo("  Qtd. de itens       : ")
 
        tempo = calcular_tempo_atendimento(itens)
        cliente = {"codigo": codigo, "itens": itens, "tempo": tempo}
 
        idx = alocar_cliente(caixas, tempos_caixas, cliente, tempo)
        tempos_clientes.append(tempo)
 
        print(f"  ✔ {codigo} → Caixa {idx + 1}  |  Tempo: {tempo:.1f} min")
 
    return tempos_clientes
 
 
def main():
    print("SIMULADOR DE CAIXA DE SUPERMERCADO\n)")

    n_caixas   = ler_inteiro_positivo("Quantidade de caixas disponíveis : ")
    n_clientes = ler_inteiro_positivo("Quantidade de clientes            : ")

    caixas        = [[] for _ in range(n_caixas)]
    tempos_caixas = [0.0] * n_caixas

    tempos_clientes = cadastrar_clientes(n_clientes, caixas, tempos_caixas)

    exibir_resultado(caixas, tempos_caixas)
    calcular_estatisticas(tempos_clientes, tempos_caixas)
 
 
if __name__ == "__main__":
    main()