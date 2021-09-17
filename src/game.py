from src.pregunta import *
from src.jugador import *
class game:
  ronda = 0
  Finished = False;
  def __init__(self):
    return None;
  #La función startGame recibe un objeto de tipo jugador como parametro.
  def startGame(self,jugador):
    while(True):
      aux = []
      self.ronda +=1
      jugador.score += 100
      preguntaAux = pregunta("a","a","a","a","a","a")
      currentQuestion = preguntaAux.generateNewQuestion(self.ronda)
      aux.append(currentQuestion.option1)
      aux.append(currentQuestion.option2)
      aux.append(currentQuestion.option3)
      aux.append(currentQuestion.correctOption)
      A = currentQuestion.showQuestion(currentQuestion)
      A1 = A[1:5]
      random.shuffle(A1)
      print(f"Ronda #{self.ronda}, la categoría es {currentQuestion.category}.")
      print(A[0])
      for i in range(4):
        print(f"{i+1}.",A1[i].rstrip("\n"))
      answer = input()
      if(not currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
        break;
      if(self.ronda == 5 and currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
        print("BIEEEEEEEEEEEEEEEN")
        break;



