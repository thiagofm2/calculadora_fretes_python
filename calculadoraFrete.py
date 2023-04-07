def dimensoesobjeto(altura, comprimento, largura):
    valorvolume = 0
    while True:
        try:
            valoraltura = int(input(altura))
            valorcomprimento = int(input(comprimento))
            valorlargura = int(input(largura))
            volume = valoraltura * valorcomprimento * valorlargura
            if volume <= 1000:
                valorvolume = 10.00
                print('O valor em R$ por um produto deste volume é de: {}'.format(valorvolume))
                break
            elif 1000 <= volume < 10000:
                valorvolume = 20.00
                print('O valor em R$ por um produto deste volume é de: {}'.format(valorvolume))
                break
            elif 10000 <= volume < 30000:
                valorvolume = 30.00
                print('O valor em R$ por um produto deste volume é de: {}'.format(valorvolume))
                break
            elif volume >= 100000:
                print('Valor não aceito.')
                continue
        except ValueError:
            print('Oops, número inválido, tente novamente!')
            continue
    return valorvolume


def pesoobjeto(peso):
    total = 0
    while True:
        try:
            valorpeso = float(input(peso))
            if valorpeso <= 0.1:
                total = valorpeso * 1
                print('Valor em R$ do peso é de: {}'.format(total))
                break
            elif 0.1 < valorpeso < 1:
                total = valorpeso * 1.5
                print('Valor em R$ do peso é de: {}'.format(total))
                break
            elif 1 < valorpeso < 10:
                total = valorpeso * 2
                print('Valor em R$ do peso é de: {}'.format(total))
                break
            elif 10 < valorpeso < 30:
                total = valorpeso * 3
                print('Valor em R$ do peso é de: {}'.format(total))
                break
            elif valorpeso >= 30:
                print('Valor não aceito.')
                continue
        except ValueError:
            print('Opa, parece que você digitou um valor errado, por favor, digite um correto.')
            continue
    return total


def rotaobjeto(rota):
    totalrota = ''
    while True:
        perguntarota = input(rota)
        if perguntarota == 'RS':
            totalrota = 1
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota == 'SR':
            totalrota = 1
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota == 'BS':
            totalrota = 1.2
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota == 'SB':
            totalrota = 1.2
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota == 'BR':
            totalrota = 1.5
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota == 'RB':
            totalrota = 1.5
            print('Valor da rota é equivalente a {}'.format(totalrota))
            break
        elif perguntarota != 'RS' or perguntarota != 'SR' or perguntarota != 'BS' or perguntarota != 'SB' or perguntarota != 'BR' or perguntarota != 'RB':
            print('Rota inválida, insira uma sigla existente.')
            continue
    return totalrota

volumeObjeto = dimensoesobjeto(
    'Digite a altura em Cm do objeto que você deseja transportar: ',
    'Digite o comprimento em Cm do objeto que você deseja transportar: ',
    'Digite a largura do objeto que você deseja transportar: '
)

calculoPesoObjeto = pesoobjeto('Digite o peso em KG do objeto: ')

print('Escolha qual a rota de entrega do seu produto: ')
print('RS - Rio de Janeiro - São Paulo')
print('SR - São Paulo - Rio de Janeiro')
print('BS - Brasilia - São Paulo')
print('SB - São Paulo - Brasilia')
print('BR - Brasilia - Rio de Janeiro')
print('RB - Rio de Janeiro - Brasilia')
calculoRotaObjeto = rotaobjeto('Digite a sigla da rota que você deseja: ')

valortotal = volumeObjeto * calculoPesoObjeto * calculoRotaObjeto
print('O valor total do frete é de: {} (Volume: R${}, Peso: R${}, Rota: R${},)'.format(valortotal, volumeObjeto, calculoPesoObjeto, calculoRotaObjeto))
