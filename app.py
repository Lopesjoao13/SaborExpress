import os

restaurantes = [{
    'nome': 'Praça',
    'categoria' : 'Japonesa',
    'ativo' : False}, 
    {
    'nome': 'Pizza Suprema',
    'categoria' : 'Pizza',
    'ativo' : True},
    {
    'nome': 'Cantina',
    'categoria' : 'Italiana',
    'ativo' : False}
    ]

def exibir_nome_do_programa():
    '''Exibe estilizado o nome do programa'''
    print('''
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')

def exibir_opcoes():
    '''Essa função somente exibe as opções para o usuario'''
    print('1- Cadastrar restaurante\n2- Listar restaurante\n3- Alternar estado do restaurante\n4- Sair\n')

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    '''Essa função retorna ao menu principal do app'''
    input('\nDigite qualquer tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    '''Essa função é para tratar opções invalidas
    
    output:
    - retorna ao menu principal
    '''
    print('opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função limpa o console e exibe o subtitulo quando chamado'''
    os.system('cls')
    #os.system('clear') para o mac
    linha = '*' * (len(texto)+4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar um novo restaurante
     
    input:
    - Nome do restaurante
    - Categoria  

    Output: 
    - Adiciona um novo restaurante a lista de restaurantes
    
     '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome':nome_do_restaurante,
        'categoria':categoria,
        'ativo': False
    }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()
              
def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados sua categoria e se estão ativos ou não
    
    output: 
    - exibe a lista de restaurantes
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {'ativado' if restaurante['ativo'] else 'desativado'}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Essa função altera o status do restaurante de desativado para ativo ou visse versa
    
    output: 
    - exibe uma mensagem indicando sucesso da operação
    '''
    print('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
        mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso! '
    print(mensagem)
    if not restaurante_encontrado: 
        print('O restaurante não foi encontrado')
    voltar_ao_menu_principal()

def escolher_opcao():
    '''Essa função é responsavel por controlar a opção que o usuario deseja operar
    
    input: 
    - escolha de opção

    output: 
    - executa a opção escolhida pelo usuario
    '''
    try:
        opcao_escolhida = int(input('Esccolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}!')
        match opcao_escolhida:
            case  1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3: 
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()





def main():
    '''Função principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()