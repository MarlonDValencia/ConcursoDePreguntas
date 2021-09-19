import os
ganadores = []
dictWinners = {}
#Retorna un diccionario con todos los ganadores y las veces que hayan ganado
class winners():
  def ganadores(self):
    carpeta = "winners"
    for archivo in os.listdir(carpeta):
      ganadores.append(os.path.join(carpeta,archivo))
      if os.path.isdir(os.path.join(carpeta,archivo)):
        devolverArchivos(os.path.join(carpeta,archivo))
    for i in range(len(ganadores)):
      f = open(ganadores[i],"r")
      lines = f.readlines()
      for i in range(len(lines)):
        T = lines[i].split(";")
        dictWinners.update({T[1].rstrip():len(lines)})
    return(dictWinners)