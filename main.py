import os
import sys
from src.jugador import *
from src.game import *
print("Hola!, Bienvenido al concurso de preguntas, qué quieres hacer.")
print("1. Crear un nuevo usuario.")
print("2. Ingresar con un usuario existente.")
print("Ingresa qué opción eliges: ")
eleccion = int(input())
if eleccion == 1:
  currentPlayer = jugador()
  currentPlayer.newPlayer()
if eleccion == 2:
  while(True):
    print("Ingresa tu nombre de usuario: ")
    currentPlayer = jugador()
    usuario = input()
    if(currentPlayer.validatePlayer(usuario)):
      break;
  
  