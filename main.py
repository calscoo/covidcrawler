from crawlers import worldometers_crawler, statista_crawler
import texttable as tt
from tools import merge_tools as mt

# dictionaries of covid data from crawlers
statista_data = statista_crawler.crawl()
worldometers_data = worldometers_crawler.crawl()

# averaging and combining the dictionaries, returning a list
data = mt.combine_data(statista_data, worldometers_data)

# sort by total deaths (since both data sources contained this stat)
data.sort(key=lambda row: row[1], reverse=True)

# create a text table for display, set the header and add the data
data_table = tt.Texttable()
data_table.add_rows([(None, None, None, None, None, None, None, None, None)] + data)
data_table.set_cols_align(('c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c'))
data_table.header((' Country ', ' Deaths ', ' Deaths (last 7 days) ', ' Deaths (daily increase) ', ' Population ', ' Deaths (per 1m) ', ' Deaths (per 1m last 7 days) ', ' Confirmed ', ' Continent '))
data_table.set_cols_width([30, 20, 20, 20, 20, 20, 20, 20, 30])
print(data_table.draw())
