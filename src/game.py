from src.pregunta import *
from src.jugador import *
from src.lostGame import *
import sys
class game:
  ronda = 0
  finished = False;
  def __init__(self):
    return None;
  #La función startGame recibe un objeto de tipo jugador como parametro.

  def startGame(self,jugador,ronda):
    self.ronda = ronda
    while(True):
      aux = []
      self.ronda += 1
      preguntaAux = pregunta("","","","","","")
      currentQuestion = preguntaAux.generateNewQuestion(self.ronda)
      aux.append(currentQuestion.option1)
      aux.append(currentQuestion.option2)
      aux.append(currentQuestion.option3)
      aux.append(currentQuestion.correctOption)
      A = currentQuestion.showQuestion(currentQuestion)
      A1 = A[1:5]
      random.shuffle(A1)
      print("*****************************************************************")
      print(f"Ronda #{str(self.ronda)}, la categoría es {currentQuestion.category}.")
      print("*****************************************************************")
      print(A[0])
      for i in range(4):
        print(f"{i+1}.",A1[i].rstrip("\n"))
      print(f"0. Salir del juego (Se guardará tu progreso en la ronda {str(self.ronda)})")
      answer = input()
      if(answer == "0"):
        juegoPerdido = lostGame(jugador,self)
        sys.exit()
      elif(not currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
        print("Falso!")
        jugador.removeProgress()
        return self.ronda
      else:
        jugador.score = (self.ronda*2)*1000
        print(f"Correcto!, tu puntaje hasta el momento es de {jugador.score}")
      if(self.ronda == 5 and currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
        jugador.removeProgress()
        return False
  
  def resumeGame(self,player):
    ruta = "inProgress/"+(player.userName).lower()+".txt"
    f=open(ruta,"r")
    lastMatch = f.readlines()[-1]
    previousRound = lastMatch.split(";")
    return int(previousRound[2])

  def quitGame(self):
    sys.exit()