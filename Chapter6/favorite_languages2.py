favorite_languages = {
    'tony' : ['python','c#'],
    'rahul' : ['C'],
    'leo' : ['ruby','java','python'],
    'naruto' : ['R']
    
}

for name,lang in favorite_languages.items():
    if len(lang) == 1 :
        print(name.title()+"'s favorite language is:")
    else:    
        print(name.title()+"'s favorite languages are:")
    for l in lang:
        print("\t\t\t      "+l.title()) 
            