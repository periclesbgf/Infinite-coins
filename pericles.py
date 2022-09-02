""" Made by Péricles Buarque de Gusmão Filho in 02/09/2022 """

""" Esse código funciona recursivamente:

 Primeiro ele vai receber um input do usuário (número) e a posição do array onde se encontra
 a moeda de valor mais alto, nesse caso a de 25(quarters). Então passa como parâmetro para a
 função makeChange que irá recebe-los e virificar se a posição no vetor é menor do que a quantidade
 de moedas nele - 1, pois o final do array é o elemento 3. Então ele vai verificar se o numero menos
 a moeda atual é negativo, pois se for, significa que o numero não é divisivel pela moeda e ele adicionará
 0 no array e assim passará para proxima moeda chamando a funcao novamente e passando agora indice da moeda + 1,
 ou seja, moeda que será analizada é 10 (dimes), ele vai fazer a verificação se o numero menos a moeda for negativo,
 caso não for negativo ela vai para outra etapa, nessa etapa vem o i, que é a quantidade de moeda que cabe no numero,
 por exemplo: " 25 cabe uma vez em 30". Então, entra no while, porque agora terá i vezes de possibilidades de representar
 esse valor, exemplo: "O numero 5 cabe uma vez em 8, mas temos a possibilidade de usar 1 moeda de 5 e 3 de 1, e 0 moedas de 5,
 e 8 de 1, consequentemente o numero 8 teria duas possibilidades", com isso, ele adiciona o valor de vezes que a moeda cabe
 no numero em um array, ele vai adicionar na posição em que a moeda está representada no array, se a moeda for 25, ele adiciona
 na posição 0, se for 1, na ultima posição... Então ele verifica se o numero - moeda é 0, pois siginifica que a divisão é
 exata, assim, ele chama a função novamente agora com outra moeda até ela ser a ultima moeda, ou seja, quando for 1, então
 ele entra no Else que vai pegar o resto(num), e multiplicar por 1, após isso ele adicionar o array no array list. 
 Voltando então para a chamada da função anterior, e diminuindo o i em 1, significando a outra possibilidade,
 por exemplo, o numero 30, temos a possibilidade de ter 1 moeda de 25 ou não, se não tiver ele vai ter que compensar colocando
 três de 10. Ele vai continuar assim até não ter mais possibilidades, ou seja, até que todos os "i's" forem vistos.
 
 Em poucas palavras: Input = 12
 1 - 25 cabe em 12? Não
 2 - 10 cabe em 12? Sim, então temos a possibilidade de ter 1 moeda 10 ou não ter,
 3 - Se tem moeda 10, proximo valor é 2. 5 cabe em 2? Não
 4 - 1 cabe em 2? Sim, então então ficaria array = [0 1 0 2]
 5 - Voltando para tópico 2. Possibilidade de não ter a moeda,
 6 - 5 cabe em 12? Sim, duas vezes, então temos a possibilidade de ter 2, 1 ou 0 moedas de 5
 7 - Tendo duas moedas de 5, sobra 2 moedas, pois (2 * 5) - 12 = 2
 8 - 1 cabe em 2? Sim, então array = [0 0 2 2]
 9 - Volta para o topico 6, agora temos a possibilidade de 1 moeda de 5,
 10 - (12 - 5) = 7, então ele passaria para a proxima moeda(1) valendo 7, então array = [0 0 1 7]
 11 - volta para topico 6, agora com 0 moedas de 5, sobrando 12 moedas de 1, então array = [0 0 0 12]
 
 Adicionei mais duas funções, uma para mostrar o array list na tela, e outra para printar o numero de possibilidades.
 """


def makeChange(num, moeda):
    if moeda < len(moedas) - 1:
        if num - moedas[moeda] < 0:
            aux[moeda] = 0
            makeChange(num, moeda + 1)
        elif num - moedas[moeda] >= 0:
            i = num//moedas[moeda]
            while i != -1:
                aux[moeda] = i
                if moedas[moeda] * i == 0:
                    makeChange(num, moeda + 1)
                else:
                    makeChange(num - (moedas[moeda] * i), moeda + 1)
                i -= 1
    else:
        aux[moeda] = moedas[moeda] * num
        list.append(aux.copy())


def size():
    return print(f"Há {len(list)} possibilidades de escrever o numero {value} com as moedas de 25, 10, 5 e 1 centavos")


def toArray():
    return print(list)


value = int(input())
aux = [0, 0, 0, 0]  # Vetor que coleta as possibilidades
list = []  # Vetor em que são salvo todas as possibilidades
moedas = [25, 10, 5, 1]  # Vetor com moedas
makeChange(value, 0)  # Chamada da função principal
toArray()  # Chamada da Função de exibir na tela os valores
while 1:
    inp = input("\n1 - Size\n2 - Print list\nOther - exit\n")
    if inp == '1':
        size()
    elif inp == '2':
        toArray()
    else:
        exit()
