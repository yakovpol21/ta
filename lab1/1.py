#Состояние автомата определяется следующими тремя свойствами, представленными как глобальные переменные
#Состояние игровой доски, номер (фигура) игрока который сейчас ходит, состояние игры (в процессе, победа Х/0, ничья)

#Начальное состояние автомата - Доска с пустыми ячейками
board =[[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
playerS = 1
gameOv = 0

#grab принимает координаты клетки доски
def grab(i, j):
  global playerS
  global board
  #Если клетка занята или находится за пределами доски, то команда возвращает ошибку
  if (i < 0 or i > 2 or j < 0 or j > 2 or board[i][j] != 0):
    print ("oops")
    return
  #Если клетка свободна, то команда меняет состояние доски и состояние  игрока
  else :
    board[i][j] = playerS
    playerS = -playerS
  return

#gameOvCheck проверяет окончилась ли игра.
def gameOvCheck():
  global gameOv 
  #Имеется набор конечных состояний доски, где один из играющих побеждает
  conditions = [[0, 0, 0, 1, 0, 2], [1, 0, 1, 1, 1, 2], [2, 0, 2, 1, 2, 2],
                [0, 0, 1, 0, 2, 0], [0, 1, 1, 1, 2, 1], [0, 2, 1, 2, 2, 2],
                [0, 0, 1, 1, 2, 2], [0, 2, 1, 1, 2, 0]]

  #Стоят ли в этих положениях одинаковые фигуры, не равные пустой клетке
  for check in conditions:
    if (board[check[0]][check[1]] == board[check[2]][check[3]] == board[check[4]][check[5]] != 0):
      #Состояние окончания игры меняется на победу одного из игроков
      gameOv = board[check[0]][check[1]]
      return 
  #Проверяется не закончилась ли игра ничьей
  drawCheck = 0
  for i in range(3):
    for j in range(3):
      if (board[i][j] == 0):
        drawCheck = 1
  if (drawCheck == 0):
    gameOv = 2

#reinitGame возвращает автомаат в начальное состояние
def reinitGame():
  global board
  global playerS
  global gameOv
  board = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
  playerS = 1
  gameOv = 0

#Основной цикл игры
while (1):
  print("Enter the vertical position:")
  i = int(input())
  print("Enter the horizontal position:")
  j = int(input())
  grab(i,j)
  print(str(board[0]) + "\n" + str(board[1]) + "\n" + str(board[2]))
  gameOvCheck()
  if (gameOv != 0):
    if (gameOv == 2):
      print("It's a Draw!\nAnother round?\ny/n")
    else:
      print("Game over! " + str(gameOv) + " wins\nAnother round? \ny/n")
    a = input()
    if (a == "y"):
      reinitGame()
    else :
      break