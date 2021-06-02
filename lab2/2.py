#Задаём класс конечного акцептора
class Acceptor:

  def __init__(self, alphabet, states, initialState, endState):
    self.alphabet = set(alphabet)
    self.states = states
    self.initialState = initialState
    self.endState = set(endState)

  #Допускается ли input акцептором
  def accept(self, input): 
    state = self.initialState
    for char in input:
      if (char in self.alphabet) == False:
        return False        
      state = states[state][char]
    if (state in self.endState) == True:
      return True
    else:
      return False
alphabet = {'1', '0', 'a'}

#Задаём соответствующие переходы
states = {0:{'0':0, '1':1, 'a':0},
       1:{'0':0, '1':2, 'a':1},
       2:{'0':1, '1':2, 'a':3},
       3:{'0':0, '1':0, 'a':0}}

#Начальное значение
initialState = 0

#Конечное значение
endState = {3}

#Создаём объект по заданным параметрам
acceptor = Acceptor(alphabet, states, initialState, endState)

#Проверяем на нескольких примерах
print(acceptor.accept(""))
print(acceptor.accept("b"))
print(acceptor.accept("11aa"))
print(acceptor.accept("11aaa01aa11a"))