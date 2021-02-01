cities = {
    'chennai' : {
        'country' : 'india',
        'population' : '10 million',
        'fact' : 'worlds 2nd longest beach',
    },
    'new york city' : {
        'country' : 'America',
        'population' : '5 million',
        'fact' : 'most populated city in america',
    },
    'london' : {
        'country' : 'england',
        'population' : '2 million',
        'fact' : 'sherlock holmes lives there',
    }

}
for city,info in cities.items():
    print(city+':')
    country = info['country']
    pop = info['population']
    fact = info ['fact']
    print("\tCountry: "+country)
    print("\tPopulation: "+pop)
    print("\tfact: "+fact)

