#----------------------------------------------------------------------------------------------------------------------#
# AmBev - Python classes
# Author: Raphael Eloi
#----------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------#
#PART 05: Define a function that shows the results
#----------------------------------------------------------------------------------------------------------------------#

def congrats():
    if (win == 1):
        print('Congrats, ' + user_1 + '. You won!')
        exit()
    elif (win == 2):
        print('Congrats, ' + user_2 + '. You won!')
        exit()
    elif (win == 3):
        print('Tic Tac Toe! Please try again!')
        exit()
    return 0

#----------------------------------------------------------------------------------------------------------------------#
#PART 01: Knowing the users and choosing the symbols
#----------------------------------------------------------------------------------------------------------------------#

user_1 = input('Hey, 1st player! Welcome to AmBev Tic Tac Toe! What is your name?')
user_2 = input('Hey, 2nd player! Welcome to AmBev Tic Tac Toe too! What is your name?')
symbol_1 = input("Hello, " + user_1 + '. Please choose if you are going to be X or O:')
symbol_1 = symbol_1.upper()     # Garante que, caso o usuário tenha escrito em minúsculo, o "if" a seguir funcione
if (symbol_1 == "X"):
    symbol_2 = "O"
elif (symbol_1 == "O"):
    symbol_2 = "X"
else:
    symbol_1 = "O"
    symbol_2 = "X"

print('Alright, so ' + user_1 + ' plays with "' + symbol_1 + '" and ' + user_2 + ' plays with "' + symbol_2 + '".')

#----------------------------------------------------------------------------------------------------------------------#
#PART 02: Explaining the rules and positions
#----------------------------------------------------------------------------------------------------------------------#

print('You can choose where to play following the positions showed below:')

A11 = "A11"
A12 = "A12"
A13 = "A13"
A21 = "A21"
A22 = "A22"
A23 = "A23"
A31 = "A31"
A32 = "A32"
A33 = "A33"

print('   ' + A11 + '   |  ' + A12 + '  |   ' + A13 + '\n ------------------------- \n   ' + A21 + '   |  ' + A22 + '  |   ' + A23  + '\n ------------------------- \n   ' + A31 + '   |  ' + A32 + '  |   ' + A33 )

#----------------------------------------------------------------------------------------------------------------------#
#PART 03: Choosing the positions
#----------------------------------------------------------------------------------------------------------------------#

print('Now, we are going to start!')

#Setting all matrix variables as "blank" to get the real tic tac toe structure and "win" initialization as "0"
A11 = ""
A12 = ""
A13 = ""
A21 = ""
A22 = ""
A23 = ""
A31 = ""
A32 = ""
A33 = ""
win = 0

print('   ' + A11 + '   |  ' + A12 + '  |   ' + A13  + '\n ---------------- \n   ' + A21 + '   |  ' + A22 + '  |   ' + A23 + '\n ---------------- \n   ' + A31 + '   |  ' + A32 + '  |   ' + A33 )

#----------------------------------------------------------------------------------------------------------------------#
#PART 04: Filling the blanks
#----------------------------------------------------------------------------------------------------------------------#

#Beginning of While
while win == 0:
    move = input('Please, choose the position for your move, ' + user_1 + ':')
    move = move.upper()
    if (move == "A11"):
        A11 = symbol_1
    elif move == "A12":
        A12 = symbol_1
    elif (move == "A13"):
        A13 = symbol_1
    elif (move == "A21"):
        A21 = symbol_1
    elif (move == "A22"):
        A22 = symbol_1
    elif (move == "A23"):
        A23 = symbol_1
    elif (move == "A31"):
        A31 = symbol_1
    elif (move == "A32"):
        A32 = symbol_1
    elif (move == "A33"):
        A33 = symbol_1

    print('   ' + A11 + '   |  ' + A12 + '  |   ' + A13 + '\n ---------------- \n   ' + A21 + '   |  ' + A22 + '  |   ' + A23 + '\n ---------------- \n   ' + A31 + '   |  ' + A32 + '  |   ' + A33 )

    if (A11 == A12 and A12 == A13 and A11 != ""):
        win = 1
    elif (A21 == A22 and A22 == A23 and A21 != ""):
        win = 1
    elif (A31 == A32 and A32 == A33 and A31 != ""):
        win = 1
    elif (A11 == A21 and A21 == A31 and A11 != ""):
        win = 1
    elif (A12 == A22 and A22 == A32 and A12 != ""):
        win = 1
    elif (A13 == A23 and A23 == A33 and A13 != ""):
        win = 1
    elif (A11 == A22 and A22 == A33 and A11 != ""):
        win = 1
    elif (A13 == A22 and A22 == A31 and A13 != ""):
        win = 1
    else:
        win = 0

    if (A11 != "" and A12 != "" and A13 != "" and A21 != "" and A22 != "" and A23 != "" and A31 != "" and A32 != "" and A33 != ""):
        win = 3

    congrats()

    #End of player 1 move and start of player 2 move

    move_2 = input('Please, choose the position for your move, ' + user_2 + ':')
    move_2 = move_2.upper()         #Transforma em maiuscula para evitar erros quando o usuário insere minúscula
    # Verificação se o jogador #1 ganhou
    if move_2 == "A11":
        A11 = symbol_2
    elif move_2 == "A12":
        A12 = symbol_2
    elif move_2 == "A13":
        A13 = symbol_2
    elif move_2 == "A21":
        A21 = symbol_2
    elif move_2 == "A22":
        A22 = symbol_2
    elif move_2 == "A23":
        A23 = symbol_2
    elif move_2 == "A31":
        A31 = symbol_2
    elif move_2 == "A32":
        A32 = symbol_2
    elif move_2 == "A33":
        A33 = symbol_2

    print('   ' + A11 + '   |  ' + A12 + '  |   ' + A13 + '\n ---------------- \n   ' + A21 + '   |  ' + A22 + '  |   ' + A23  + '\n ---------------- \n   ' + A31 + '   |  ' + A32 + '  |   ' + A33 )

    if (A11 == A12 and A12 == A13 and A11 != ""):
        win = 2
    elif (A21 == A22 and A22 == A23 and A21 != ""):
        win = 2
    elif (A31 == A32 and A32 == A33 and A31 != ""):
        win = 2
    elif (A11 == A21 and A21 == A31 and A11 != ""):
        win = 2
    elif (A12 == A22 and A22 == A32 and A12 != ""):
        win = 2
    elif (A13 == A23 and A23 == A33 and A13 != ""):
        win = 2
    elif (A11 == A22 and A22 == A33 and A11 != ""):
        win = 2
    elif (A13 == A22 and A22 == A31 and A13 != ""):
        win = 2
    else:
        win = 0

    if (A11 != "" and A12 != "" and A13 != "" and A21 != "" and A22 != "" and A23 != "" and A31 != "" and A32 != "" and A33 != ""):
        win = 3

    congrats()

    #End of While

#----------------------------------------------------------------------------------------------------------------------#
