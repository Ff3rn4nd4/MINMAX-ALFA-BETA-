import math

# Definir la estructura


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')

# Inicializando el teclado


def freeSpace(position):
    if board[position] == ' ':
        return True
    else:
        return False

# Checando que la posicion este vacia


def checkBoard():
    for key in board.keys():
        # si hay posiciones vacias aun se puede seguir jugando
        if (board[key] == ' '):
            return False
    return True

# Funcion de evaluacion
    # Generales


def checkForWin():
    # Filas
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    # Columnas
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    # Diagonales
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

    # Con estas verificamos el ganador bot/persona


def checkWhichMarkWin(mark):
    # Filas
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    # Columnas
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    # Diagonales
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

# Funcion de utilidad


def Turn(simbol, position):
    if freeSpace(position):
        board[position] = simbol
        printBoard(board)
        if checkForWin():
            if simbol == 'O':
                print("El bot gana!")
                exit()
            else:
                print("Ganaste!")
                exit()
        if (checkBoard()):
            print("Empate!")
            exit()

        return

    else:
        print("Esta posicion esta ocupada xc")
        position = int(input("Ingresa una nueva posicion: "))
        Turn(simbol, position)
        return


def playerMove():
    position = int(input("Ingrese la posicion para 'X':  "))
    Turn(player, position)
    return


def compMove():
    # solo se necesita la mejor opcion de este
    bestScore = -math.inf
    bestMove = 0
    #esta variable sirve para podar ramas
    alpha = -math.inf
    #esta variable sirve para retener ramas 
    beta = math.inf
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False, alpha, beta)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
            alpha = max(alpha, bestScore)
    Turn(bot, bestMove)
    return

def minimax(board, depth, isMaximizing, alpha, beta):
    if checkWhichMarkWin(bot):
        return 1
    elif checkWhichMarkWin(player):
        return -1
    elif checkBoard():
        return 0

    if isMaximizing:
        bestScore = -math.inf
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False, alpha, beta)
                board[key] = ' '
                bestScore = max(score, bestScore)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        return bestScore

    else:
        bestScore = math.inf
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True, alpha, beta)
                board[key] = ' '
                bestScore = min(score, bestScore)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return bestScore

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = 'X'
bot = 'O'
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
printBoard(board)


# Turnos en juego
while not checkBoard() and not checkWhichMarkWin(player) and not checkWhichMarkWin(bot):
    playerMove()
    if not checkBoard() and not checkWhichMarkWin(player) and not checkWhichMarkWin(bot):
        compMove()
