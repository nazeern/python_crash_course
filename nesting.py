cities = {
    'edison': {
        'type': 'suburban',
        'size': 'medium',
        'fun fact': 'named after Thomas Edison'
        },
    'new york city': {
        'type': 'urban',
        'size': 'large',
        'fun fact': 'has 5 distinct boroughs'
        },
    'troy': {
        'type': 'urban',
        'size': 'medium',
        'fun fact': 'home of RPI'
        }
    }

for city, information in cities.items():
    print("\nCity: " + city.title())
    print("\tType: " + information['type'])
    print("\tSize: " + information['size'])
    print("\tFun Fact: " + information['fun fact'])