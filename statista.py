# importing modules
import requests
from bs4 import BeautifulSoup

# URL for scrapping data
url = 'https://www.statista.com/statistics/1104709/coronavirus-deaths-worldwide-per-million-inhabitants/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

# soup.find_all('td') will scrape every
# element in the url's table
data_iterator = iter(soup.find_all('td'))

# data_iterator is the iterator of the table
# This loop will keep repeating till there is
# data available in the iterator
while True:
    try:
        country = next(data_iterator).text
        deaths = next(data_iterator).text
        deaths_last7 = next(data_iterator).text
        deaths_daily_increase = next(data_iterator).text
        population = next(data_iterator).text
        deaths_1m = next(data_iterator).text
        deaths_1m_last7 = next(data_iterator).text

        # For 'confirmed' and 'deaths',
        # make sure to remove the commas
        # and convert to int
        data.append((
            country,
            int(deaths.replace(',', '')),
            int(deaths_last7.replace(',', '')),
            int(deaths_daily_increase.replace(',', '')),
            float(population.replace(',', '')),
            float(deaths_1m.replace(',', '')),
            float(deaths_1m_last7.replace(',', ''))
        ))

    # StopIteration error is raised when
    # there are no more elements left to
    # iterate through
    except StopIteration or ValueError:
        break

# Sort the data by the number of confirmed cases
data.sort(key=lambda row: row[1], reverse=True)
print(data)
