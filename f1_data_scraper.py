from lxml import html
import requests
page = requests.get('https://www.motorsport.com/f1/results/2019/australian-gp-417660/')
tree = html.fromstring(page.content)
columns = tree.xpath('//th/text()')
drivers = tree.xpath('//span[@class="name"]/text()')
results = tree.xpath('//span[@class="ms-table_row-value"]/text()')

print(columns)
print(drivers)
print(results)