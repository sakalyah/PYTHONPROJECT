#SHould always specify the type of file
#f = open('Harish.txt','r')
#f = open("Harish.txt",'w')
f = open("Harish.txt",'a')
print(f)
#print(f.read())
#f.write("This is through Write COmmand in Python")#TO write we need to change to write mode
#print(f.read())
f.write("This through Append1")
f.write("This through Append2")
f.write("This through Append3")


