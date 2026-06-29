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
 
 
def ler_nota(mensagem):
    """Lê e retorna uma nota entre 0 e 10."""
    while True:
        try:
            nota = float(input(mensagem))
            if not (0 <= nota <= 10):
                print("  A nota deve estar entre 0 e 10.")
                continue
            return nota
        except ValueError:
            print("  Entrada inválida. Digite um número (ex.: 7.5).")
 
 
def ler_nome(mensagem):
    """Lê e retorna um nome não vazio."""
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        print("  O nome não pode ser vazio.")
 
 
def calcular_media(n1, n2, n3):
    """Calcula a média aritmética simples de três notas."""
    return (n1 + n2 + n3) / 3
 
 
def classificar(media):
    """Retorna a situação do aluno conforme a média."""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
 
 
def cadastrar_alunos(n):
    """Cadastra n alunos e retorna uma lista de dicionários."""
    alunos = []
    for i in range(1, n + 1):
        print(f"\n--- Aluno {i} ---")
        nome = ler_nome("  Nome: ")
        n1   = ler_nota("  Nota 1: ")
        n2   = ler_nota("  Nota 2: ")
        n3   = ler_nota("  Nota 3: ")
 
        media    = calcular_media(n1, n2, n3)
        situacao = classificar(media)
 
        alunos.append({
            "nome":     nome,
            "n1":       n1,
            "n2":       n2,
            "n3":       n3,
            "media":    media,
            "situacao": situacao,
        })
        print(f"  ✔ '{nome}' cadastrado — Média: {media:.2f} ({situacao})")
    return alunos
 
 
def exibir_tabela(alunos):
    """Exibe a tabela de alunos com notas, média e situação."""
    cab  = f"{'Nome':<22} {'N1':>5} {'N2':>5} {'N3':>5} {'Média':>7} {'Situação':<12}"
    linha = "─" * len(cab)
 
    print(f"\n{linha}")
    print(cab)
    print(linha)
    for a in alunos:
        print(
            f"{a['nome'][:22]:<22} "
            f"{a['n1']:>5.1f} "
            f"{a['n2']:>5.1f} "
            f"{a['n3']:>5.1f} "
            f"{a['media']:>7.2f} "
            f"{a['situacao']:<12}"
        )
    print(linha)
 
 
def exibir_estatisticas(alunos):
    """Calcula e exibe as estatísticas gerais da turma."""
    media_geral = sum(a["media"] for a in alunos) / len(alunos)
 
    melhor = max(alunos, key=lambda a: a["media"])
    pior   = min(alunos, key=lambda a: a["media"])
 
    aprovados    = sum(1 for a in alunos if a["situacao"] == "Aprovado")
    recuperacao  = sum(1 for a in alunos if a["situacao"] == "Recuperação")
    reprovados   = sum(1 for a in alunos if a["situacao"] == "Reprovado")
 

    print("ESTATÍSTICAS DA TURMA")

    print(f"Média geral da turma : {media_geral:>6.2f}            ")
    print(f"Maior média        : {melhor['media']:>6.2f}  ({melhor['nome'][:14]:<14})")
    print(f"Menor média        : {pior['media']:>6.2f}  ({pior['nome'][:14]:<14})")
   
    print(f"Aprovados         : {aprovados:>3} aluno(s)")
    print(f"Recuperação       : {recuperacao:>3} aluno(s)")
    print(f"Reprovados        : {reprovados:>3} aluno(s) ")
   
 
def main():
    print(" ANÁLISE DE NOTAS DE UMA TURMA ")
 
    n  = ler_inteiro_positivo("Quantidade de alunos na turma: ")
    alunos = cadastrar_alunos(n)
 
    exibir_tabela(alunos)
    exibir_estatisticas(alunos)
 
 
if __name__ == "__main__":
    main()