

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Write the name of a country: ')).lower()
    
    try:
        print('Estimated poblation of {} is: {} millions'.format(country, countries[country]))
    except KeyError:
        print('Country name -{}- not found, try with other'.format(country))