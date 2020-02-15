# The board consists of 9 slots, named 1 to 9 from top left to bottom right:
#
#  1 2 3
#  4 5 6
#  7 8 9

# Declaração de Variáveis

slot1 = '1'
slot2 = '2'
slot3 = '3'
slot4 = '4'
slot5 = '5'
slot6 = '6'
slot7 = '7'
slot8 = '8'
slot9 = '9'



# Functions

# Printa o game board

def board(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9):

    print('\n'+slot1, '|', slot2, '|', slot3,'\n'+slot4, '|', slot5, '|', slot6,'\n'+slot7, '|', slot8, '|', slot9)



# Faz as jogadas em cada rodada

def Jogada(x, round, a1, a2, a3, a4, a5, a6, a7, a8, a9):

    # Varíavel que fica em 1 se o input for uma entrada possível, como slot1, slot2, etc, e fica 0 se a entrada for
    # incorreta, como "jj", "34sd" ou qualquer outro caracter que o programa não tenha instruções sobre como lidar
    controle = 0

    # Escolha de player - Player1 é X e Player2 é O
    if round%2!=0:
        b='X'
    else:
        b='O'

    # Escolha da casa onde vai jogar
    if x=='slot1':
        controle+=1
        # O if/else abaixo confere se a casa já recebeu jogada e impede de sobrepor
        if a1 == '1':
            a1 = b
            # Este round dentro do if impede que o jogador mude quando há uma tentativa de sobrepor slots.
            # Em outras palavras, uma tentativa de sobrepor cai no else, e o round não varia, mantendo o mesmo jogador.
            round += 1
        else:
            print('\n\nEste slot já foi jogado! Escolha outro: ')

    if x=='slot2':
        controle += 1
        if a2 == '2':
            a2 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot3':
        controle += 1
        if a3 == '3':
            a3 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot4':
        controle += 1
        if a4 == '4':
            a4 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot5':
        controle += 1
        if a5 == '5':
            a5 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot6':
        controle += 1
        if a6 == '6':
            a6 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot7':
        controle += 1
        if a7 == '7':
            a7 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot8':
        controle += 1
        if a8 == '8':
            a8 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if x=='slot9':
        controle += 1
        if a9 == '9':
            a9 = b
            round += 1
        else:
            print('\n\nEste slot já foi jogado. Escolha outro: ')

    if controle==0:
        print('\n\nJogada inválida. Jogue uma posição válida: ')

    return round, a1, a2, a3, a4, a5, a6, a7, a8, a9



# Analisa se alguma sequência de 3 casas foi fechada, garantindo a vitório do jogador - não identifica o
# jogador vitorioso, apenas retorna o símbolo que venceu dentro da variável c

def Vitoria(b1, b2, b3, b4, b5, b6, b7, b8, b9):

    c=''

    if b1!='':
        if b2==b1:
            if b3==b1:
                c=b1
        if b5==b1:
            if b9==b1:
                c=b1
        if b4==b1:
            if b7==b1:
                c=b1

    if b2!='':
        if b5==b2:
            if b8==b2:
                c=b2

    if b3!='':
        if b6==b3:
            if b9==b3:
                c=b3
        if b5==b3:
            if b7==b3:
                c=b3

    if b4!='':
        if b5==b4:
            if b6==b4:
                c=b4

    if b7!='':
        if b8==b7:
            if b9==b7:
                c=b7

    return c



# Main

print('\nEsse é o tabuleiro do jogo:')
print('\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')

round = 1

while round<1000:
    x = input('\nJogador, digite onde quer jogar. Por exemplo, se quer jogar no slot1, digite slot1: ')
    #A construção dos slots recebendo o valor de jogada e também sendo args de jogada é para que seja feita a substituição
    #sem que sejam perdidos os valores iniciais atribuídos aos slots. Ao rodar a função, um dos slots será mudado para X ou O,
    #mas os demais devem continuar vazios (''), por isso eles entram na função e a função retorna os próprios slots para eles mesmos.
    round, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9 = Jogada(x, round, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9)
    board(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9)
    d=Vitoria(slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9)

    if d=='X':
        print('\nVitória Player 1!')
        exit()
    if d=='O':
        print('\nVitória Player 2!')
        exit()