import datetime
import csv

filename = "data.csv"


def update():
  global today
  now = datetime.datetime.now()
  today = now.strftime("%Y-%m-%d")



def getfile():
  file = open(filename, "r")
  reader = csv.reader(file)
  return({rows[0]:rows[1] for rows in reader})
  file.close()


#getdayfile("2022-06-28")



def logvalue(value):
  update()
  file = open(filename, "a")
  writer = csv.writer(file)
  file.write(str(datetime.datetime.now())+","+str(value)+"\n")
  file.close()
  print("Logged",str(value))



def gettoday():
  update()
  file = getfile()
  total = 0
  for item in reversed(file):
    if today in item:
#      print(file[item])
      total += int(file[item])
    else:
      pass
  return(total)
