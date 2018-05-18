from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code


if __name__ == '__main__':
    countries = ['Andorra', 'United Arab Emirates', 'Uruguay']
    for country in countries:
        print(get_country_code(country))
