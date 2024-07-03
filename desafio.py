import csv

def ler_csv(file) -> list:
    dados = []
    with open(file=file, mode='r', encoding='utf-8') as file:
        leitor_csv = csv.DictReader(file)
        for linha in leitor_csv:
            dados.append(linha)
    return dados

def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item['Categoria']
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias

def calcular_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = sum(int(item['Quantidade']) * int(item['Venda']) for item in itens)
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

def imprime(vendas_por_categoria):
    for categoria, total in vendas_por_categoria.items():
        print(f'{categoria}: ${total}')

def pipeline(file):
    dados = ler_csv(file)
    venda_produtos = processar_dados(dados)
    vendas_por_categoria = calcular_vendas_categoria(venda_produtos)
    imprime(vendas_por_categoria)
    return vendas_por_categoria

if __name__ == '__main__':
    file = 'vendas.csv'
    pipeline(file)