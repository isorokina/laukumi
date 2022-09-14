from math import*
from xml.etree.ElementTree import PI
class Prizmas():
    H=12
   
    def pamataLaukums(self,n,a):
        return (n*a*a)/(4*tan(3/n))




print(Prizmas.H)
atr=Prizmas()
print(atr.pamataLaukums(6,2))
atr1=atr.pamataLaukums(6,2)
print(atr1)

