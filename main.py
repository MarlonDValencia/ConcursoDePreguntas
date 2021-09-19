import os
import sys
from src.jugador import *
from src.game import *
from src.wonGame import *
from src.lostGame import *
print("***************************************************************")
print("Hola!, Bienvenido al concurso de preguntas, qué quieres hacer.")
print("1. Crear un nuevo usuario.")
print("2. Ingresar con un usuario existente.")
print("Ingresa qué opción eliges: ")
eleccion = int(input())

def resultado(juego,player,ronda):
  if(not juego.startGame(player,ronda)):
    juegoGanado = wonGame(player)
  else:
    print(f"Incorrecto!, tu puntaje final fue de {player.score}")
  return None

def jugar(player):
  if(not player.gameInProgress()):
    juego = game()
    resultado(juego,player,0)
  elif(player.gameInProgress()):
    print("Tienes un juego en progreso, quieres reanudarlo o quieres empezar de cero?")
    print("1. Reanudar partida.")
    print("2. Empezar nuevo juego.")
    choose = input()
    if(choose=="1"):
      juego = game()
      ronda = (juego.resumeGame(player))-1
      resultado(juego,player,ronda)
    else:
      juego = game()
      resultado(juego,player,0)

if eleccion == 0:
  sys.exit()

if eleccion == 1:
  currentPlayer = jugador()
  print("Ingresa el nombre de usuario deseado")
  while(True):
    name = input()
    if(not currentPlayer.newPlayer(name)):
      print("Ese nombre de usuario ya está registrado, por favor intenta con otro: ")
    else:
      print("Usuario creado exitosamente")
      break
  jugar(currentPlayer)

if eleccion == 2:
  while(True):
    print("Ingresa tu nombre de usuario: ")
    currentPlayer = jugador()
    usuario = input()
    if(currentPlayer.validatePlayer(usuario)):
      print("Bienvenido de nuevo, "+currentPlayer.userName+"!")
      break;
    else:
      print("Nombre de usuario no encontrado, Intenta de nuevo \n")
  jugar(currentPlayer)
  