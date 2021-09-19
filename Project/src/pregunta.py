import os
import codecs
import random
x = []
questions = []
#Ronda 1; Preguntas de conocimiento general (General)
#Ronda 2; Preguntas de Entretenimiento
#Ronda 3; Preguntas de deportes
#Ronda 4; Preguntas de geografía
#Ronda 5; Preguntas de historia
class pregunta:
  statement = ""
  category = ""
  option1 = ""
  option2 = ""
  option3 = ""
  correctOption = ""

  def __init__(self,statement,category,option1,option2,option3,correctOption):
    self.statement = statement
    self.category = category
    self.option1 = option1
    self.option2 = option2
    self.option3 = option3
    self.correctOption = correctOption

  def generateNewQuestion(self,ronda):
    f = open("questions/questions.txt","r",encoding = "utf8")
    lines = f.readlines()
    for i in range(len(lines)):
      x.append(lines[i])

    for i in range(len(lines)):
      Q = lines[i].split(";")
      #Se crea una instancia por cada pregunta
      cQuestion = pregunta(Q[0],Q[1],Q[2],Q[3],Q[4],Q[5])
      questions.append(cQuestion)
    if(ronda == 5):
      return questions[random.randrange(0,5,1)]
    elif(ronda == 3):
      return questions[random.randrange(5,10,1)]
    elif(ronda == 1):
      return questions[random.randrange(10,15,1)]
    elif(ronda == 2):
      return questions[random.randrange(15,20,1)]
    elif(ronda == 4):
      return questions[random.randrange(20,25,1)]
    
  def validateQuestion(self,question,Answer):
    if question.correctOption == Answer:
      return True
    else:
      return False
      

  def showQuestion(self,question):
    return [question.statement,question.option1,question.option2,question.option3,question.correctOption]