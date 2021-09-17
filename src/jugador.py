import os
import sys
class jugador:
  score = 0
  userName = ""
  def setScore(self,points):
    self.score += points
  
  def newPlayer(self):
      while(True):
        print("Ingresa el nombre de usuario deseado")
        name = input()
        ruta = "users/"+name.lower()+".txt"
        if os.path.exists(ruta):
          print("Ese nombre de usuario ya está registrado, por favor intenta con otro")
        else:
          file = open(ruta,"w")
          print("Usuario creado exitosamente")
          break

  def validatePlayer(self,name):
    ruta = "users/"+name.lower()+".txt"
    if os.path.exists(ruta):
      print("Bienvenido de nuevo, "+name+"!")
      return(True)
    else:
      print("Nombre de usuario no encontrado :(")
      return(False)