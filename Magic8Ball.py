#Magic8Ball.py
#Name:Fatima
#Date:Davila
#Assignment:lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  response = input ("Im the great magic 8 ball..\n ask me a question...")
  answers = ["As I see it, yes", "Ask again later.", "Better not tell you now", "Cannot predict now.," "Concentrate and ask again." "Reply hazy, try again.", "Signs point to yes.", "Signs point to yes.", "You may rely on it."
          "Don’t count on it.", "It is certain.", "It is decidedly so." "Most likely.", "My sources say no.", "My reply is no.", "Outlook not so good.", "Outlook good", "Without a doubt.", "Yes.", "Yes – definitely." ]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r=random.random() * length
  r=int(r) #cut off any decimal value
  print(r) 
  response=answers[r]
  print(response)
if __name__ == '__main__':
  main()
