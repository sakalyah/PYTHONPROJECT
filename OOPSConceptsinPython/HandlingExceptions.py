import math

a= 5
b =0
try :
    c = a/b
    print(c)
    math.sqrt(25)

except ValueError as e1:
    print("Get Lost, you cant find square root of negative number" ,e1)
except Exception as e :
    print("Something went wrong")
finally:
 print("Bye, Check for some exceptions")