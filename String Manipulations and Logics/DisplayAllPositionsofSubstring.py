def substring_in_string(a,b):

    i =0
    n = len(a)
    flag = False
    print(type(flag))
    while i < n :
        s = a.find(b,i,n)
        if s!=-1:
            print("Substring found at :",s+1)
            i = s+1
            flag = True
        else:
            i = i+1
    if flag == False :
        print("Substring not found")

str1 = "Dhyan se Pade"
str2 = "Paade"
substring_in_string(str1,str2)






