import os
import sys
from src.jugador import *
from src.game import *
from src.wonGame import *
from src.winners import *
print("***************************************************************")
print("Hola!, Bienvenido al concurso de preguntas, qué quieres hacer.")
print("1. Crear un nuevo usuario.")
print("2. Ingresar con un usuario existente.")
print("3. Ver la lista de ganadores")
print("Ingresa qué opción eliges: ")
eleccion = int(input())

#Todas las clases se encuentran en la carpeta src

#Determina el resultado de un juego (Perdido o Ganado)
def resultado(juego,player,ronda):
  if(not juego.startGame(player,ronda)):
    juegoGanado = wonGame(player)
  else:
    print(f"Incorrecto!, tu puntaje final fue de {player.score}")
  return None

#Determina si un jugador ya tenía un juego sin terminar o en caso contrario empieza uno nuevo
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

#Cierra la aplicación en caso de que así lo haya decidido el usuario
if eleccion == 0:
  sys.exit()
#Crear un usuario nuevo
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
#Iniciar sesión con un nombre de usuario que ya se encuentre en la base de datos
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

if eleccion == 3:
  winners = winners()
  cont = 0
  for i in winners.ganadores():
    value = (winners.ganadores())[i]
    print(f"{cont+1}. {i}: {value} victorias.")
    cont +=1
  