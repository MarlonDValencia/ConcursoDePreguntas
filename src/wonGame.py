import os
import sys
from src.game import *
from src.jugador import *
class wonGame(game):
  #__init__ es el constructor de la clase wonGame, cada que se cree una instancia de esta clase se ejecutará este método
  #Se guarda en la base de datos el nombre y puntaje del jugador que ganó, si un jugador ha ganado mas de una vez, lo agrega a su registro
  def __init__(self,jugador):
    ruta = "winners/"+(jugador.userName).lower()+".txt"
    if os.path.exists(ruta):
      f = open(ruta,"a")
      text = str(jugador.score)+";"+jugador.userName+"\n"
      f.write(text)
      f.close()
      print ("*****************************************************************************************")
      print (f"Felicidades {jugador.userName}, ganaste! 10000 Puntos han sido añadidos a tu registro!")
    else:
      f = open(ruta,"w")
      text = str(jugador.score)+";"+jugador.userName+"\n"
      f.write(text)
      f.close()
      print ("****************************************************************************************************")
      print (f"Felicidades {(jugador.userName).lower()}, ganaste! has sido añadido al registro de ganadores con 10000 puntos")
    return None

