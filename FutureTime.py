#FutureTime.py
#Name:Fatima Davila
#Date:1/31/2025
#Assignment:Lab 2


# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour =( now.hour-6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  inputhr = input("hours")
  #Ask user for minutes
  inputmin = input("minutes")
  moreMins = (60 * int(inputhr) + int(inputmin) )

  futureMins = (currentMinute + moreMins) % 60
  extraHour =  ( (currentHour + (currentMinute + moreMins ) // 60) % 24 )
  print(str(extraHour)+ ":" + str(futureMins))
  print(extraHour)
  print(futureMins)
  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.
 
  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
