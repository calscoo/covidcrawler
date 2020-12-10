import requests
from bs4 import BeautifulSoup


def scrape():
    url = 'https://www.statista.com/statistics/1104709/coronavirus-deaths-worldwide-per-million-inhabitants/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = dict()
    # grab all table data on the page
    iterator = iter(soup.find_all('td'))
    while True:
        try:
            country = next(iterator).text
            deaths = next(iterator).text
            deaths_last7 = next(iterator).text
            deaths_daily_increase = next(iterator).text
            population = next(iterator).text
            deaths_1m = next(iterator).text
            deaths_1m_last7 = next(iterator).text

            # fix the formatting
            country = country.replace('¹', '').replace('USA', 'United States')
            deaths = deaths.replace(',', '')
            deaths_last7 = deaths_last7.replace(',', '')
            deaths_daily_increase = deaths_daily_increase.replace(',', '')
            population = population.replace(',', '')
            deaths_1m = deaths_1m.replace(',', '')
            deaths_1m_last7 = deaths_1m_last7.replace(',', '')

            # cast to proper types
            data[country] = (
                int(deaths),
                int(deaths_last7),
                int(deaths_daily_increase),
                float(population),
                float(deaths_1m),
                float(deaths_1m_last7)
            )

        except ValueError:
            break

    return data
