Str = "Harish is learning Python"

print(len(Str))
n = 0
ls1 =[]
rev = -1
ls2=[]
#Printing each CHaracter Logic
while n < len(Str):
    print(Str[n], end='')
    ls1.append(Str[n])
    n= n+1
print()
print(ls1)
#Printing Reverse Order Logic
while rev>= -(len(Str)):
    print(Str[rev], end='')
    ls2.append(Str[rev])
    rev = rev-1
print()
print(ls2)
STR = "".join(reversed(Str))
print(STR)
#Substring inside a String
str1 = "KKR and RCB are playing Today's Match"
str2 ="KKR and RCB"
if str2 in str1:
    print(str2+" is in "+ str1)
else:
    print("Something Went wrong")

str3 = "      Harish learns Python     "
print(str3.rstrip())
print(str3.lstrip())
print(str3.strip())
#Finding Substring using find and index methods
#find() method
str4 = "Enter String 4 = "
str5 = "Enter Sub String= "
s = str4.find(str5,0,len(str4))
if s==-1:
    print("Substring not found")
else:
    print("Substring Found",s+1)
#IndexMethod
str6 = "Pani hota hail 100 Percent Pure"
str7 = "Harish"
try :
    n1 = str6.index(str7, 0, len(str6))
except ValueError as e1 :
    print("SubString not found",e1)
    raise ValueError
else:
    print(str7+" found at ",n1+1)



