from src.pregunta import *
from src.jugador import *
from src.leftGame import *
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
      #Creamos un objeto de tipo Pregunta para acceder a los métodos de dicha clase
      preguntaAux = pregunta("","","","","","")
      #Se genera una nueva pregunta, le pasamos como parametro la ronda actual de juego para
      #que así el programa muestre una pregunta aleatoria de la categoría asociada a dicha ronda.
      currentQuestion = preguntaAux.generateNewQuestion(self.ronda)
      aux.append(currentQuestion.option1)
      aux.append(currentQuestion.option2)
      aux.append(currentQuestion.option3)
      aux.append(currentQuestion.correctOption)
      A = currentQuestion.showQuestion(currentQuestion)
      A1 = A[1:5]
      random.shuffle(A1)
      #Almacenamos la pregunta y mostramos su enunciado y sus opciones de respuesta en desorden(aleatorio)
      print("*****************************************************************")
      print(f"Ronda #{str(self.ronda)}, la categoría es {currentQuestion.category}.")
      print("*****************************************************************")
      print(A[0])
      for i in range(4):
        print(f"{i+1}.",A1[i].rstrip("\n"))
      print(f"0. Salir del juego (Se guardará tu progreso en la ronda {str(self.ronda)})")
      while(True):
        answer = int(input())
        if(answer == 0):
          juegoPerdido = leftGame(jugador,self) #En caso de que el usuario haya decidido salirse se llama a la clase leftGame para almacenar el progreso de dicha partida
          sys.exit()
        #Se llama a al metodo validaQuestion de la clase Pregunta para así poder determinar si la respuesta fue correcta
        elif(not currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
          print("Falso!")
          jugador.removeProgress()#Sí el jugador pierde se elimina su progreso, así que la proxima vez que juegue tiene que empezar desde la ronda 1
          return self.ronda
        elif(answer> 4 or answer< 1):
          print("Por favor, ingresa una opción válida")
        else:
          jugador.score = (self.ronda*2)*1000 #Cada ronda tiene un premio diferente, claramente la ronda 5, por ser la de mayor dificultad tiene un premio mayor
          print(f"Correcto!, tu puntaje hasta el momento es de {jugador.score}") 
          break
        if(self.ronda == 5 and currentQuestion.validateQuestion(currentQuestion,A1[int(answer)-1])):
          jugador.removeProgress()#Sí el jugador gana se elimina su progreso, así que la proxima vez que juegue debe empezar desde cero
          return False
  
  def resumeGame(self,player):
    #Este metodo busca en la base de datos si hay algún juego en progreso asociado al jugador que se le haya pasado como parametro
    ruta = "inProgress/"+(player.userName).lower()+".txt"
    f=open(ruta,"r")
    lastMatch = f.readlines()[-1]
    previousRound = lastMatch.split(";")
    return int(previousRound[2]) #Retorna la ronda en la cual se quedó el jugador la ultima vez que jugó

  def quitGame(self):
    sys.exit() #Cierra el juego