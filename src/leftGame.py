import os
import sys
from src.game import *
from src.jugador import *
class leftGame():
  def __init__(self,jugador,game):
    ruta = "inProgress/"+(jugador.userName).lower()+".txt"
    f = open(ruta,"a")
    text = jugador.userName+";"+str(jugador.score)+";"+str(game.ronda)+";"+"notFinished"+"\n"
    f.write(text)
    f.close()
    print(f"Se guardará tu progreso, {jugador.userName}, La próxima vez que ingreses empezarás en la ronda {game.ronda}")
    return None
