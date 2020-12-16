# Covid Truth Crawler

CTC (Covid Truth Crawler) is a Python web crawler that gathers and combines Covid-19 data from multiple sources.

## Installation

Download the source code from [github/calscoo/covidcrawler](https://github.com/calscoo/covidcrawler) and open with your python editor of choice

## Usage

```python
from crawlers import custom_x_crawler, custom_y_crawler
from tools import merge_tools

# dictionaries of covid table data from crawlers
x_data = custom_x_crawler.crawl()
y_data = custom_y_crawler.crawl()

# averaging and combining the dictionaries, returning a list
data = mt.combine_data(statista_data, worldometers_data)
```

## Output
This is simply for visualization.

```
+--------------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+--------------------------+
|          Country         |        Deaths        |    Deaths (last 7    |     Deaths (daily    |      Population      |    Deaths (per 1m)   |  Deaths (per 1m last |       Confirmed      |         Continent        |
|                          |                      |        days)         |      increase)       |                      |                      |       7 days)        |                      |                          |
+==========================+======================+======================+======================+======================+======================+======================+======================+==========================+
|      United States       |        308274        |        14327         |         3083         |       328.240        |       921.310        |        43.650        |       17347665       |      North America       |
+---------=----------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+--------------------------+
|          Brazil          |        183267        |         3804         |         964          |       211.050        |       866.140        |        18.020        |       7040608        |      South America       |
+--------------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+--------------------------+
.
.
.
+--------------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+--------------------------+
|          India           |        144292        |         2324         |         387          |       1366.420       |       105.460        |        1.700         |       9954769        |           Asia           |
+--------------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+--------------------------+
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Visit My Website
[calebolson.space](https://calebolson.space/)
