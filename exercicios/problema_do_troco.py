MOEDAS = [100, 25, 10, 5, 1]

def ordena_moedas(moedas):
    return sorted(moedas, reverse=True)

def problema_do_troco(valor):
    moedas_ordenadas = ordena_moedas(MOEDAS)
    moedas_de_troco = []

    for moeda in moedas_ordenadas:
        quantidade_moedas = 0
        if valor >= moeda:
            quantidade_moedas = valor // moeda
            valor -= quantidade_moedas * moeda
        moedas_de_troco.append(f'{quantidade_moedas} moeda(s) de {moeda}')
    
    print('\n'.join(moedas_de_troco))   

try:
    valor = int(input('Insira o valor para troco: '))
    problema_do_troco(valor)
except:
    print('Erro: Tipo do valor inválido: Entrada espera um valor inteiro')