### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 40 
preco = 20

if quantidade >= 0 and preco >= 0:
    print('Dados Válidos')
else:
    print('Dados inválidos')

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "hoje é nossa segunda aula de bootcamp, bootcamp de python"

texto = texto.lower() #padroniza o texto com todas as letras minúsculas

caracteres_especiais = [',', '.', ':', ';', '-', '/', '\\', '!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '~', '?'] #lista para remover todos os caracteres especiais
texto_corrigido = [] #lista que receberá cada caracter válido para a tratativa

for caracteres in texto:
    if caracteres not in caracteres_especiais:
        texto_corrigido.append(caracteres)

texto_final = ''.join(texto_corrigido).split()
#print(texto_final)

contagem = {}

for palavra in texto_final:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]

minimo = min(numeros)
maximo = max(numeros)

normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

# usuarios_validos = []

# for usuario in usuarios:
#     if all( valor != '' for valor in usuario.values() ):
#         usuarios_validos.append(usuario)

usuarios_validos = [
    u for u in usuarios
    if all( valor != '' for valor in u.values() )
]

# for usuario in usuarios:
#     # Verifica se nenhum campo está vazio
#     if all(valor != "" for valor in usuario.values()):
#         usuarios_validos.append(usuario)

# for usuario in usuarios_validos:
#     print(usuario)

print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = range(1, 11)

numeros_pares = [x for x in numeros if x % 2 == 0]

print(numeros_pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}

#pegar todas as categorias da base
for venda in vendas:
    categoria = venda['categoria']
    valor = venda['valor']
#agregar o valor em cada categoria
    total_por_categoria[categoria] = total_por_categoria.get(categoria, 0) + valor

print(total_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    entrada = input('Insira algum dado (para sair digite "sair"): ')
    if entrada.lower() == 'sair':
        print('O programa será finalizado')
        break

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

while True:
    try:
        entrada = int(input('Insira algum dado (para sair digite "sair"): '))
    except ValueError:
        print("Dado com formato inválido para a operação. Insira um número inteiro")
    # except TypeError:
    #     print("Unsupported operation!")
    except Exception as e:
        print(e)
    else:
        if entrada >= 0 and entrada <= 10:
            print('O número está dentro do range especificado')
            print('O programa será finalizado...')
            break
        else:
            print('O número está fora do range especificado. Tente novamente\n')

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

import random
import time

tentativas_maximas = 8
tentativa = 1
tentativa_sucesso = random.randint(tentativa, tentativas_maximas)

while tentativa <= tentativas_maximas:
    print(f'Tentativa {tentativa} de {tentativas_maximas}')
    print('Requisitando a API...')
    time.sleep(0.5)
    if tentativa == tentativa_sucesso:
        print('Conexão bem-sucedida (200)')
        break
    print('Conexão falhou (500)\n')
    tentativa += 1

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [1, 2, 3, "parar", 4, 5]

i = 0
while True:
    print(f'Percorrendo item nº{i+1}...')
    print(f'Valor "{itens[i]}" encontrado')
    if itens[i] == 'parar':
        print('Condicao de parada encontrada, o programa será finalizado...')
        break
    print('Continuando iteração...\n')
    i += 1