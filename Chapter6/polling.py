favorite_language = {
        'tony':'python',
        'leo' : 'c',
        'naruto': 'C#',
        'phil' : 'java',
        'david': 'python',
}
should_take = ['david','naruto','elon','rock lee']

for st in should_take:
    if st in favorite_language.keys():
        print("thank you for taking the poll "+ st)
    else:
        print(st+" you should take the poll")    