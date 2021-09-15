a = int(input(" State the seconds"))

if 0<=a<60:
  print(f"Hours:0 Minutes:0 Seconds:{a}")
elif 60<=a<3600:
  print(f"Hours:0 Minutes:{a//60} Seconds:{round((((a/60)-(a//60)))*60)}")
elif 3600<=a:
  print(f"Hours:{a//3600} Minutes:{int((round((a/3600)-(a//3600),7)*60))} Seconds:{  round((round((((round(((a/3600) - (a//3600)),7))*60)  -   (int((round((a/3600)-(a//3600),7)*60)))),7))*60) }")
else:
  print("Invalid input")



  
#9840
#100203