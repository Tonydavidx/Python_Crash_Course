age = 9 

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'Adult'
elif age > 65:
    stage = 'elder'            

print('that person life stage is '+stage)    