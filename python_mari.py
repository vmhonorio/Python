# coding=<Non-UTF-8>
########################################################
def obter_limite():
########################################################
    #                    ATIVIDADE 1
    #Neste trecho esta sendo exibido na tela as informa��es para o cliente
    print("")
    print("Bem vindo a loja Doce Vida! Aqui eh Chica da Silva !")
    print("Faremos uma analise do seu credito, para isso precisamos de algumas informacoes:")
    print("")

    #Aqui, o usuario precisara informar os 3 dados abaixo:
    var_cargo = input("Digite o cargo na empresa em que trabalha atualmente: ")
    while var_cargo.isnumeric():
        var_cargo = input("Cargo invalido, ditite novamente: ")

    #Digita Sal�rio e valida
    var_salario = input("Digite o salario da empresa em que trabalha atualmente: ")
    while var_salario.isalpha():
        var_salario = input("Salario invalido, ditite novamente: ")

    #Digita Ano de nascimento e valida
    var_ano_nascimento = input("Digite o seu ano de nascimento: ")
    while var_ano_nascimento.isalpha():
        var_ano_nascimento = input("Ano de nascimento invalido, digite novamente: ")

    #Mostra os dados informados pelo cliente"
    print('')
    print("O cargo digitado foi: ", var_cargo)
    print("O salario digitado foi: ", var_salario)
    print("O ano digitado foi: ", var_ano_nascimento)
    print('')

    #                    ATIVIDADE 2
    #Calcula idade aproximada do cliete
    var_idade_cliente = int(var_data_atual.year) - int(var_ano_nascimento)
    print('Sua idade aproximada eh: ', var_idade_cliente)

    #Calcula o limite de credito disponivel
    var_limite_credito = (float(var_salario) * (int(var_idade_cliente) / 1000)) + 100
    print("Seu limite na nossa loja eh de: ", var_limite_credito, " Venha aproveitar!!")
    print('')

    return var_limite_credito, var_idade_cliente

########################################################
def verificar_produto(var_limite_credito_disponivel,
########################################################
                    var_quantidade_caracteres_nome_completo,
                    var_valor_produto,
                    var_idade_cliente,
                    var_quantidade_caracteres_primeiro_nome):

    #                    ATIVIDADE 3
    #Verificar o desconto que o cliente tera no produto comprado
        # -> Cliente tera desconto caso o valor do produto esteja entre a quantidade de caracteres do nome e a idade do mesmo.
    if float(var_quantidade_caracteres_nome_completo) < float(var_valor_produto) < float(var_idade_cliente):
        var_valor_desconto = (int(var_quantidade_caracteres_primeiro_nome) * int(var_valor_produto)) / 100
        var_valor_final = float(var_valor_produto) - var_valor_desconto
        print("Voce tera um desconto de: ", int(var_quantidade_caracteres_primeiro_nome), "%")
        print('Seu desconto em R$ foi de: ', var_valor_desconto)
        print("Voce pagara pelo produto o valor de: ", float(var_valor_final))
    else:
        print("Produto sem desconto")
        var_valor_final = var_valor_produto

    #Verificar se cliente pode comprar e forma de parcelamento
    if float(var_valor_produto) <= float(var_limite_credito_disponivel * 0.6):
        var_limite_credito_disponivel = float(var_limite_credito_disponivel) - float(var_valor_final)
        print("Produto Liberado")
    elif float(var_limite_credito_disponivel * 0.6) < float(var_valor_produto) <= float(var_limite_credito_disponivel * 0.9):
        var_limite_credito_disponivel = float(var_limite_credito_disponivel) - float(var_valor_final)
        print("Produto liberado ao parcelar em ate 2x")
    elif float(var_limite_credito_disponivel * 0.9) <= float(var_valor_produto) <= float(var_limite_credito_disponivel):
        var_limite_credito_disponivel = float(var_limite_credito_disponivel) - float(var_valor_final)
        print("Produto liberado ao parcelar em ate 3x")
    else:
        var_limite_credito_disponivel = float(var_limite_credito_disponivel)
        if float(var_limite_credito_disponivel) < float(var_valor_produto):
            print('Sem saldo disponivel para esta compra')
        else:
            print("Bloqueado")

    return var_limite_credito_disponivel

##############################################################################
#               INICIO DA EXECUCAO, CHAMADADA DAS FUNCOES                    #
##############################################################################
from datetime import date
var_data_atual = date.today()
var_quantidade_caracteres_nome_completo = len("Chica da Silva")
var_quantidade_caracteres_primeiro_nome = len("Chica")

#CHAMA A FUNCAO PARA OBTER LIMITE/QTDE PRODUTOS DESEJADO
var_limite_credito, var_idade_cliente = obter_limite()

var_qtde_produtos = input("Digite a quantidade de produtos que deseja: ")
while var_qtde_produtos.isalpha():
    var_qtde_produtos = input("Quantidade invalida, ditite novamente: ")

# Solicita os dados do produto conforme quantidade desejada
var_limite_credito_disponivel = float(var_limite_credito) - 0
var_qual_produto = 0

########################################################
#Loop para digitar os produtos
########################################################
for c in range(int(var_qtde_produtos)):
    print("".format(c + 1))
    var_qual_produto = var_qual_produto + 1
    print('VAMOS DIGITAR AS INFORMACOES DO PRODUTO ', var_qual_produto)

    var_nome_produto = input("Digite o nome do Produto: " )

    var_valor_produto = input("Digite o valor do produto : ")
    while var_valor_produto.isalpha():
        var_valor_produto = input("Valor invalido, ditite novamente: ")

    #CHAMA A FUNCAO PARA VERIFICAR SE PODE COMPRAR OS PRODUTOS
    var_limite_credito_disponivel = verificar_produto(var_limite_credito_disponivel,
                                          var_quantidade_caracteres_nome_completo,
                                          var_valor_produto,
                                          var_idade_cliente,
                                          var_quantidade_caracteres_primeiro_nome)

    if var_limite_credito_disponivel <= 0:
        print('########################################################')
        print('Infelizmente seu limite acabou para compras de novos produtos, ate breve !!')
        print('########################################################')
        break
    else:
        print('########################################################')
        print('Seu saldo disponivel eh de: ', var_limite_credito_disponivel)
        print('########################################################')