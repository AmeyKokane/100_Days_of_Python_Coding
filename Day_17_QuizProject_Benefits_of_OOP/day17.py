class Car:
    def __init__(self, seats,speed):
     self.seats = seats
     self.speed = speed
     self.numtyres = 4
   
#create an object from class Car  
honda = Car(5,90)

#print attribute of an object
print(honda.speed)