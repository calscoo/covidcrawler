from scrapy.cmdline import execute

# The string to be executed in the command line
exec_string = "scrapy crawl quotes -O quotes.json"

execute(exec_string.split())
