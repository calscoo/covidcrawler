import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = dict()
    # grab all table data on the page
    iterator = iter(soup.find_all('td'))
    while True:
        try:
            country = next(iterator).text
            confirmed = next(iterator).text
            deaths = next(iterator).text
            continent = next(iterator).text

            # fix the formatting
            country = country.replace('¹', '').replace('USA', 'United States')
            confirmed = confirmed.replace(',', '')
            deaths = deaths.replace(',', '')

            # cast to proper types
            data[country] = (
                int(confirmed),
                int(deaths),
                continent
            )

        except StopIteration or ValueError:
            break

    return data
