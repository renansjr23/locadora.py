import os
print("Bem vindo a locadora do futuro")

print("Portfólio de Carros")

portifolio = {
            1:  'Porsche 992 Turbo S',
            2:  'BMW X6 M',
            3:  'Mercedes GLC 500 AMG',
            4:  'Tesla Model X',
            5:  'Range Rover Sport',
            6:  'Volvo XC 90',
            7:  'Land Rover Defender',
            8:  'Porsche taycan' 
}

precos_dia = {1: 120, 2: 90, 3: 150, 4: 85, 5: 120, 6: 60, 7: 70, 8: 130}
alugados = {}
dias_alugados = {} #chave + soma em reais do valor a pagar

def tela_principal():
    os.system('cls')
    print('O que precisa fazer? Escolha uma das opções abaixo:\n')
    while True:
        preciso = input('0 - Mostrar portifólio disponível | 1 - Alugar um carro | 2 - Devolver um veículo | 3 - Sair do Programa\n\n')
        if preciso not in ['0', '1', '2', '3']:
            print('\nDigite somente 0, 1, 2 ou 3!\n')
            continue
        break
    if preciso == '0':
        mostrar_portifolio()
    elif preciso == '1':
        mostrar_tela_aluguel()
    elif preciso  == '2':
        tela_devolver_veiculo()
        #por aqui a tela de devolução
    else:
        print('\nSAINDO DO PROGRAMA! Até a próxima...')   
        return
#=========================Função=Tela=Portifólio===============================================
def mostrar_portifolio():
    os.system('cls')
    for chave, nome, in portifolio.items():
        print(f'{chave} {nome} - R$ {precos_dia.get(chave)} /dia')
    print('=' * 20)
    sair_ou_voltar()
    return

#=========================Tela=de=Alugar========================================================
def mostrar_tela_aluguel():
    global alugados
    os.system('cls')
    print('ALUGUEL')
    for chave, nome, in portifolio.items():
        print(f'{chave} {nome} - R$ {precos_dia.get(chave)} /dia')
    print('=' * 20)
    while True:
        try:
            veiculo_a_alugar = int(input('\nEscolha o código do veículo de acordo com os dados acima: '))
        except ValueError:
            print('Escolha somente um dos números acima!')
            continue
        if veiculo_a_alugar not in portifolio.keys():
            print('Escolha somente um dos números acima!')
            continue
        break
    print(f'\nVoce escolheu o veículo {portifolio.get(veiculo_a_alugar)}, para quantos dias deseja alugá-lo? De 2 a 7 dias.  \n')
    while True:
        try:
            quantos_dias = int(input())
        except ValueError:
            print('Digite um número válido, de 2 a 7 dias.')
            continue
        if quantos_dias not in range(2,8):
            print('Somente de 2 a 7 dias.')
            continue
        break
    while True:
        desistir = input(f'\nVocê escolheu {portifolio.get(veiculo_a_alugar)} por {quantos_dias} dias, valor total {(precos_dia.get(veiculo_a_alugar) * quantos_dias):.2f}, confirmar aluguel? 0 - SIM | 1 - NÃO ')
        if desistir not in ['0', '1']:
            print('Digite somente 0 ou 1!')
            continue
        elif desistir == '1':
            tela_principal()
            return
        else:
            break

    alugados[veiculo_a_alugar] = portifolio.pop(veiculo_a_alugar) # código de passar do dicionário de disponiveis para o de alugados
    dias_alugados[veiculo_a_alugar] = precos_dia.get(veiculo_a_alugar) * quantos_dias #adiciona o valor dos dias alugados a um dicionario, corriga essa linha
    print(f'\nParabéns! Você alugou {alugados.get(veiculo_a_alugar)} por {quantos_dias} dias, valor total {(precos_dia.get(veiculo_a_alugar) * quantos_dias):.2f}.')   
    alugados = dict(sorted(alugados.items()))
    sair_ou_voltar()
    return
#=============================Tela=de=Devolver==================================================
def tela_devolver_veiculo():
    global portifolio
    os.system('cls')
    for chave_a, nome_a, in alugados.items():
        print(f'{chave_a} {nome_a} - R$ {dias_alugados.get(chave_a)} a pagar')
    print('=' * 20)
    while True:
        if alugados == {}:
            print('\nNão há nenhum veículo alugado no momento para devolver!')
            sair_ou_voltar()
            return
        try:
            veiculo_a_devolver = int(input('\nEscolha o código do veículo de acordo com os dados acima: '))
        except ValueError:
            print('Escolha somente um dos números acima!')
            continue
        if veiculo_a_devolver not in alugados.keys():
            print('Escolha somente um dos números acima!')
            continue
        break
    print(f'\nObrigado por devolver o veículo {alugados.get(veiculo_a_devolver)}, receba o pagamento de R$ {dias_alugados.pop(veiculo_a_devolver):.2f}!') #já remove o valor a pagar do dicionario
    portifolio[veiculo_a_devolver] =  alugados.pop(veiculo_a_devolver) # remove o veiculo do dicionario de alugados e poe no dicionario de disponíveis
    portifolio = dict(sorted(portifolio.items()))
    sair_ou_voltar()
    return
#========================Função=de=Sair=ou=Voltar===============================================
def sair_ou_voltar():
    while True:
        voltar = input('\n0 - VOLTAR | 1 - SAIR\n')
        if voltar not in ['0', '1']:
            print('Digite somente 0 ou 1!')
            continue
        elif voltar == '0':
            os.system('cls')
            tela_principal()
        else:
            print('\nSAINDO DO PROGRAMA! Até a próxima...')
        break
    return
#========================Execução=do=codigo=====================================================
tela_principal()