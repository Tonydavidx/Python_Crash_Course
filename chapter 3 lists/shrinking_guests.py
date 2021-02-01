guest = ['Da Vinci', 'Napoleon', 'lupin', 'Bill Gates', 'Micheal Angelo']

print('Hello Mr.'+ guest[0] + " i admire you so much you are a marvelous man")
print("Hey " +guest[1] + " glad to see you")
print(""+guest[2]+ " Wondering in the moonlight are we")
print("Hi Mr." + guest[3]+ " thank you for windows \n")

print("Sadly Micheal Angelo was not able to join us\n")

guest[4] = 'Chandler'

print("Mr."+guest[0]+"i hope you are glad that mike could not come")
print("Make your self at home "+ guest[1])
print("please dont turn into wolf "+ guest[2])
print("thank you for coming Mr."+ guest[3])
print("Ah "+ guest[4] + " so nice to see you\n")

message = "i found a bigger dinner table " 

print(message+guest[0])
print(message+guest[1])
print(message+guest[2])
print(message+guest[3])
print(message+guest[4])

guest.insert(0,'Conan')
guest.insert(2,'Andy')
guest.append('Dravid')

greet ="Nice to to see you my man "
print(greet+guest[0])
print(greet+guest[1])
print(greet+guest[2])
print(greet+guest[3])
print(greet+guest[4])
print(greet+guest[5])
print(greet+guest[6])
print(greet+guest[7])

print("sorry Gentlemen the extra table will not arrive in time")
rg1 = guest.pop(2)
rg2 = guest.pop(3)
rg3 = guest.pop(4)
print(guest)
del guest[2]
del guest[2]
del guest[2]

msg_sorry = ['sorry Mr ',' there in no extra space']

print(msg_sorry[0]+rg1+msg_sorry[1])
print(msg_sorry[0]+rg2+msg_sorry[1])
print(msg_sorry[0]+rg3+msg_sorry[1]+"\n")

print("Mr."+guest[0]+"you all will be joining with me")
print("Mr."+guest[1]+"you all will be joining with me")
