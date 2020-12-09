# importing modules
import requests
from bs4 import BeautifulSoup
import texttable as tt

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
        deaths = deaths.replace(',', '')
        deaths_last7 = deaths_last7.replace(',', '')
        deaths_daily_increase = deaths_daily_increase.replace(',', '')
        population = population.replace(',', '')
        deaths_1m = deaths_1m.replace(',', '')
        deaths_1m_last7 = deaths_1m_last7.replace(',', '')

        # For 'confirmed' and 'deaths',
        # make sure to remove the commas
        # and convert to int
        data.append((
            country,
            int(deaths),
            int(deaths_last7),
            int(deaths_daily_increase),
            float(population),
            float(deaths_1m),
            float(deaths_1m_last7)
        ))

    # StopIteration error is raised when
    # there are no more elements left to
    # iterate through
    except StopIteration or ValueError:
        break

# Sort the data by the number of confirmed cases
data.sort(key=lambda row: row[1], reverse=True)

# create texttable object
table = tt.Texttable()

# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None, None, None, None)] + data)

# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c', 'c', 'c', 'c'))
table.header((' Country ', ' Deaths ', ' Deaths (last 7 days) ', ' Deaths (daily increase)', ' Population ', ' Deaths (per 1m)', ' Deaths (per 1m last 7 days)'))

print(table.draw())
