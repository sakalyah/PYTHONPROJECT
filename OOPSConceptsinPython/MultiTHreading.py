from threading import *
from time import sleep
class Hari(Thread):
    def run(self):
        for i in range(3):
            print ("Hari")
            sleep(1)

class Harish(Thread):
    def run(self):
        for i in range(3):
            print("Harish")
            sleep(1)

H1 = Hari()
H2 = Harish()
#WithoutMultithreading
# H1.run()
# H2.run()
#With MultiThreading
H1.start()
H2.start()

#print ("HELLO") #Main THread Statement.TO stop this execution we use join to the above objects
H1.join()
H2.join()
print("HELLo after Join")
