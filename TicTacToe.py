import os
from itertools import cycle
from colorama import Fore, Back, Style, init

init()
def clear():
    os.system('cls')


def allSame(l):
    if l.count(l[0]) == gameSize:
        return True
    return False


def checkWin():
    #Diagonal check
    pDiag = []
    sDiag = []
    for i, j in enumerate(reversed(range(gameSize))):
        pDiag.append(board[i][i])
        sDiag.append(board[i][j])
    if allSame(pDiag):
        return True
    if allSame(sDiag):
        return True

    #Horizontal Check
    for row in board:
        if allSame(row):
            return True

    #Vertical check
    for i in range(gameSize):
        vList = []
        for row in board:
            vList.append(row[i])
        if allSame(vList):
            return True
    return False


def updateBoard(sign, row, collumn):
    board[row][collumn] = sign


def validateChoice(row, collumn):
    if choice < 1 or choice > 9:
        print('The position must be from 1 to', gameSize ** 2)
        return False
    if board[row][collumn] != choice:
        print('This position is already taken. Try another position')
        return False
    return True


def displayBoard():
    clear()
    for row in board:
        print(' ', end = ' ')
        for i in row:
            if i == 'x':
                print(Fore.RED + i + Style.RESET_ALL, end = ' ')
            elif i == 'o':
                print(Fore.GREEN + i + Style.RESET_ALL, end = ' ')
            else:
                print(Style.DIM + str(i) + Style.RESET_ALL, end = ' ')
        print('')
    print('')

play = True
clear()
print('Enter player names.\nPlayer 1:', end = ' ')
player1 = input().strip()
print('Player 2:', end = ' ')
player2 = input().strip()
player = cycle([player1, player2])
while play:
    global board
    sign = cycle(['x', 'o'])
    gameSize = 3
    placeHolder = cycle(range(1, gameSize ** 2 + 1))
    board = [[next(placeHolder) for i in range(gameSize)] for _ in range(gameSize)]
    gameWon = False
    displayBoard()
    count = 0
    counted = False
    while not gameWon:
        currentPlayer = next(player)
        currentSign = next(sign)
        print('Current Player:', currentPlayer)
        rightChoice = False
        while not rightChoice:
            try:
                print('Enter position(from blanks):', end = ' ')
                choice = int(input())
                row = (choice - 1) // gameSize
                collumn = (choice - 1) % gameSize
                rightChoice = validateChoice(row, collumn)
            except Exception:
                print('Invalid input. Try again.')
                continue
        updateBoard(currentSign, row, collumn)
        displayBoard()
        gameWon = checkWin()
        count += 1
        if count == 9 and gameWon == False:
            print(Fore.BLUE + 'This round is a draw' + Style.RESET_ALL)
            counted = True
            gameWon = True
        if gameWon:
            if gameWon == True and counted == False:
                if count % 2 != 0:
                    print(Fore.RED + currentPlayer + Style.RESET_ALL, 'won this round.')
                else:
                    print(Fore.GREEN + currentPlayer + Style.RESET_ALL, 'won this round.')
            print('Want to play again?(y/n)', end = ' ')
            playAgain = input()
            if playAgain.lower() == 'y':
                print('restarting....')
                play = True
            else:
                play = False
