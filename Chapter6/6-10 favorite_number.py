favorite_num = {
    'tony':[19,54,12],
    'leo':[25,1],
    'naruto':[54,22,5,4,65],
    'kaka':[8],
    }

for name,fnum in favorite_num.items():
    if len(fnum) >= 2:
        print(name+"'s Favorite numbers is :")
    else:
        print(name+"'s Favorite number is :")    
    for num in fnum:
        print(num)
