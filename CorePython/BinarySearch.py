
h = [34,35,46,67,78,90,109,5678] #Always Given List should be Sorted in some order

l = 0
u = len(h)-1
n = 46

while l <=u :
    mid = (l+u)//2  # // STands INteger Division
    if h[mid]==n:
        print("Number found at "+mid.__str__())
        break
    elif h[mid]!=n:
        if h[mid] < n: #Search Value greater than mid value then l = mid + 1
            l = mid+1
        else: #Search Value lesser than mid value then u = mid - 1
            u = mid-1
else:
    print(n.__str__()+" NOT FOUND")