favorite_language = {
        'tony':'python',
        'leo' : 'c',
        'naruto': 'C#',
        'phil' : 'java',
        'david': 'python'
}

# print("tonys favorite language is " + 
#     favorite_language['tony'].title())

# for name,lang in favorite_language.items():
#         print(name.title()+"'s favorite language is " +lang.title())

# for name in favorite_language:
#         print("people who took the pool are "+name.title())

# friends = ['leo','naruto']
# for name in favorite_language.keys():
#         print(name.title())

#         if name in friends:
#                 print("Hi " + name.title()+
#                 " i didn't know your favorite language is "+
#                 favorite_language[name].title())

# if 'itachi' not in favorite_language.keys():
#         print("itach please pick a language you like")

# for name in favorite_language.keys():
#         print(name.title() + ", thank for taking the pool")

print("these are the languages students choose:")
for lang in set(favorite_language.values()):
        print(lang)