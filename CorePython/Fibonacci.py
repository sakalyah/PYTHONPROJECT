a=0
b=1
#print (a,b,end=" ")
count =0
sequence = int(input(str("Sequence ?")))
print(a,b)
while count<sequence:
  c = a+b
  print (c ,end =" ")
  a=b
  b=c
  count = count + 1




