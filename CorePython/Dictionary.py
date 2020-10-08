My_Family ={"Father":'Bhaskar',"Mother":'Uma',"Sister":'Bandu'}
print(My_Family)
a = My_Family["Sister"]
print(My_Family.keys())
print(My_Family.values())
print(My_Family.items())
for fam in My_Family:
    print(fam +" " + My_Family[fam])
print(a)
Empty_dict = {}
Empty_dict['Comp1'] = 'CAPGEMINI'
Empty_dict['Comp2'] = 'COGNIZANT'
Empty_dict['Comp3'] = 'ZOHO'
print(Empty_dict)
d = {'k':{'a':'a1','b':'b1','c':'c1'}}
print(d)
print(d['k']['b'])
print(d.keys())
print(d.values())
print(d.items())
