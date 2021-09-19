import os
import sys
from src.game import *
from src.jugador import *
class wonGame(game):
  def __init__(self,jugador):
    ruta = "winners/"+jugador.userName+".txt"
    if os.path.exists(ruta):
      f = open(ruta,"a")
      text = +str(jugador.score)+";"+jugador.userName+"\n"
      f.write(text)
      f.close()
      print (f"Felicidades {jugador.userName}, ganaste! 1500 Puntos han sido añadidos a tu registro!")
    else:
      f = open(ruta,"w")
      text = jugador.userName+";"+str(jugador.score)+"\n"
      f.write(text)
      f.close()
      print (f"Felicidades {jugador.userName}, ganaste! has sido añadido al registro de ganadores con 1500 puntos")
    return None

