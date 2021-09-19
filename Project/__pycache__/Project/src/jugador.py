import os
import sys
class jugador:
  score = 0
  userName = ""
  def setScore(self,points):
    self.score += points
  
  def newPlayer(self,name):
    self.userName = name
    ruta = "users/"+name.lower()+".txt"
    if os.path.exists(ruta):
      return False
    else:
      file = open(ruta,"w")
      return True

  def validatePlayer(self,name):
    self.userName = name
    ruta = "users/"+name.lower()+".txt"
    if os.path.exists(ruta):
      return(True)
    else:
      return(False)
  
  def gameInProgress(self):
    self.userName = self.userName
    ruta = "inProgress/"+(self.userName).lower()+".txt"
    if os.path.exists(ruta):
      return(True)
    else:
      return(False)
  
  def removeProgress(self):
    self.userName = self.userName
    ruta = "inProgress/"+(self.userName).lower()+".txt"
    if os.path.exists(ruta):
      os.remove(ruta)
      return(True)
    else:
      return(False)
