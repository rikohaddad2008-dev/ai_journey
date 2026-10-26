import time
import datetime as dt

print('this is the time app')
class clock:
  def __init__(self):
   pass
  
  def timer(self,n):
    self.n=n
    n=int(n)
    while n!=0:
        print(n)
        
        time.sleep(1)
        self.timer(n-1)
        break
    if n==0:
      print('horray')

  def secconnverter(self,second):
        print('your time is',dt.timedelta(seconds=second))

  def stopwatch(self,tim=0):
    self.tim=tim
    
    print(tim)
    time.sleep(1)
    self.stopwatch(tim+1)
    
r=clock()
r.timer(n=1)
r.secconnverter(99)