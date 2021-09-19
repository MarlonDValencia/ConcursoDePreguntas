import os
import sys
class jugador:
  score = 0
  userName = ""
  #Suma una cantidad n de puntos al jugador
  def setScore(self,points):
    self.score += points
  
  #Crea un nuevo jugador y lo almacena en la base de datos (users)
  def newPlayer(self,name):
    self.userName = name
    ruta = "users/"+name.lower()+".txt"
    if os.path.exists(ruta):
      return False
    else:
      file = open(ruta,"w")
      return True
  
  #Valida si el nombre de usuario ingresado ya pertenece a otro jugador
  def validatePlayer(self,name):
    self.userName = name
    ruta = "users/"+name.lower()+".txt"
    if os.path.exists(ruta):
      return(True)
    else:
      return(False)
  
  #Valida si un jugador tiene un juego en progreso
  def gameInProgress(self):
    self.userName = self.userName
    ruta = "inProgress/"+(self.userName).lower()+".txt"
    if os.path.exists(ruta):
      return(True)
    else:
      return(False)
      
  #Elimina el progreso de un jugador
  def removeProgress(self):
    self.userName = self.userName
    ruta = "inProgress/"+(self.userName).lower()+".txt"
    if os.path.exists(ruta):
      os.remove(ruta)
      return(True)
    else:
      return(False)
