def city_country(city,country):
    """ Display city and country names """
    c_cname = f"{city}, {country}"
    return c_cname.title()
n = 0
while n < 3:
    n += 1
    City_name = input("Give me a city Name: ")
    Country_name = input("Give me a country Name: ")

    cc = city_country(City_name,Country_name)
    print(cc)