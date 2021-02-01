file = 'sherlock.txt'

with open(file, 'r' , encoding ='utf-8') as text:
    read = text.read()
    c = read.lower().count('hudson')
    print(c)