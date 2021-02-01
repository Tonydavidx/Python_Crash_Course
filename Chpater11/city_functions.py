
def city_function(city,country,population = 0):
    """ format a city name and country """
    if population:
        formatted = f"{city}, {country} - population  {str(population)}"
        return formatted.title()

    else:
        formatted = f"{city}, {country}"
        return formatted.title()

