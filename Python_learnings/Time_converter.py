#Todo
a = int(input(" State the seconds"))

if 0<=a<60:
  print(f"Hours:0 Minutes:0 Seconds:{a}")
elif 60<=a<3600:
  minutes = int(a//60)
  seconds = int(a - minutes*60)
  
  
  print(f"Hours:0 Minutes:{minutes} Seconds:{seconds}")


elif 3600<=a:
  hour = int(a//3600)
  minutes =  int(((a/60)-(hour*60)))
  seconds = int(a - (hour*3600) - (minutes*60))
  print(f"Hours:{hour} Minutes:{minutes} Seconds:{  seconds }")
else:
  print("Invalid input")
