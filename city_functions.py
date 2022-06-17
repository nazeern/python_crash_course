def get_city_country(city, country, population=''):
    title = city.title() + ", " + country.title()
    if population:
        title += ": Population -- " + str(population)
    return title

